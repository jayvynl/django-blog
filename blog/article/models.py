from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(_('title'), max_length=32)
    posted_at = models.DateTimeField(_('posted at'), auto_now_add=True)
    edited_at = models.DateTimeField(_('edited at'), auto_now=True)
    tags = models.ManyToManyField('articles.Tag', verbose_name=_('tags'), related_name='articles')
    content = models.TextField(_('content'))
    content_editable = models.TextField(_('content for editor'), max_length=8192)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ('-id',)


class Tag(models.Model):
    name = models.CharField(
        _('name'),
        unique=True,
        error_messages={
            'unique': _("A tag with that name already exists."),
        },
    )

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
