# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from management.commands.check_links import LinkChecker
from models import BrokenLink
from generics.views import GenericTableMixin


class BrokenLinkListView(GenericTableMixin, ListView):
    model = BrokenLink
    selected = 'system'

    def get_menues(self):
        return []


class BrokenLinkDeleteView(DeleteView):
    model = BrokenLink


class LinkCheckView(View):
    def get(self, *args, **kwargs):
        LinkChecker.handle(*args, **kwargs)
