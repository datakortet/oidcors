# -*- coding: utf-8 -*-
from django import http, template, shortcuts as dj


def home(request):
    return dj.render_to_response('home.html', template.Context({
        'name': 'world'
    }))
