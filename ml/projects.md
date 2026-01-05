---
layout: page
title: ML Tasks
permalink: /ml/projects/
---

### Here I will add any ML tasks I work on to learn!


{% for project in site.projects_ml %}
- [{{ project.title }}]({{ project.url }})
{% endfor %}