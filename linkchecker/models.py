# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext as _


class BrokenLink(models.Model):
    entity = models.CharField(max_length=255,
        blank=True, default=u'',
        verbose_name=_(u'Entity'))
    field_name = models.CharField(max_length=200,
        blank=True, default=u'',
        verbose_name=_(u'Field'))
    last_checked = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'last_checked'))
    url = models.URLField(
        max_length=5000,
        verbose_name=_(u'Broken link'))
    status_code = models.PositiveSmallIntegerField(
        blank=True, null=True,
        verbose_name=_(u'Status code'))
    object_url = models.URLField(
        blank=True, null=True,
        verbose_name=_(u'Go to Object'))

    def row_buttons(self):
        buttons = [
            {'url': reverse_lazy('linkchecker-delete', kwargs={
                'pk': self.id}),
             'css': 'btn-danger',
             'icon': 'glyphicon glyphicon-remove',
             'label': 'Delete Broken Link Entry',
             }
        ]
        return buttons

    def __unicode__(self):
        return 'Broken link: %s' % self.url

    class Meta:
        ordering = ('-last_checked', )
        verbose_name = _(u'Broken link')
        verbose_name_plural = _(u'Broken links')
