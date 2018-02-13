# -*- coding: utf-8 -*-
import json

from django import http, template, shortcuts as dj


def home(request):
    return dj.render_to_response('home.html', template.Context({
        'name': 'world'
    }))


def djson(request):
    print request
    if request.is_ajax() or 1:
        r = http.HttpResponse(
            json.dumps({'name': 'world'}, indent=4),
            content_type='application/json'
        )
        r['Access-Control-Allow-Origin'] = request.META['HTTP_ORIGIN']
        print 'returning:'
        print r
        return r
    return http.HttpResponse("This url must be requested with ajax..")
