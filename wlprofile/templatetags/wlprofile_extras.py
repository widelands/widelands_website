#!/usr/bin/env python -tt
# encoding: utf-8
#
# File: wlprofile/templatetags/wlprofile.py
#
# Created by Holger Rapp on 2009-03-15.
# Copyright (c) 2009 HolgerRapp@gmx.net. All rights reserved.
#
# Last Modified: $Date$
#

from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

register = template.Library()


@register.filter
def user_link(user):
    print('isinstance', user, isinstance(user, User))
    if user.email == 'deleted@wl.org':
        return 'User deleted'
    else:
        data = u'<a href="%s">%s</a>' % (
            reverse('profile_view', args=[user.username]), user.username)
    return mark_safe(data)
