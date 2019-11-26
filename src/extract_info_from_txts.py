import re
import os
import copy
import pandas as pd

regex_dict = {
    'ad_line_start': r"^Ad\s+",
    # Sometimes pdf files wrote Id with an 1, l or I character the spacing was also inconsistent
    'ad_id': r"^A\s*d\s*(I|l|1)\s*D\s*(?P<ad_id>[0-9]*)",
    'ad_text': r"^A\s*d\s*Text\s*",
    'ad_landing_page': r"^Ad\s+Landing\s+Page\s+(?P<ad_landing_page>.*)",

    # ad targeting
    'ad_targeting': r"^Ad\s*Targeting\s*(?P<ad_targeting>.*)",

    'ad_impressions': r"^Ad\s*Impressions\s*:?\s*(?P<ad_impressions>.*)",
    'ad_clicks': r"^Ad\s*Clicks\s*:?\s*(?P<ad_clicks>.*)",
    'ad_spend': r"^Ad\s*spend\s*:?\s*(?P<ad_spend>.*)",
    'ad_creation_date': r"^Ad\s*creation\s*date\s*:?\s*(?P<ad_creation_date>.*)",
    'ad_end_date': r"^Ad\s*end\s*date\s*:?\s*(?P<ad_end_date>.*)"
}

# Order of these entries is important!
ordered_targeting_topics_regex = {
    'custom_audience': r'^custom\s*audience\s*:?\s*(?P<custom_audience>.*)',
    'location': r'^location\s*:?\s*(?P<location>.*)',
    'interests': r'^interests\s*:?\s*(?P<interests>.*)',
    'excluded_connections': r'^excluded\s*connections\s*:?\s*(?P<excluded_connections>.*)',
    'age': r'^age\s*:?\s*(?P<age>.*)',
    'language': r'^language\s*:?\s*(?P<language>.*)',
    'placements': r'^placements\s*:?\s*(?P<placements>.*)',
    'people_who_match': r'^people\s*who\s*match\s*:?\s*(?P<people_who_match>.*)'
}


def row_from_file(file_name, file_path, parse_errors_file_dict):
    with open(file_path, 'r') as ad_file:
        lines = ad_file.readlines()
        if lines is None and len(lines) == 0:
            parse_errors_file_dict['empty'].append(file_path)

        line_index = 0

        # ad_id
        (ad_id, line_index) = extract_inline('ad_id', file_name, lines, line_index, parse_errors_file_dict)

        # ad_text
        (ad_text, line_index) = extract_ad_text(file_name, lines, line_index, parse_errors_file_dict)

        # ad_landing_page
        (ad_landing_page, line_index) = extract_inline('ad_landing_page', file_name, lines, line_index,
                                                       parse_errors_file_dict)

        # ad_targeting (all ad_targeting is extracted here
        (ad_targeting_custom_audience,
         ad_targeting_location,
         ad_targeting_interests,
         ad_targeting_excluded_connections,
         ad_targeting_age,
         ad_targeting_language,
         ad_targeting_placements,
         ad_targeting_people_who_match,
         line_index) = extract_ad_targeting(
            file_name,
            lines,
            line_index,
            parse_errors_file_dict)

        # ad_impressions
        (ad_impressions, line_index) = extract_inline('ad_impressions', file_name, lines, line_index,
                                                      parse_errors_file_dict)

        # ad_clicks
        (ad_clicks, line_index) = extract_inline('ad_clicks', file_name, lines, line_index, parse_errors_file_dict)

        # ad_spend
        (ad_spend, line_index) = extract_inline('ad_spend', file_name, lines, line_index, parse_errors_file_dict)

        # ad_creation_date
        (ad_creation_date, line_index) = extract_inline('ad_creation_date', file_name, lines, line_index,
                                                        parse_errors_file_dict)

        # ad_end_date
        (ad_end_date, line_index) = extract_inline('ad_end_date', file_name, lines, line_index, parse_errors_file_dict)

    return [file_name,
            ad_id,
            ad_text,
            ad_landing_page,
            ad_targeting_custom_audience,
            ad_targeting_location,
            ad_targeting_interests,
            ad_targeting_excluded_connections,
            ad_targeting_age,
            ad_targeting_language,
            ad_targeting_placements,
            ad_targeting_people_who_match,
            ad_impressions,
            ad_clicks,
            ad_spend,
            ad_creation_date,
            ad_end_date]


def extract_ad_text(file_name, lines, line_index, parse_errors_file_dict):
    ad_text = None
    ad_text_end_found = False
    line = lines[line_index]

    matches = re.search(regex_dict['ad_text'], line, flags=re.IGNORECASE)
    if matches is not None and matches.span() is not (-1, -1):
        (_, end) = matches.span()
        ad_text_array = [line[end:]]
        new_line_index = line_index + 1
        while not ad_text_end_found and new_line_index < len(lines):
            line = lines[new_line_index]
            matches = re.search(regex_dict['ad_line_start'], line, flags=re.IGNORECASE)
            if matches is not None:
                break
            else:
                ad_text_array.append(line)
                new_line_index += 1

        ad_text = ''.join(ad_text_array)

    if ad_text is None:
        parse_errors_file_dict['ad_text'].append(file_name)
        new_line_index = line_index

    return ad_text, new_line_index


