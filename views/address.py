# -*- coding: utf-8 -*-
import urllib2
from django.http.response import Http404
from django.http import HttpResponse
import json

def get(request):
    if request.is_ajax():
        if request.method == 'POST':
            param = request.POST['input']
            param = param.encode('cp1251')
            param = urllib2.quote(param)
            req = "http://geocode-maps.yandex.ru/1.x/?format=json&geocode=%s"%param
            response = urllib2.urlopen(req)
            json_data = json.load(response)
            descs = json_data[u'response'][u'GeoObjectCollection'][u'featureMember']
            result_list = []
            for i in range(len(descs)):
                result_list.append(descs[i]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
            res = {"options": result_list}
            return HttpResponse(json.dumps(res), content_type="application/json")
    raise Http404