# -*- coding: utf-8 -*-
import urllib2
from django.core.management.base import BaseCommand
from linkchecker.models import BrokenLink
from linkchecker.utils import load
from linkchecker.settings import LINKCHECKERS, LINKCHECKER_TIMEOUT, LINKCHECKER_LINK_TO, LINKCHECKER_LOGGER as logger


class Command(BaseCommand):
    def handle(self, *args, **options):
        for linkchecker_string in LINKCHECKERS:
            linkchecker = load(linkchecker_string)
            qs = linkchecker.get_queryset() or linkchecker.get_model().objects.all()
            url_fields = [f for f in linkchecker.get_fields() if f not in linkchecker.get_excluded()]

            for current, obj in enumerate(qs, start=1):
                for field_name in url_fields:
                    url = getattr(obj, field_name, None)
                    print 'Testing link %(current)s of %(total)s' % {'current': current, 'total': qs.count()}
                    self.test_url(obj, field_name, url, linkchecker.get_link())

    def test_url(self, obj, field_name, url, link_to=None):
        if url is None or url.strip() == '':
            return

        request = urllib2.Request(url)
        try:
            urllib2.urlopen(request, timeout=LINKCHECKER_TIMEOUT)
        except urllib2.HTTPError, e:
            obj_name = obj._meta.verbose_name
            print 'found broken link %s' % url
            bl, created = BrokenLink.objects.get_or_create(
                entity=obj_name,
                field_name=field_name,
                url=url[:5000],
                status_code=e.code
            )
            if link_to:
                self.set_link_to(bl, obj, link_to)

        except Exception, e:
            print('Link %(url)s returned an Error: %(exception)s' %
                         {'url': url,
                          'exception': e})
        return

    def set_link_to(self, bl, obj, link_to):
        if callable(link_to):
            bl.link_to = link_to()
        else:
            bl.link_to = link_to
        bl.save()

