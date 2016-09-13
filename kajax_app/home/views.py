#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from home.serializers import SliderSerializer, CompanyDataSerializer, ServiceSerializer, ClientSerializer, \
    ProjectSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)


class CompanyDataAPIView(ListAPIView):
    """
    Slider list (available to participation).
    """
    serializer_class = CompanyDataSerializer
    queryset = serializer_class.Meta.model.objects.all()


class SliderListAPIView(ListAPIView):
    """
    Slider list (available to participation).
    """
    serializer_class = SliderSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ServiceAPIView(ListAPIView):
    """
    Service list (available to participation).
    """
    serializer_class = ServiceSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ClientAPIView(ListAPIView):
    """
     Client list (available to participation).
    """
    serializer_class = ClientSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ProjectAPIView(ListAPIView):
    """
     Projects list (available to participation).
    """
    serializer_class = ProjectSerializer
    queryset = serializer_class.Meta.model.objects.all()

class MessageView(APIView):

    def post(self):
        pass