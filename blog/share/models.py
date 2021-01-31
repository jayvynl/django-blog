from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from share.cached import set_site_information


class SiteInformation(models.Model):
    name = models.CharField(_('name'), max_length=16, default=_('My site'))
    register = models.CharField(_('register'), max_length=16, blank=True, default=_('Not registered'))
    register_url = models.URLField(_('register url'), blank=True, default='#')

    class Meta:
        verbose_name = _('site information')


class PersonalInfo(models.Model):
    content = MarkdownxField(_('markdown content'), max_length=1024)
    content_html = models.TextField(_('html content'))

    def save(self, *args, **kwargs):
        self.content_html = f'<div class="markdownx-preview">{markdownify(self.content)}</div>'
        super(PersonalInfo, self).save(*args, **kwargs)


def update_site_info(sender, instance, *args, **kwargs):
    site_info = {
        'site_name': instance.name,
        'site_register': instance.register,
        'site_register_url': instance.register_url
    }
    set_site_information(**site_info)


post_save.connect(update_site_info, sender=SiteInformation, dispatch_uid='update_site_info')
