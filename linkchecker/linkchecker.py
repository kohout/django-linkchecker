# -*- coding: utf-8 -*-
from .settings import LINKCHECKER_FIELD_TYPES, LINKCHECKER_LINK_TO


class BaseLinkChecker(object):
    model = NotImplementedError
    queryset = None

    fields = [f for f in model._meta.get_fields() if type(f) in LINKCHECKER_FIELD_TYPES]
    excluded = []

    link_to = LINKCHECKER_LINK_TO or getattr(model, 'get_edit_url', None)

    class Meta:
        abstract = True
