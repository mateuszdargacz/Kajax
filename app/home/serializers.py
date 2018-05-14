# -*- coding: utf-8 -*-
from home.models import Slider, SliderImage, CompanyData, Service, Client, ProjectImage, Project, Message
from rest_framework import serializers

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '6/11/16 / 12:47 PM'
__git__ = 'https://github.com/mateuszdargacz'


class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyData


class SliderImageSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        return ''.join(obj.tags.split(' ')).split(',')

    class Meta:
        model = SliderImage


class SliderSerializer(serializers.ModelSerializer):
    images = SliderImageSerializer(many=True)

    class Meta:
        model = Slider


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True)
    image = serializers.SerializerMethodField()
    detail_url = serializers.SerializerMethodField()

    def get_image(self, obj):
        project_image = obj.images.filter(primary=True).first()
        return ProjectImageSerializer(instance=project_image).data

    def get_detail_url(self, obj):
        return 'http://google.pl'

    class Meta:
        model = Project


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
