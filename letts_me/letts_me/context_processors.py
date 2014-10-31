#!/usr/bin/env python

from django.conf import settings

def site_title(request):
    
    return {'site_title': settings.SITE_TITLE }

def social_media(request):

    media_types = str.upper("facebook github instagram twitter").split()

    request_context_dict = {}

    for media in media_types:
        const_val = getattr(settings, media+"_PROFILE")
        if const_val:
            request_context_dict[str.lower(media)] = const_val

    return request_context_dict
