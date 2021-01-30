from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save


class SiteInformation(models.Model):
    name = models.CharField(_('name'), max_length=16, default=_('My site'))
    register = models.CharField(_('register'), max_length=16, blank=True, default=_('Not registered'))
    register_url = models.URLField(_('register url'), blank=True, default='#')

    class Meta:
        verbose_name = _('site information')


post_save()