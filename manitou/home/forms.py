# -*- coding: utf-8 -*-
from django import forms
from home.models import Message

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '9/13/16 / 7:56 PM'
__git__ = 'https://github.com/mateuszdargacz'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = []

