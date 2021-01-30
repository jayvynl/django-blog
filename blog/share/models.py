from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

from share.cached import set_site_information


class SiteInformation(models.Model):
    name = models.CharField(_('name'), max_length=16, default=_('My site'))
    register = models.CharField(_('register'), max_length=16, blank=True, default=_('Not registered'))
    register_url = models.URLField(_('register url'), blank=True, default='#')

    class Meta:
        verbose_name = _('site information')


def update_site_info(sender, instance, *args, **kwargs):
    site_info = {
        'site_name': instance.name,
        'site_register': instance.register,
        'site_register_url': instance.register_url
    }
    set_site_information(**site_info)


post_save.connect(update_site_info, sender=SiteInformation, dispatch_uid='update_site_info')
