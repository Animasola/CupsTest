#-*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to
from annoying.functions import get_object_or_None
from my_info.models import Contact


@login_required
@render_to('my_info/home.html')
def info_page(request):
    my_contacts = get_object_or_None(Contact, pk=1)
    return {'contacts': my_contacts}
