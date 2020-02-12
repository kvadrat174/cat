
from cats.serializers import CategorySerializer
from cats.models import Category

from django.http import HttpResponse
from rest_framework import viewsets, mixins

import json

class CategoryViewSet(mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """ get n post"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request):

        try:
            jdata = json.loads(request.body)
        except json.decoder.JSONDecodeError as e:
            return HttpResponse('Wrong data: %s' % e)

        def parse(el, parent=None):

            name = el.get('name')
            if not name:
                return

            category, _ = Category.objects.get_or_create(name=name, parent=parent)

            for children in el.get('children', []):
                parse(children, parent=category)

        parse(jdata)

        return HttpResponse('Data uploaded')