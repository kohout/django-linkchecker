# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from management.commands.check_links import Command as LinkChecker
from models import BrokenLink
from generics.views import GenericTableMixin


class LinkCheckView(View):
    def get(self, *args, **kwargs):
        LinkChecker.handle(*args, **kwargs)
