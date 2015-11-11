# -*- coding: utf-8 -*-
from linkchecker.settings import LINKCHECKER_FIELD_TYPES, LINKCHECKER_LINK_TO


class BaseLinkChecker(object):
    model = NotImplementedError
    queryset = None

    fields = None
    excluded = []

    link_to = None

    def get_model(self):
        return self.model

    def get_queryset(self):
        return self.queryset

    def get_fields(self):
        if self.fields:
            return self.fields

        return [f for f in self.model._meta.get_all_field_names() if type(self.model._meta.get_field(f)) in LINKCHECKER_FIELD_TYPES]

    def get_excluded(self):
        return self.excluded

    def get_link(self):
        return self.link_to

    class Meta:
        abstract = True
