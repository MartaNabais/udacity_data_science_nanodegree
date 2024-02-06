---
layout: post
title: "Crime Trends in Scotland: What is going on in Shetland?"
tags: CrimeTrends Scotland kMeans-clustering DataScience Python
---


<img src="https://ik.imagekit.io/panmac/tr:f-auto,w-740,pr-true//bcd02f72-b50c-0179-8b4b-5e44f5340bd4/7887d0f1-9ea1-46c9-bbf1-a23d6ec007da/ann-cleeves-shetland-series-2.jpg" width="1000" class="unconfined"/>

## Introduction

<p> This year, I have started working for the Scottish Government, within the AI & Data Science unit. I am therefore looking to enhance my skills as a Data Scientist, to aid in implementing solutions that could help government make the fastest, best, and fairest decisions.
</p>

<p> This exercise is a tiny first step into that journey, which is also being fostered by  <a href="#" onclick='window.open("https://www.udacity.com/course/data-scientist-nanodegree--nd025");return false;'> Udacity’s Nanodegree in Data Science.</a>
</p>

<p> I would also like to make clear that this is a personal post (i.e., not government work) and all views are my own. </p>

## The problem

<p>I have always been fascinated by (true) crime, and I know I am not alone. The growing popularity of (true) crime shows means big business and not just for streaming services — yes, I am looking at you, Netflix.
</p>

<p>As a society, our inherent curiosity drives us to closely examine instances of criminal activities, as we aim to unravel the intricate details of the criminal mind. We want to know <i>“who”, “what”, and “where”</i>, but most pervasively, we want to know <i>“why”</i>.
</p>

<p>Beyond personal curiosity, crime statistics serve as a vital tool for shaping <strong>government policies</strong>. These statistics provide invaluable insights into the frequency and distribution of criminal activities, offering a compass for policymakers to navigate the complexities of law enforcement.
</p>

<p> By understanding such patterns, authorities can strategically allocate resources, optimizing the deployment of police presence in areas with higher crime rates. Moreover, a nuanced analysis of crime statistics proves instrumental in identifying and addressing emerging crime problems, fostering a proactive and adaptable approach to maintaining public safety. 
</p>

<p> In the age of Artificial Intelligence (AI), the ethical debate of the role of AI in criminal justice is, or should be, unavoidable. Although 
    <a href="#" onclick='window.open("https://www.litcharts.com/lit/the-minority-report/summary");return false;'>predictive policing in the way of “Precogs” 
    </a> 
is still just a work of fiction, we need to actively advocate against implementation of governance strategies/tools that are hampered by algorithmic biases. This is crucial for human development, as a just and democratic society. For example,
</p>

<blockquote> there are at least six documented cases of illegal detention in the United States, all of them black people, due to automatic facial recognition systems that made a mistake
</blockquote>


<p> Alas, AI is not really the focus of this post, but I thought the paragraph above would be noteworthy. <a href="#" onclick='window.open("https://english.elpais.com/technology/2023-10-21/toju-duke-artificial-intelligence-amplifies-systemic-injustices-that-were-supposed-to-have-dropped-by-now.html#");return false;'> You can read this Toju Duke’s interview for more on this topic.</a> </p>


## The dataset
<p>The Scottish Government has made over 250 datasets from a range of producers publicly available at statistics.gov.scot. It is a great resource, and here I have focused on the “Recorded Crimes and Offences” dataset.
</p>
<p>This dataset contains statistics on crimes and offences, including number of crimes/offences and crime/offence rates per 10,000 population recorded by Police Scotland from 1996/97 to 2022/23 and by Local Authority. I have decided to focus on three simple exploratory questions for my first project.
</p>

## Question 1: How have reported crime rates changed over time in Scotland?

<p> Before answering my first question, I have to let you know I have only focused on “Crimes” and not “Offences”. This is because there may be some statistical differences between these terms. “Crime” is generally used for the more serious criminal acts; the less serious termed “offences”, although the term “offence” may also be used in relation to serious breaches of criminal law.
</p>

<p>In the figure below, you can see how crime rates have evolved over the years, for different counties in Scotland (you can hover over the lines to check for specific values): </p>

