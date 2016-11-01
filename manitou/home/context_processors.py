# -*- coding: utf-8 -*-
from home.models import CompanyData

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '6/11/16 / 1:08 PM'
__git__ = 'https://github.com/mateuszdargacz'


def company_data(request):
    """
    Returns a lazy 'messages' context variable.
    """
    return {
        'company_data': CompanyData.objects.first(),
    }
