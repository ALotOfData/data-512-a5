# A5: Facebook's Russian ads analysis

Name: Benjamin Brodeur Mathieu
Date: 11/05/2019

## Goal


## Repository structure
```
├── LICENSE
├── README.md
├── assets
│   └── pictures
│       └── ad_preview.png
├── clean_data
├── raw_data
└── src
```

| File                                          | Description                                                                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| LICENSE                                       | Code license                                                                                                             |
| README.md                                     | This readme.                                                                                                             |
| artifacts/data/ores_not_found.csv             | Entries in our dataset for which there were no article quality given by the [ORES](https://www.mediawiki.org/wiki/ORES). |
| artifacts/images/coverage.png                 | Coverage table screenshot. The table was created as part of analysis.                                                    |
| artifacts/images/relative_quality.png         | Relative article quality table screenshot. The table was created as part of the analysis.                                |
| clean_data/wp_wpds_countries_no_match.csv     | Article entries for which no match were found in the country's population list.                                          |
| clean_data/wp_wpds_politicians_by_country.csv | Article entries including quality rating and country's population.                                                       |
| human.yml                                     | [conda](https://docs.conda.io/en/latest/) environement file                                                              |
| raw_data/WPDS_2018_data.csv                   | Population resource bureau, mid-2018 population by country                                                               |
| raw_data/page_data.csv                        | Wikipedia politicians by country dataset                                                                                 |
| src/Whcds-a2-bias.ipynb                       | IPython notebook containing analysis (explanations and code)                                                             |

## Data sources used

The raw data is provided in zips of pdfs on the [HPSCI government website](https://intelligence.house.gov/social-media-content/social-media-advertisements.htm). 

> *The Facebook advertisements we are publishing today have been carefully reviewed by the Committee Minority and redacted by Facebook to protect personally-identifiable information (PII). To protect innocent victims, Facebook—at the urging of the Committee Minority—also has notified users whose genuine online events were unwittingly promoted by the IRA.* - [HPSCI](https://intelligence.house.gov/social-media-content/)

Each pdf files contained two pages. A first page with the description of the ad and the relevant information for this exercise (see image below). A second page containing an image of the ad.

![Russian ad description](./assets/pictures/ad_preview.png)
| field                             | description                                  |
| --------------------------------- | -------------------------------------------- |
| ad_id                             | Unique number for the ad                     |
| ad_text                           | Text visible on the ad                       |
| ad_landing_page                   | Hyperlink for ad click                       |
| ad_targeting_location             | Targeted location by the ad                  |
| ad_targeting_excluded_connections | Ad not shown criteria                        |
| ad_targeting_age                  | Targeted age group                           |
| ad_targeting_language             | Targeted language                            |
| ad_targeting_placements           | Targeted placement on page / in app          |
| ad_impressions                    | Number of users who scrolled by / saw the ad |
| ad_clicks                         | Number of clicks on ad                       |
| ad_spend                          | Money spend on ad with currency string       |
| ad_creation_date                  | Creation date of the ad                      |


* Data was accessed on 11/05/2019
* Released under a public license

### How to obtain the raw_data provided

After downloading and extracting the zip files and placing them under raw_data:

```
./raw_data/
├── 2015-06
├── 2015-q3
├── 2015-q4
├── 2016-q1
├── 2016-q2
├── 2016-q3
├── 2016-q4
├── 2017-04
├── 2017-05
├── 2017-q1
└── 2017-q3
```

Make sure to place them under raw_data before running the .ipynb notebook.

## Bias


## Resources used
This analysis was prepared using Python 3.7.5 running in a Jupyter Notebook environment.  
Documentation for Python can be found here: https://docs.python.org/3.7/  
Documentation for Jupyter Notebook can be found here: http://jupyter-notebook.readthedocs.io/en/latest/  

To extract the data we used the [xpdf](http://www.xpdfreader.com/about.html) pdf reader cli pdftotext.

The following Python packages were used and their documentation can be found at the accompanying links:

* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)
* [IPython](https://ipython.org/)

## Files Created
This notebook creates 2 CSV files of data extracted and compiled as part of this analysis.

* clean_data/wp_wpds_countries-no_match.csv 
* clean_data/wp_wpds_politicians_by_country.csv

Both share the same schema, some rows will have missing values in the no_match file.

| Column          | Description                                                                                                   | Data type |
| --------------- | ------------------------------------------------------------------------------------------------------------- | --------- |
| article_name    | The unsanitized page tytpe                                                                                    | string    |
| country         | sanitized country name, extracted from the category name                                                      | string    |
| revision_id     | edit ID of the last edit to the page                                                                          | string    |
| article_quality | An appoximation of article quality given by the ORES api learn more [here](https://github.com/wikimedia/ores) | string    |
| population      | Population in millions (thousands are comma separated)                                                        | string    |

## How to run the notebook

You will need a computer with access to the internet and access to a command line which has the required privileges to install open-source software.

> The human.yml file was created on OSX and will not work on linux or windows. If you are not on OSX, install the dependencies manually.

1. Install [conda or miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).
2. [Replicate the conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) using the human.yml file provided by running: `conda env create -f human.yml`
3. Activate the environment with: `conda activate human`
4. Using a terminal or cmd, navigate to the src folder.
5. Lauch jupyter by running: `jupyter notebook`
6. Select the hcds-a2-data-curation notebook.

## Observations

* Looking at the dataset more closely, we can see that more than 10 countries have no articles about a politician which obtained a quality rating of "FA" or "GA".
* Having very few articles makes it easy for a contributor to go and increase the relative_quality rating for a given country.
* Many of the countries having poor relative quality ratings also have a few number of articles.
* When looking at the region table, we see that the Northern America has the highest relative quality rating. This may be due to having a large number of english native speakers.

## Reflection