<iframe
  src="https://nbviewer.org/github/MartaNabais/udacity_html_first_project/blob/main/scottish_crime_ratios_over_time.html"
  style="height:400px; width: 100%;" frameborder="0">
</iframe>

<p style="text-align:center; color:grey;">Fig.1 - Scottish Crime Rates over the Years.</p>

<p> If we focus on the year 1996/1997 (left-most side of the figure), there are a couple of counties that stand out for having a lot more reported crimes than the rest. Here’s the <strong>top-three</strong>: 
</p>

<ul>
    <li><strong>Glasgow</strong> is first (with a staggering 1647 crimes reported for every 10,000 people) 🥇</li>
    <li><strong>Dundee</strong> comes in a close second 🥈</li>
    <li><strong>Aberdeen</strong> comes in third 🥉</li>
    Although I am not sure this is a race you would really want to win…
</ul>


<p>The <strong>bottom-three</strong> are all Scottish isles: <strong>Orkney, Shetland</strong> and <strong>Na h-Eileanan an Iar</strong> (the Outer Hebrides). 
</p>

<p> In conclusion, if I were more risk-averse and had to decide where I would relocate within Scotland, I would be tempted to embrace the island lifestyle! Nonetheless, if we follow the lines from the past to the end of 2022 (or left to right), we can see the <strong><i>trend</i></strong> across all counties looks good: crime rates seem to be going <strong>down</strong> in Scotland!</p>

## Question 2: In the past year, which countries show the highest increase and decrease in overall crime rates?

<p>Although there seem to be higher crime rates in the mainland compared to the isles, it may also be interesting to look how rates have been changing within each county. To help us answer this question, we can take the <strong><i>percentage change</i></strong> between crime rates for the most recent and past years.
</p>

<p>In the figure below, I have calculated the percentage change in crime rates for each county, between the years 2022/2023 (latest data provided) and 2021/2022. Positive numbers imply there has been a <strong><i>increase</i></strong> and negative numbers imply there has been a <strong><i>decrease</i></strong> in crime rates:
</p>

<iframe
src="https://nbviewer.org/github/MartaNabais/udacity_html_first_project/blob/main/percent_change_crimes.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>


<p> Interestingly, the three counties showing highest increase in crime rates in the past years are the three isles: <strong>Shetlands (40%), Orkney (39%) and Na h-Eileanan an Iar (33%). This would’ve been hard to conclude just by visually inspecting Fig.1!</strong>
</p>

<p>However, it is important to note this is a cross-sectional comparison, meaning it is only a snapshot of a point in time. Just because crime rates increased in the isles, does not mean they are expected to keep increasing over time.</p>

## Question 3: Which Scottish counties have more similar crime patterns?

<p> Looking at overall crime rates gives us a broad perspective of crime trends in Scotland. However, I would also like to understand if we can find <strong><i>similarity patterns</i></strong> between counties, by looking at the <strong><i>different crime types</i></strong>.
</p>

<p> Fortunately, our dataset contains such information. Indeed, if we take a look at the distributions of different crime type rates for some counties for last year: 
</p>

<iframe
src="https://nbviewer.org/github/MartaNabais/udacity_html_first_project/blob/main/different_crime_types_2022-2023.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>

<p>
If we compare the <strong><i>total value of crime rates</i></strong> and the <strong><i>proportions</i></strong> of different crime types between each county, we can see that some counties seem to have more similar patterns to one another. For example, Glasgow and Edinburgh are more similar to each other and the Orkney Islands are more similar to East Dunbartonshire.
</p>


<p>To assess this more formally, we can make use of mathematical algorithms. More specifically, I will make use of the <strong><i>k-Means Clustering algorithm</i></strong>. Without getting too much into details, this algorithm aims to partition data into <strong><i>k</i></strong> clusters in a way that data points in the same cluster are more similar to each other. This is exactly what I need to answer my question!
</p>

<p> After applying the algorithm using the different crime type rates as data points, I ended up with 4 different clusters:
<p></p>

<iframe
src="https://nbviewer.org/github/MartaNabais/udacity_html_first_project/blob/main/cluster_crimes_chloropeth.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>

