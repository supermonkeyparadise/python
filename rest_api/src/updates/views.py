import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Update
# def detail_view(request):
#     return render(request, template, {}) # return JSON data
#     return HttpResponse(get_template().render({}))


def json_shortcutExample_view(request):
    data = {
        "count": 1001,
        "content": "Some new content"
    }

    return JsonResponse(data)


def json_example_view(request):
    '''
    GET -- Retrieve
    '''

    data = {
        "count": 3001,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
