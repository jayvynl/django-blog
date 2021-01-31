from django.db import models
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Article(models.Model):
    title = models.CharField(_('title'), max_length=32)
    posted_at = models.DateTimeField(_('posted at'), auto_now_add=True)
    edited_at = models.DateTimeField(_('edited at'), auto_now=True)
    tags = models.ManyToManyField('article.Tag', verbose_name=_('tags'), related_name='articles')
    content = MarkdownxField(_('markdown content'), max_length=8192)
    content_html = models.TextField(_('html content'), blank=True)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        self.content_html = f'<div class="markdownx-preview">{markdownify(self.content)}</div>'
        super(Article, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(
        _('name'),
        max_length=32,
        unique=True,
        error_messages={
            'unique': _("A tag with that name already exists."),
        },
    )

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
