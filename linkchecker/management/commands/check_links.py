# -*- coding: utf-8 -*-
import urllib2
from django.core.management.base import BaseCommand
from models import BrokenLink
from settings import LINKCHECKERS, LINKCHECKER_TIMEOUT, LINKCHECKER_LINK_TO, LINKCHECKER_LOGGER as logger


class LinkChecker(BaseCommand):
    def handle(self, *args, **options):
        for linkchecker in LINKCHECKERS:
            qs = linkchecker.queryset or linkchecker.model.objects.all()
            url_fields = [f for f in linkchecker.fields if f not in linkchecker.exclude]

            for obj in qs:
                urls = obj.values(*url_fields)
                for field_name, url in urls.items():
                    self.test_url(obj, field_name, url)

    def test_url(self, obj, field_name, url):
        if url is None or url.strip() == '':
            return

        request = urllib2.Request(url)
        try:
            urllib2.urlopen(request, timeout=LINKCHECKER_TIMEOUT)
        except urllib2.HTTPError, e:
            obj_name = obj._meta.verbose_name

            bl, created = BrokenLink.objects.get_or_create(
                entity=obj_name,
                field_name=field_name,
                url=url[:5000],
                status_code=e.code
            )
            if LINKCHECKER_LINK_TO:
                self.set_link_to(bl, obj)

        except Exception, e:
            logger.debug('Link %(url)s returned Error Code %(code)s: %(exception)s' %
                         {'url': url,
                          'code': e.code,
                          'exception': e})
            return

    def set_link_to(self, bl, obj):
        link_to = getattr(obj, LINKCHECKER_LINK_TO)
        if callable(link_to):
            bl.link_to = link_to()
        else:
            bl.link_to = link_to
        bl.save()

