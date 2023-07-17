# Project-3# Project-3

Members: Justin Talamantes, Mina Kemmer-Lee, Mason Wikoff


## Code Info / Data Process
Raw data was retrieved in CSV form. Data cleanup was preformed within Excell and Jupyter Notebook using Pandas. All data was stored and sorted in PostgreSQL.

Using Flask as our web framework, data stored within our PostgreSQL database was imported using psycopg2. Jsonify was used from the Flask Library to convert all SQL data into JSON format. 

The Javascript libraries Chart.js and Leaflet were used for data visualization. Chart.js was utililzed for data charting, while Leaflet was used to create a heatmap. Within the CSS, the Font Awesome ​library was used to integrate fonts to style buttons on the webpage.

## Summary
Our project covers the Covid-19 pandemic. Using data gathered from the CDC, US Census, and other smaller sites, we covered the impact of Covid in the US between the years 2021-2022 (this may also include data from 2020 and 2023). This includes death statistics and vaccine statistics, both on a country and state level.

## Conclusions
__How many deaths were caused by Covid between 2020-2023?__
- 14.78% of deaths between 2020-2023 were due to Covid and Covid related illnesses (Deaths from Covid and Deaths from Covid/Pneumonia)

__How many People were vaccinated in the US between 2021-2022?__
- About 223 million people were vaccinated in 2021 with about 190 million of those receiving both doses.
- In 2022, about 249 million people were vaccinated with about 213 million receiving both doses.

__How did Vaccines affect death rates?__
- During 2021 around 451,000 people died due to Covid and Covid related illnesses, while around 238,000 people died in 2022. This results in a 53% drop in deaths between the two years.

__Which state was the most and least affected by Covid?__
- West Virgina had the highest death rates for both 2021 and 2022. The deathrate for 2021 was 16.13 people per 100,000 people, this number postively drops in 2022 with 15.22 deaths per 1,000 people.
- New York had the lowest death rates for both 2021 and 2022. The deathrate for 2021 was 5.85 people per 1,000 people, this number nominally drops in 2022 with 5.69 deaths per 100,000 people.

## References: 
Provisional COVID-19 Deaths by Sex and Age (CDC)  
-  https://data.cdc.gov/NCHS/Provisional-COVID-19-Deaths-by-Sex-and-Age/9bhg-hcku

COVID-19 Vaccinations in the United States, by County (CDC) 
-  https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-Jurisdi/unsk-b7fc

State Populations (US Census)
-  https://www.census.gov/data/tables/time-series/demo/popest/2020s-state-total.html

US state Capitals Coordinates (stolen from someone’s github)   
-  https://github.com/jasperdebie/VisInfo/blob/master/us-state-capitals.csv


## Javascript Libraries:
Leaflet (Mapping)
- https://leafletjs.com/reference.html

Chart.JS (Charts)
- https://www.chartjs.org/docs/latest/

Font Awesome (Icons, Fonts)
- https://fontawesome.com/start


## Project Proposal: https://docs.google.com/document/d/1S5r0pV_Z4pcUn92i68-pTQz1liKfdy-L9NvOmP9dEjg/edit?usp=sharing

