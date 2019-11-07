# A4: Final project proposal

## **🧾 Motivation/problem statement**

For the final project, I will analyze Facebook ads used by the IRA, a Kremlin supported "troll" farm, reported by the HPSCI (House of Representatives Minority Permanent Select Committee on Intelligence). The ads date from 2015 to 2017 when a public hearing was held with the committee and Social Media companies. By analyzing these ads, my goal is to gain a better understanding about how the IRA targeted users on social media in an effort to undermine  the U.S. political system during the 2016 presidential campaign.  Here are the main areas I would like to explore and why: 

1. Which demographics / locations were targeted and to which extend they were targeted.
    - Demographics / locations information are crucial in election campaigns to estimate the number of votes each party will obtain. This is because demographics and groups within the same location often share ideologies and tend to vote for the same candidate. Targeting a demographic in order to sway votes is a critical tactic employed by politicians.
    - I believe analyzing this data may reveal what the IRA thought would be the best demographics / locations to target in order to influence the 2016 election. Combining this information with election results could show which efforts were more fruitful.
2. Did the target demographics / locations vary over time during the campaign.
    - The IRA must have had mechanism to monitor their own influence. If so, it is likely that they could have adjusted their advertising tactics overtime. Examining the target location of ads may inform  how the group decided to pursue demographics that they felt had a larger impact.
3. Reach and overall spending
    - Understanding how many Facebook users were exposed to these ads and how they interacted with them can give us an idea of the reach of the IRA's effort. Similarly learning more about the total spending can advise our understanding of the breath of the campaign: Was this campaign closer to a probe or a "full on" attempt at swaying elections.

Overall, I am hopeful that this analysis can lead to a clearer picture of how the IRA ads attempted to influence the U.S. political process. As we are now a year away from the 2020 presidential elections, it is important to be able to identify similar patterns or ads we might come across during our social media usage so that they can be reported or dealt with scrutiny.


## 🧪 **Data used**

### 🧩 Data source

The enigma public group is providing a csv of text extracted from the raw pdf of the IRA's facebook ads made available on the HPSCI's website. The first source is made available using a creative commons license and the original source, although it doesn't explicitly state a license, makes a clear statement about academic use-cases.

1. [Enigma public csv](https://public.enigma.com/datasets/committee-minority-report-on-facebook-ads/619060d1-71ad-4764-8f2f-b5a3872c05c7)
    - Released as CC BY-NC 4.0.
2. HPSCI government [data website](https://intelligence.house.gov/social-media-content/social-media-advertisements.htm) and [information website](https://intelligence.house.gov/social-media-content/)
    - The dataset doesn't specify license/terms of use, but the text of the intelligence website's is clear that it is making the data available for public / academic use :

        > "As part of that continuing effort to educate the public and seek additional analysis, the Committee Minority is making available all IRA advertisements identified by Facebook. This is an effort to be fully transparent with the public, allow outside experts to analyze the data, and provide the American people a fuller accounting of Russian efforts to sow discord and interfere in our democracy. [...] Congress does not have the technical expertise to fully analyze this data—that lies in outside groups such as news publications and academic researchers. We hope that the publication of these materials will facilitate this important work." - [HSPCI website](https://intelligence.house.gov/social-media-content/)

### ✏️ Data description

The descriptions in the table below were extracted from the Enigma public website. I retroactively added the comments in parentheses.

| Field name        | Type    | Description                                                                     |
| ----------------- | ------- | ------------------------------------------------------------------------------- |
| Ad Id             | integer | Unique identifier assigned to Facebook advertisement.                           |
| Ad Text           | string  | Facebook advertisement text.                                                    |
| Ad Landing Page   | string  | URL to Facebook advertisement landing page.                                     |
| Ad Targeting      | integer | Facebook advertisement targeting, unparsed.                                     |
| Ad Impression     | integer | Number of Facebook advertisement impressions.                                   |
| Ad Clicks         | integer | Number of Facebook advertisement clicks.                                        |
| Ad Spend          | string  | Money spent on Facebook advertisement in Russian rubbles (RUB).                 |
| Ad Creation Date  | string  | Date Facebook advertisement was created in MM-DD-YY format.                     |
| Ad End Date       | string  | Date Facebook advertisement ended in MM-DD-YY format.                           |
| Target Location   | string  | Facebook advertisement target location. (state origin / state living)           |
| Target Age        | string  | Facebook advertisement target age.                                              |
| Target Language   | string  | Facebook advertisement target language. (language(s) spoken by target audience) |
| Target Placements | string  | Facebook advertisement target placements. (app and location)                    |
| Target People     | string  | Facebook advertisement target people. (likes)                                   |


This data seems to contains the information needed to evaluate the reach, spending and demographics of Facebook users targeted by the IRA's ad campaign. The "Target" fields can be used to understand demographics. The "Ad Spend" can be used to approximate spendings. The Creation and End date can be leverage to examine the density of ads targeting different demographics overtime and the "Ad Impressions" and "Ad Clicks" can inform pure reach (Impressions) and active interactions with the campaign (Clicks).  

### ⚖️ Ethical implications

The HPSCI website states that the data has been "carefully examined" and that PII (Personally identifiable information has already been removed).

> "The Facebook advertisements we are publishing today have been carefully reviewed by the Committee Minority and redacted by Facebook to protect personally-identifiable information (PII). To protect innocent victims, Facebook—at the urging of the Committee Minority—also has notified users whose genuine online events were unwittingly promoted by the IRA."

After examination of the dataset and the fields available, I feel comfortable to use it as it contains the advertisement created by the group, but no information linkable to users or their activities. 


## ⛈ **Unknowns and dependencies**

### 🔨 Technical hurdles

- The dataset linked above from the enigma website was not parsed correctly and could be much richer if the extraction of data from pdfs was done properly. I have already identified and tried open source utilities that can do most of the parsing of the raw HSPCI data, but a non-negligible amount of work remains to be done to obtain a full, rich dataset.
- Location data seems to be fairly easy to extract, but it is harder to classify demographics data. The different entries are varied and some classification / associations would need to be created to fully leverage the dataset.

### ☠️ Non-technical hurdles

- Dental appointment on November 12th.
- Moving to a new apartment on December 15th.
- I'm currently in the process of transitioning from a software/data engineering  role to a data scientist role in my organization. The process of ramping up my responsibilities in this new work will take a significant amount of my time (in and potentially outside of work).