def extract_inline(regex_key, file_name, lines, line_index, parse_errors_file_dict):
    line = lines[line_index]
    matches = re.search(regex_dict[regex_key], line, flags=re.IGNORECASE)
    to_extract = None

    if matches is not None:
        group_dict = matches.groupdict()
        to_extract = group_dict.get(regex_key)

    # Add to fail to parse dictionary if regex was not comprehensive
    if to_extract is None:
        parse_errors_file_dict[regex_key].append(file_name)
        new_line_index = line_index
    else:
        new_line_index = line_index + 1

    return to_extract, new_line_index


def extract_ad_targeting(file_name, lines, line_index, parse_errors_file_dict):
    # Step 1) get all targeting related lines and next line
    targeting_lines, next_line_index = extract_targeting_lines(lines, line_index)

    # Step 2) get topic dictionary with list of target per topic
    topic_dictionary = get_topic_dictionary(targeting_lines) if targeting_lines else dict()

    # Step 3) assign topic dictionary entry to variables (get defaults to None)
    ad_targeting_custom_audience = topic_dictionary.get('custom_audience')
    ad_targeting_location = topic_dictionary.get('location')
    ad_targeting_interests = topic_dictionary.get('interests')
    ad_targeting_excluded_connections = topic_dictionary.get('excluded_connections')
    ad_targeting_age = topic_dictionary.get('age')
    ad_targeting_language = topic_dictionary.get('language')
    ad_targeting_placements = topic_dictionary.get('placements')
    ad_targeting_people_who_match = topic_dictionary.get('people_who_match')

    # Step 4) add parse errors

    return (ad_targeting_custom_audience,
            ad_targeting_location,
            ad_targeting_interests,
            ad_targeting_excluded_connections,
            ad_targeting_age,
            ad_targeting_language,
            ad_targeting_placements,
            ad_targeting_people_who_match,
            next_line_index)


def extract_targeting_lines(lines, line_index):
    targeting_lines = []

    # Step 1) check that the current line is the targeting line
    matches = re.search(regex_dict['ad_targeting'], lines[line_index], flags=re.IGNORECASE)
    if matches is None:
        return None, line_index
    else:
        location = matches.groupdict()['ad_targeting']
        targeting_lines.append(location)
        line_index += 1

    # Step 2) get lines
    next_line_index = line_index
    match_found = False
    while next_line_index < len(lines) and not match_found:
        line = lines[next_line_index]
        matches = re.search(regex_dict['ad_impressions'], line, flags=re.IGNORECASE)

        if matches is not None:
            match_found = True
        else:
            targeting_lines.append(line)
            next_line_index += 1

    if not match_found:
        targeting_lines = None
        parse_errors_file_dict['ad_targeting'].append(file_name)

    return targeting_lines, next_line_index if match_found else line_index


def get_topic_dictionary(targeting_lines):
    topic_regex = copy.deepcopy(ordered_targeting_topics_regex)
    topic_text_dictionary = {}
    current_topic = None
    for i in range(len(targeting_lines)):
        line = targeting_lines[i]

        for topic, regex in topic_regex.items():
            matches = re.search(regex, line, flags=re.IGNORECASE)

            if matches and matches.groupdict():
                # current_topic can match until new topic is found
                current_topic = topic

                # remove topic name from value using groups
                group_dict = matches.groupdict()
                line = group_dict.get(topic)

                # Once a topic is found it is removed
                topic_regex.pop(topic)
                break

        if current_topic is None:
            return None

        if current_topic in topic_text_dictionary:
            topic_text_dictionary[current_topic] += (' ' + line.replace('\n', ''))
        else:
            topic_text_dictionary[current_topic] = line if line is not None else ''

    return topic_text_dictionary


input_path = '../raw_data/txt_files/'
output_path = '../raw_data/raw.csv'

# Get all txt files under path
file_paths = []
all_rows = []
parse_errors_file_dict = {
    'ad_id': [],
    'ad_text': [],
    'ad_landing_page': [],
    'ad_targeting': [],
    'ad_targeting_custom_audience': [],
    'ad_targeting_location': [],
    'ad_targeting_interests': [],
    'ad_targeting_excluded_connections': [],
    'ad_targeting_age': [],
    'ad_targeting_language': [],
    'ad_targeting_placements': [],
    'ad_targeting_people_who_match': [],
    'ad_impressions': [],
    'ad_clicks': [],
    'ad_spend': [],
    'ad_creation_date': [],
    'ad_end_date': [],
    'empty': []
}

for root, directories, files in os.walk(input_path):
    for file_name in files:
        if ".txt" in file_name:
            txt_file_path = os.path.join(root, file_name)
            row_array = row_from_file(file_name, txt_file_path, parse_errors_file_dict)
            all_rows.append(row_array)

df = pd.DataFrame(all_rows, columns=[
    'file_name',
    'ad_id',
    'ad_text',
    'ad_landing_page',
    'ad_targeting_custom_audience',
    'ad_targeting_location',
    'ad_targeting_interests',
    'ad_targeting_excluded_connections',
    'ad_targeting_age',
    'ad_targeting_language',
    'ad_targeting_placements',
    'ad_targeting_people_who_match',
    'ad_impressions',
    'ad_clicks',
    'ad_spend',
    'ad_creation_date',
    'ad_end_date'
])
df.to_csv(output_path)
