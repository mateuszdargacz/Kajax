#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from home.forms import MessageForm
from home.serializers import SliderSerializer, CompanyDataSerializer, LifterSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
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


class LifterAPIView(ListAPIView):
    """
     Lifter list (available to participation).
    """
    serializer_class = LifterSerializer
    queryset = serializer_class.Meta.model.objects.all()


class MessageView(APIView):
    def post(self, *args, **kwargs):
        form = MessageForm(self.request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return Response(status=200)
        else:
            return Response(form.errors, status=400)
