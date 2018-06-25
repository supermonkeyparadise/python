import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from restapi.mixins import JsonResponseMixin

from .models import Update
# def detail_view(request):
#     return render(request, template, {}) # return JSON data
#     return HttpResponse(get_template().render({}))

# level 1


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

# level 2


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 3003,
            "content": "Some new content"
        }

        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

# level 3


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 3002,
            "content": "Some new content"
        }

        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj], fields=('user', 'content'))
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }

        # json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }

        # json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')
