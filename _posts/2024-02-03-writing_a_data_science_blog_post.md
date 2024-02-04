---
layout: post
title: Crime Trends in Scotland
author: Marta Nabais
tags: Scotland Crime k-Means DataScience
---

<img src="https://ik.imagekit.io/panmac/tr:f-auto,w-740,pr-true//bcd02f72-b50c-0179-8b4b-5e44f5340bd4/7887d0f1-9ea1-46c9-bbf1-a23d6ec007da/ann-cleeves-shetland-series-2.jpg" width="1000" class="unconfined"/>

## Introduction

<p> This year, I have started working for the Scottish Government, within the AI & Data Science unit. I am therefore looking to enhance my skills as a Data Scientist, to aid in implementing solutions that could help government make the fastest, best, and fairest, of all possible decisions.
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
<p>The Scottish Government has made over 250 datasets from a range of producers publicly available at statistics.gov.scot. It is a great resource, and I have focused on the “Recorded Crimes and Offences” dataset.
</p>
<p>This dataset contains statistics on crimes and offences, including number of crimes/offences and crime/offence rates per 10,000 population recorded by Police Scotland from 1996/97 to 2022/23 and by Local Authority. I have decided to focus on three simple exploratory questions for my first project.
</p>

## Question 1: How have reported crime rates changed over time in Scotland?

<p> Before answering my first question, I have to let you know I have only focused on “Crimes” and not “Offences”. This is because there may be some statistical differences between these terms. “Crime” is generally used for the more serious criminal acts; the less serious termed “offences”, although the term “offence” may also be used in relation to serious breaches of criminal law.
</p>

<p>In the figure below, you can see how crime rates have evolved over the years, for different counties in Scotland (you can hover over the lines to check for specific values): </p>

<iframe
  src="https://nbviewer.org/github/MartaNabais/html_attempt/blob/main/scottish_crime_ratios_over_time.html"
  style="height:400px; width: 100%;" frameborder="0" title="Fig.1 — Scottish crime rates over time.">
</iframe>

<p> If we focus on the year 1996/1997 (left-most side of the figure), there are a couple of counties that stand out for having a lot more reported crimes than the rest. Here’s the <strong>top-three</strong>: 
</p>

<ul>
    <li><strong>Glasgow</strong> is first (with a staggering 1647 crimes reported for every 10,000 people counted) 🥇</li>
    <li><strong>Dundee</strong> comes in a close second 🥈</li>
    <li><strong>Aberdeen</strong> comes in third 🥉</li>
</ul>


<p>Although I am not sure this is a race you would really want to win…</p>

<p>The <strong>bottom-three</strong> are all Scottish isles: <strong>Orkney, Shetland</strong> and <strong>Na h-Eileanan an Iar</strong> (the Outer Hebrides). In conclusion, if I were more risk-averse and had to decide where I would relocate within Scotland, I would be tempted to embrace the island lifestyle!
</p>

<p> Nonetheless, if we follow the lines from the past to the end of 2022 (or left to right), we can see the <i>trend</i> across all counties looks good: crime rates seem to be going down in Scotland!</p>

## Question 2: In the past year, which countries show the highest increase and decrease in overall crime rates?

<p>Although there seem to be higher crime rates in the mainland compared to the isles, it may also be interesting to look how rates have been <i>changing</i> within each county. To help us answer this question, we can take the <i>percentage change</i> between crime rates for the most recent and past years.
</p>

<p>In the bar graph below, I have calculated the percentage change in crime rates for each county, between the years 2022 (latest data provided) and 2021. Positive numbers imply there has been a <strong><i>X% increase</i></strong> and negative numbers imply there has been a <strong><i>X% decrease</i></strong>:
</p>

<iframe
src="https://nbviewer.org/github/MartaNabais/html_attempt/blob/main/percent_change_crimes.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>


<p> The three counties showing highest increase in crime rates in the past years are the three isles: Shetlands (40%), Orkney (39%) and Na h-Eileanan an Iar (33%). This would’ve been hard to conclude just by visually inspecting Fig.1!
</p>

<p>However, it is important to note this is a cross-sectional comparison, meaning it is only a snapshot of a point in time. Just because crime rates increased in the isles, does not mean they are expected to keep increasing over time.</p>

## Question 3: Which Scottish counties have more similar crime patterns?

<p> Looking at overall crime rates gives us a broad perspective of crime trends in Scotland. However, I would also like to understand if we can find <i>similarity patterns</i> between counties, by making use of information for <i>different crime types</i>.
</p>

<p> Fortunately, our dataset contains such information. Indeed, if we take a look at the distributions of different crime type rates for some counties for last year: 
</p>

<iframe
src="https://nbviewer.org/github/MartaNabais/html_attempt/blob/main/different_crime_types_2022-2023.html"
style="height:400px; width: 100%;" frameborder="0">
</iframe>

<p>
If we look at the <strong><i>proportion</i></strong> of different crime types between each county, we can see that some counties seem to have more similar distributions than other. For example, Glasgow City seems to have similar distribution to Aberdeen City. So do Falkirk and Inverclyde. And East Dunbartonshire and East Renfrewshire. And finally, so do the Isles!
</p>