<ul>
  <li> <strong> <a style="color:purple;">Cluster 1</a></strong>, consists of East Dunbartonshire and East Renfrewshire.
  </li> <strong> <a style="color:blue;">Cluster 2</a></strong>, consists of Aberdeen, Dundee, Edinburgh and Glasgow.
  <li> <strong> <a style="color:red;">Cluster 3</a></strong>, consists of Aberdeenshire, Angus, Argyll and Bute, Highland, Moray, Na h-Eileanan Siar, Orkney Islands, Perth and Kinross, Scottish Borders, Shetland Islands and Stirling.
  </li> 
  <li> <strong> <a style="color:green;">Cluster 4</a></strong>, consists of Clackmannanshire Dumfries and Galloway, East Ayrshire, East Lothian, Falkirk, Inverclyde, Midlothian, North Ayrshire, North Lanarkshire, Renfrewshire, South Ayrshire, South Lanarkshire, West Dunbartonshire and West Lothian. 
  </li>
</ul>

<p> To check what the different clusters are capturing, I have calculated the <strong><i> mean crime rates </i></strong> for each crime type in each cluster:
</p>

<iframe
src="https://nbviewer.org/github/MartaNabais/udacity_html_first_project/blob/main/cluster_means_2022-2023.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>

<p> We can clearly see, that Cluster 1 (East Dunbartonshire and East Renfrewshire) has <strong>lower</strong> mean crime rates compared to the other clusters, and we can observe the exact opposite for cluster number 2. 
</p>

<p> The separation between clusters is also visible if we plot crime rates for <i>"Common assault"</i> and <i>"Vandalism"</i>, for example. In this case, these two crime types seem to vary <i> linearly </i>,that is, a county with high vandalism rates will also likely have high common assault rates:
</p>

<iframe
src="https://nbviewer.org/github/MartaNabais/udacity_html_first_project/blob/main/vandalism_vs_assault_clusters_2022-2023.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>

<p>
Interestingly, this separation becomes murkier if we plot  crime rates for <i>"Common assault"</i> and <i>"Drugs Possession"</i>. In this case, the linearity of their relationship is not so clear. For example, if we hover over the Shetland Islands, we can see they show high rates for drug possession, but relatively lower rates for common assault:
</p>

<iframe
src="https://nbviewer.org/github/MartaNabais/udacity_html_first_project/blob/main/drugs_possession_vs_assault_clusters_2022-2023.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>

<p style="font-size:18px;color:grey;"> It makes me wonder...</p>
<p style="font-size:22px;color:grey;text-align:center;"> What is going in Shetland? </p>
<p>&nbsp;</p>

<hr>

<h2> Conclusions </h2>
<ol>
  <li> Overall crime rates seem to be going down in Scotland.  </li>
  <li> Some areas with lower crime rates have shown an increase in overall crime rates last year (e.g., Orkney, Shetlands and Outer-Hebrides).</li>
  <li> We can cluster Scottish counties into 4-different groups taking into account different crime type rates. From lower to higher mean crime rates: Cluster 1 < Cluster 3 < Cluster 4 < Cluster 2. </li>
</ol>

<h3> Limitations </h3>

<p> There are several limitations to these analyses, including:
 <ul>
  <li> The high-dimensionality of the data: As the number of dimensions increases, a distance-based similarity measure converges to a constant value between any given examples. I could've potentially addressed this by using a dimensionality reduction technique (such as principal component analysis). </li>
  <li> The random initialization of <i>k</i> being dependent on the initial values. </li>
  <li> Highly impacted by outliers. </li>
  <li> Always tried to find circular clusters. </li>
 </ul>
 </p>

<h3> Some possible follow-up questions </h3>
<ul>

  <li> Can we predict specific crime types for each county? </li>
  <li> Why aren't the isles clustered within cluster 1? </li>
  <li> Why do some counties show high crime rate levels of one type of crime, but not others (e.g., Shetlands have high drugs possession crime rates, but overall low crime)?</li>
  <li> Can we reduce dimensionality of data before clustering? </li>
  <li> Is there a better algorithm other than K-means to capture non-spherical clusters? </li>
  <li> Even though crime rates are calculated per capita, what is the effect of different population densities in each county? </li>

</ul>