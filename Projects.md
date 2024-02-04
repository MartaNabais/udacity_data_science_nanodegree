---
layout: page
title: "Projects"
permalink: /projects
---


# Udacity Data Science Nanodegree Projects
## First Project
<ul>
    {% for post in site.posts %}
        {% if post.title == "Crime Trends in Scotland" %}
        <button class="button button1">  <a href="{{ post.url }}">  Writing a Data Science Blog Post </a>
        </button>
        
        {% endif %}

    {% endfor %}
</ul>

--- 
## Second Project
<ul>
    <button class="button button2">   In Progress...</button>
</ul>