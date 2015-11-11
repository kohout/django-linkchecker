# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import URLField
import logging

LINKCHECKER_DELETE_HISTORY_ON_UPDATE = getattr(settings, 'LINKCHECKER_DELETE_HISTORY_ON_UPDATE', False)
LINKCHECKER_LOGGER = getattr(settings, 'LINKCHECKER_LOGGER', logging.getLogger('link_checker'))
LINKCHECKERS = getattr(settings, 'LINKCHECKERS', list())
LINKCHECKER_FIELD_TYPES = getattr(settings, 'LINKCHECKER_FIELD_TYPES', [URLField])
LINKCHECKER_LINK_TO = getattr(settings, 'LINKCHECKER_LINK_TO', None)
LINKCHECKER_TIMEOUT = getattr(settings, 'LINKCHECKER_TIMEOUT', 3)
