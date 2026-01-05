---
layout: page
title: ML Notes
permalink: /ml/notes/
---
Here I post notes on stuff I am learning for ML!

{% for note in site.notes_ml %}
- [{{ note.title }}]({{ note.url }})
{% endfor %}