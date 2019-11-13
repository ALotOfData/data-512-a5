# A5: Final project plan

Benjamin Brodeur Mathieu

DATA 512A: Human-Centered Data Science

Nov 14, 2019

## **🧾 Motivation/problem statement**

For the final project, I will analyze Facebook ads used by the IRA (Internet Research Agency), a Kremlin supported "troll" farm, reported by the HPSCI (House of Representatives Minority Permanent Select Committee on Intelligence). The ads dating from 2015 to 2017 were identified to be related to the group by Facebook and were made public after a hearing was held between the HPSCI committee and social media companies.

### 🧐 Why is this important?

> "*On February 16, 2018 Special Counsel Robert S. Mueller III indicted 13 Russian individuals and three Russian organizations for engaging in operations to interfere with U.S. political and electoral processes, including the 2016 presidential election.*" - [HPSCI](https://intelligence.house.gov/social-media-content/)

In the 2016 elections, the United-States political system was influenced by a foreign power whose goal was to 

> "*sow discord in the U.S. political system, including the 2016 U.S. presidential election. Defendants posted derogatory information about a number of candidates, and by early to mid-2016, Defendants’ operations included supporting the presidential campaign of then-candidate Donald J. Trump (“Trump Campaign”) and disparaging Hillary Clinton.*" [- Indictment United States of America v. Internet Research Agency LLC](https://www.justice.gov/file/1035477/download)

As we are currently a year away from the 2020 presidential election, it is important to understand how these actors went about influencing the elections so that actions can be taken to recognize and ultimately undermine these efforts. Voting is **the** way American citizen's make their voice heard and influence decision making at a national level and, as a consequence of having one of the largest capital and a far reaching culture, a global level.

### 📌Background work

Due to the potential repercussions and scale of the issue, a lot of work has already been done by a variety of institutions to understand this dataset. These efforts can be divided into three categories:

1. 🗞Journalistic

    Articles by news outlet like the [New York Times](https://www.nytimes.com/2017/11/01/us/politics/russia-2016-election-facebook.html) and the [Wall Street Journal](https://www.wsj.com/articles/full-stock-of-russia-linked-facebook-ads-shows-how-propaganda-sharpened-1525960804), tend to summarize the issue, show key statistics such as the number of ads made available and focus on specific examples of outrageous advertisement crafted by the group. They also mention that the key goals of the IRA was to increase tension around divisive political issues.

2. 👩‍🎓Student / data enthusiasts

    This group made a variety of tools available, [like this one](https://russian-ira-facebook-ads.datasettes.com/russian-ads-919cbfd/faceted-targets?targets=%5B%22d6ade%22%5D), to investigate the dataset. Unfortunately these tools did not provide license terms and cannot be leveraged for this assignment. [Other groups on kaggle](https://www.kaggle.com/paultimothymooney/exploring-political-propaganda-on-facebook) did some key descriptive analysis and basic clustering analysis. One group of data enthusiast in particular, *tech for campaigns*, published [a comprehensive descriptive analysis of the dataset](https://medium.com/techforcampaigns/how-russian-trolls-won-american-hearts-and-minds-30037e1e13b7) which listed the findings below:

    - Trump and Hilary were not the focus of the ad campaign
    - Instead, identity politics were the main focus
    - Ads concentrated around African Americans and Conservatives
    - Analysis of ad spent, ad viewed and click through rates per demographic
3. 🌋Massive cross-dataset studies

    Two massive studies were conducted by merging the Facebook ads dataset with other sources of data. Below is a summary of their goals and findings.

    - 🔍**[On Microtargeting Socially Divisive Ads: A Case Study of Russia-Linked Ad Campaigns on Facebook](https://arxiv.org/pdf/1808.09218.pdf) - Multiple universities**

        This study focused on three issues:

        1. How divisive the IRA ads content was.

            > "*we conducted three online surveys on a U.S. census-representative sample (n=2,886). We used each survey to measure one of three axes along which ads could potentially be divisive: 1) reporting: whether respondents would report the ads, and why, 2) approval and disapproval: whether they approve or disapprove the content of the ad, and 3) false claims: if they are able to identify any false claims in the content of the ad. [...] We find that many of these ads were severely divisive, and generated strongly varied opinions across the two ideological groups of liberals and conservatives."*

        2. The effectiveness of the targeting of socially divisive ads

            > "*Click through rate was 10x higher than that of typical Facebook ads.*"

            > "*A deeper analysis of the demographic biases in the targeted audience reveals that the ads have been targeted at people who are more likely to approve the content and perceive fewer false claims, and are less likely to report.*"

        3. What features of Facebook's ad API were leveraged in targeting the ads?

            > "*Facebook provides a tool for advertisers that, given a target attribute, presents a list of other attributes that target people with similar demographic aspects.*"

            > "*We also provide strong evidence that these advertisers have explored the Facebook suggestions tool to engineer the targeted populations.*"

        During their analysis the team of researcher also:

        - Counted the number of ads created, their impressions, cost and received clicks over time.
        - Identified the groups that were more targeted.
        - Analyzed grouping by urls.
        - Analyzed the role of websites redirections.
- 📱**[The IRA, Social Media and Political Polarization in the United States, 2012-2018](https://comprop.oii.ox.ac.uk/wp-content/uploads/sites/93/2018/12/IRA-Report.pdf) - University of Oxford**

     The study looked at the Facebooks ads dataset and complemented it with facebook posts as well as their own content gathering from Twitter and Youtube. They also looked at the virality of the campaign through shares and likes. They identified that:

    > "*Peaks in advertising and organic activity often correspond to important dates in the US political calendar, crises, and international events*"

    > "*The most far reaching IRA activity is in organic posting, not advertisements*"

    Russia's IRA activities were designed to polarize the US public and interfere in elections by:

    > *- campaigning for African American voters to boycott elections
    - procedures in 2016, and more recently for Mexican American and Hispanic voters to distrust US institutions
    - encouraging extreme right-wing voters to be more confrontational
    - spreading sensationalist, conspiratorial, and other forms of junk political news and misinformation to voters across the political spectrum.*

    > Finally, the IRA was able to leverage their presence on multiple platforms once detection efforts caught up with them by redirecting traffic to platforms where their activities had not been disrupted, and by using their accounts on one social media platform to complain about suspensions of their accounts on another platform.

## 👨🏻‍🔬Research questions & methodology

Overall, the articles and studies did not have a strong focus on measuring the engagement users had with the ads. Although the "click through rate" might not be the best proxy to determine how engaged users were, it gives a baseline to understand the proportion of individuals who were compelled to action by the IRA's advertisement. My research will attempt to answer the following questions:

**Q1: Were some targeted demographics more engaged with the IRA ads?**

**Rationale**

Although this measure has been done by the "*[tech for campaigns](https://medium.com/techforcampaigns/how-russian-trolls-won-american-hearts-and-minds-30037e1e13b7)*" groups, it is unclear how the different studies identified targeted groups. By comparing targeted groups found using an algorithmic method with the groups identified in the two major studies and the "*tech for campaigns*" group post, I hope to give a more transparent account of how the classification can be done without referring to crowd work.

**Method**

1. Finding targeted demographics

    I will be using the "likes" used to filter users on each ads to find the targeted demographics. [K-means](https://en.wikipedia.org/wiki/K-means_clustering) clustering based on the [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (term frequency - inverse document frequency )of the "likes" will group together ads based on frequency of the different words in their "likes" section. Frequency of words within these groups will be used to give a specific demographic or interest group.

    I have chosen this approach because predictions made by the combination of these methods are easy to understand, explain and are reproducible (given the same algorithm and random seed are used). However, this method does not take into account visual cues from the ads themselves which would help with the determination.

2. Engagement by demographics

    To showcase engagement by demographics, box plots of the "click through rates" for the different demographics will be created. These plots will be supplemented with averages and median values. A brief section will report the findings. Box plots seem necessary to give an accurate portrayal as averages alone, which was the only value reported in the "*tech for campaigns*" post, are fallible to outliers.

**Q2: Are targeted demographics who are shown more ads more likely to interact with them?**

**Rationale**

The Oxford study mentioned that certain demographics where more targeted than others, but no study validated whether these more strongly targeted groups had larger "clicked through rates". Does the amount of ad seem to have an effect on how much user interacted with them? Does this hold true for certain demographics and not others?

**Method**

Total impressions and engagement percentages will be calculated for each of the targeted demographics. A scatterplot will be drawn and the shape of the data discussed. If the data is linearizable and satisfies the assumption for a linear regression model, the following null hypothesis will be tested:

**Q2_H0:** The number of ads seen had no impact on the click through rate

We can use age as a control variable, but an initial exploration of the dataset has shown other variables to be either highly correlated or sparsely populated.

**Q3: How did the amount of ads seen by targeted demographics change preceding political events?**

**Rationale**

The Oxford study was able to identify spikes in instagram posts around a series of important political events. Using the identified timeline, I will investigate if targeted demographics saw an increase in political ads in the weeks leading up to the same political events. 

It will be interesting to draw a parallel between the most targeted groups and the political affiliation (democrat, republican) and the type of the events (rally, protest, election etc.). I believe we will see different interest groups receiving more ads based on the political events.

**Method**

In order to compare demographic groups' numbers, I will be using a multiline graph showcasing the most targeted groups in terms of daily ad impressions. I have chosen daily impressions instead of the raw count of ads as the later is not representative of the total amount of time ads were posted on the website. If more than one event could have had an effect on the amount of ads seen and overlapped during an observed period, a graph containing multiple events will be used so that potential side-effects due to simultaneous political events can be discussed while looking at one chart.

For all three questions, ads which had at least one click, impression and cost will be used. The first cross-dataset study identified that due to these factors, ads with these attributes were unlikely to have been published by the IRA group.

---

## 🧪 **Data used**

### 🧩 Data source

The raw pdfs of the IRA's Facebook ads were made publicly available on the HPSCI's website.

1. HPSCI government [data website](https://intelligence.house.gov/social-media-content/social-media-advertisements.htm) and [information website](https://intelligence.house.gov/social-media-content/)
    - The dataset doesn't specify license/terms of use, but the text of the intelligence website's is clear that it is making the data available for public / academic use :

        > "*As part of that continuing effort to educate the public and seek additional analysis, the Committee Minority is making available all IRA advertisements identified by Facebook. This is an effort to be fully transparent with the public, allow outside experts to analyze the data, and provide the American people a fuller accounting of Russian efforts to sow discord and interfere in our democracy. [...] Congress does not have the technical expertise to fully analyze this data—that lies in outside groups such as news publications and academic researchers. We hope that the publication of these materials will facilitate this important work.*" - [HSPCI website](https://intelligence.house.gov/social-media-content/)

### ✏️ Data description

The descriptions in the table below were extracted from the [Enigma website](https://public.enigma.com/datasets/committee-minority-report-on-facebook-ads/619060d1-71ad-4764-8f2f-b5a3872c05c7) which hosts its own version of the dataset in csv format. I retroactively added the comments in parentheses.

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


### ⚖️ Ethical implications

The HPSCI website states that the data has been "carefully examined" and that PII (Personally identifiable information has already been removed).

> "*The Facebook advertisements we are publishing today have been carefully reviewed by the Committee Minority and redacted by Facebook to protect personally-identifiable information (PII). To protect innocent victims, Facebook—at the urging of the Committee Minority—also has notified users whose genuine online events were unwittingly promoted by the IRA.*" - [HPSCI](https://intelligence.house.gov/social-media-content/)

After examination of the dataset and the fields available, I feel comfortable to use it as it contains the advertisement created by the group, but no information linkable to users or their activities. 

---

## ⛈ **Unknowns and dependencies**

### 🔨 Technical hurdles

- The dataset linked above from the [enigma website](https://public.enigma.com/datasets/committee-minority-report-on-facebook-ads/619060d1-71ad-4764-8f2f-b5a3872c05c7) was not parsed correctly and could be much richer if the extraction of data from pdfs was done properly. I have already identified and tried open source utilities that can do most of the parsing of the raw HSPCI data, but a non-negligible amount of work remains to be done to obtain a full, rich dataset.
- Classifying demographics data based on "likes" will be difficult. The different entries are varied and some classification / associations will need to be carefully created and annotated to fully leverage the dataset. Some manual work may be required.

### ☠️ Non-technical hurdles

- Dental appointment on November 18th.
- Moving to a new apartment on December 15th.
- I'm currently in the process of transitioning from a software/data engineering  role to a data scientist role in my organization. The process of ramping up my responsibilities in this new work will take a significant amount of my time (in and potentially outside of work).