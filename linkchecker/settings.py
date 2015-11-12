# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import URLField
import logging


def get_default_logger():
    logger = logging.getLogger('link_checker')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

LINKCHECKER_DELETE_HISTORY_ON_UPDATE = getattr(settings, 'LINKCHECKER_DELETE_HISTORY_ON_UPDATE', False)
LINKCHECKER_LOGGER = getattr(settings, 'LINKCHECKER_LOGGER', get_default_logger())
LINKCHECKERS = getattr(settings, 'LINKCHECKERS', list())
LINKCHECKER_FIELD_TYPES = getattr(settings, 'LINKCHECKER_FIELD_TYPES', [URLField])
LINKCHECKER_LINK_TO = getattr(settings, 'LINKCHECKER_LINK_TO', None)
LINKCHECKER_TIMEOUT = getattr(settings, 'LINKCHECKER_TIMEOUT', 3)
LINKCHECKER_IGNORE_TIMEOUT = getattr(settings, 'LINKCHECKER_IGNORE_TIMEOUT', False)
