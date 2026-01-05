---
layout: page
title: QML Notes
permalink: /qml/notes/
---
Here I post notes on stuff I am learning for QML!

{% for note in site.notes_qml %}
[{{ note.title }}]({{ note.url }})
{% endfor %}