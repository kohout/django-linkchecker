# -*- coding: utf-8 -*-
import django_tables2 as tables
from django.utils.translation import ugettext_lazy as _


class BrokenLinkTable(tables.Table):
    last_checked = tables.Column(verbose_name=_(u'Request date'))
    entity = tables.Column(verbose_name=_(u'Entity'))
    field_name = tables.Column(verbose_name=_(u'Field'))
    url = tables.TemplateColumn(verbose_name=_(u'Broken link'),
        template_name='linkchecker/cell_url.html')
    status_code = tables.Column(verbose_name=_(u'Status'))
    object_url = tables.TemplateColumn(verbose_name=_(u' '),
        template_name='linkchecker/row_buttons.html',
        orderable=False)

    class Meta:
        sequence = (
            'last_checked',
            'entity',
            'field_name',
            'url',
            'status_code',
            'object_url'
        )
        attrs = {"class": "table table-condensed table-hover"}
