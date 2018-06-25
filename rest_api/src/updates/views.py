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
        # [ basic ]
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }
        # json_data = json.dumps(data)

        # [solution 1]
        # obj = Update.objects.get(id=1)
        # data = serialize("json", [obj], fields=('user', 'content'))
        # json_data = data

        # [solution 2]
        obj = Update.objects.get(id=2)
        json_data = obj.serialize()
        
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        # [ basic ]
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }
        # json_data = json.dumps(data)

        # [solution 1]
        # qs = Update.objects.all()
        # data = serialize("json", qs, fields=('user', 'content'))
        # json_data = data

        # [solution 2]
        json_data = Update.objects.all().serialize()
        
        return HttpResponse(json_data, content_type='application/json')
