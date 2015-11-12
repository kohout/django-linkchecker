# -*- coding: utf-8 -*-
from linkchecker.settings import LINKCHECKER_FIELD_TYPES, LINKCHECKER_LINK_TO


class BaseLinkChecker(object):
    model = NotImplementedError
    queryset = None

    fields = None
    excluded = []

    object_url = None

    def get_model(self, **kwargs):
        return self.model

    def get_queryset(self, **kwargs):
        return self.queryset

    def get_fields(self, **kwargs):
        if self.fields:
            return self.fields

        return [f for f in self.model._meta.get_all_field_names() if type(self.model._meta.get_field(f)) in LINKCHECKER_FIELD_TYPES]

    def get_excluded(self, **kwargs):
        return self.excluded

    def get_object_url(self, obj, field_name, **kwargs):
        return self.object_url

    def get_urls(self, obj, field_name, **kwargs):
        return None

    class Meta:
        abstract = True
