from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.shares.validators import username_validator


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
    name = models.CharField(_('name'))

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class Comment(models.Model):
    article = models.ForeignKey('articles.Article', verbose_name=_('article'), on_delete=models.CASCADE)
    content = models.TextField(_('content'))
    content_editable = models.TextField(_('content for editor'), max_length=512)
    posted_at = models.DateTimeField(_('posted at'), auto_now_add=True)
    name = models.CharField(
        _('name'),
        max_length=32,
        validators=username_validator,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    )
    email = models.EmailField(_('email address'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def get_mask_email(self):
        user_part, domain_part = self.email.rsplit('@', 1)
        return '{first_letter}***{last_letter}@{domain}'.format(
            first_letter=user_part[0],
            last_letter=user_part[-1],
            domain=domain_part
        )
