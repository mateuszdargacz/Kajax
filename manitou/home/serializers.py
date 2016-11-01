# -*- coding: utf-8 -*-
from home.models import Slider, SliderImage, CompanyData, Message, LifterImage, Lifter, LifterFeature
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


class LifterImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LifterImage


class LifterFeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = LifterFeature


class LifterSerializer(serializers.ModelSerializer):
    images = LifterImageSerializer(many=True)
    features = LifterFeatureSerializer(many=True)
    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = Lifter

    def get_primary_image(self, obj):
        if not obj or not obj.image:
            return None
        else:
            return self.context['request'].build_absolute_uri(obj.image)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
