# -*- coding: utf-8 -*-
import urllib2, socket
from django.core.management.base import BaseCommand
from linkchecker.models import BrokenLink
from linkchecker.utils import load
from linkchecker.settings import LINKCHECKERS, LINKCHECKER_TIMEOUT, LINKCHECKER_LINK_TO, LINKCHECKER_LOGGER as logger,\
    LINKCHECKER_IGNORE_TIMEOUT


class Command(BaseCommand):
    def handle(self, *args, **options):
        for linkchecker_string in LINKCHECKERS:
            linkchecker = load(linkchecker_string)
            qs = linkchecker.get_queryset() or linkchecker.get_model().objects.all()
            url_fields = [f for f in linkchecker.get_fields() if f not in linkchecker.get_excluded()]

            for current_obj, obj in enumerate(qs, start=1):
                logger.info('Object %(current)s of %(total)s' % {'current': current_obj, 'total': qs.count()})
                for current_field, field_name in enumerate(url_fields, start=1):
                    # logger.info('  Testing field %(current)s of %(total)s' % {'current': current_field,
                    #                                                           'total': len(url_fields)})
                    urls = self.get_urls(linkchecker, obj, field_name)
                    for current_url, url in enumerate(urls, start=1):
                        # logger.info('    Testing url %(current)s of %(total)s' % {'current': current_url,
                        #                                                           'total': len(urls)})
                        self.test_url(obj, field_name, url, linkchecker.get_object_url(obj, field_name))

    def get_urls(self, linkchecker, obj, field_name):
        urls = linkchecker.get_urls(obj, field_name)
        if not urls:
            urls = getattr(linkchecker, '%s_urls' % field_name, None)
            if not urls:
                urls = [getattr(obj, field_name, None)]
        return urls

    def test_url(self, obj, field_name, url, object_url=None):
        if url is None or url.strip() == '':
            return
        logger.info('    Testing url %(url)s' % {'url': url})
        request = urllib2.Request(url)
        try:
            urllib2.urlopen(request, timeout=LINKCHECKER_TIMEOUT)
        except urllib2.HTTPError, e:
            self.create_broken_link_entry(e, field_name, object_url, obj, url)
        except socket.timeout, e:
            if LINKCHECKER_IGNORE_TIMEOUT:
                logger.warning('Link %(url)s returned an Error: %(exception)s' %
                               {'url': url,
                                'exception': e})
            else:
                self.create_broken_link_entry(e, field_name, object_url, obj, url)
        except Exception, e:
            logger.warning('Link %(url)s returned an Error: %(exception)s' %
                           {'url': url,
                            'exception': e})
        return

    def create_broken_link_entry(self, e, field_name, object_url, obj, url):
        obj_name = obj._meta.verbose_name
        logger.warning('found broken url %s' % url)
        bl, created = BrokenLink.objects.get_or_create(
            entity=obj_name,
            field_name=field_name,
            url=url[:5000],
            status_code=e.code
        )
        if object_url:
            self.set_object_url(bl, obj, field_name, object_url)

    def set_object_url(self, bl, obj, field_name, object_url):
        if callable(object_url):
            bl.object_url = object_url(obj, field_name)
        else:
            bl.object_url = object_url
        bl.save()

