from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from article import models

admin.site.register(models.Article, MarkdownxModelAdmin)
admin.site.register(models.Tag)
