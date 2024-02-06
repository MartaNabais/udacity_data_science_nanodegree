
### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

This code runs with Python 3.11.5 and requires some libraries:
- pandas              2.0.3
- plotly              5.9.0
- sklearn             1.3.0
- urlib3              1.26.16


## Project Motivation<a name="motivation"></a>

This year, I have started working for the Scottish Government, within the AI & Data Science unit. I am therefore looking to enhance my skills as a Data Scientist, to aid in implementing solutions that could help government make the fastest, best, and fairest decisions.

I have always been fascinated by crime, and I know I am not alone. The growing popularity of crime shows means big business and not just for streaming services — yes, I am looking at you, Netflix.

Beyond personal curiosity, crime statistics serve as a vital tool for shaping government policies. These statistics provide invaluable insights into the frequency and distribution of criminal activities, offering a compass for policymakers to navigate the complexities of law enforcement.

By understanding such patterns, authorities can strategically allocate resources, optimizing the deployment of police presence in areas with higher crime rates. Moreover, a nuanced analysis of crime statistics proves instrumental in identifying and addressing emerging crime problems, fostering a proactive and adaptable approach to maintaining public safety.

In here, I have analysed the “Recorded Crimes and Offences” dataset, which contains statistics on crimes and offences, including number of crimes/offences and crime/offence rates per 10,000 population recorded by Police Scotland from 1996/97 to 2022/23 and by Local Authority. I have decided to focus on three simple exploratory questions for my first project:

1. How have reported crime rates changed over time in Scotland?
2. In the past year, which countries show the highest increase and decrease in overall crime rates?
3. Which Scottish counties have more similar crime patterns?

## File Descriptions <a name="files"></a>

- first_blog_post.ipynb
    * This is a jupyter notebook containing the main analyses, with three main questions asked about the open “Recorded Crimes and Offences” dataset, from the Scottish Government

- data/scottish_crime_rates.csv
    * The main dataset analysed, downloaded from https://statistics.gov.scot.

- helper_functions.py
    * A python script containing some helper functions to parse the data imported into the jupyter notebook.

- _posts/2024-02-04-writing-a-data-science-post.md
    * The markdown file containing the blog post. The blog post is hosted on GitHub Pages and can be found [here](https://martanabais.github.io/udacity_data_science_nanodegree/), by clicking the button 'Writing a Data Science Blog Post'.

- Other folders / files
    * Are not specifically related to Udacity project, but they were used to build the website I am hosting the blog post.


## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://martanabais.github.io/udacity_data_science_nanodegree/), by clicking the button 'Writing a Data Science Blog Post'.

## Licensing, Authors, Acknowledgements<a name="licensing"></a>
Thank you to the Scottish Government and the partner organisations for providing the dataset used in this project. A list of can be found here: https://statistics.gov.scot/home.

