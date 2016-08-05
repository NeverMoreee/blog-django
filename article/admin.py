from django.contrib import admin

# Register your models here.

from.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("art_title", "art_pub_date", "art_type")
    ordering = ("-art_pub_date",)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ("rp_pub_date", "article", "rp_title", "rp_content")
    ordering = ("-rp_pub_date",)


class DriftAdmin(admin.ModelAdmin):
    list_display = ("dr_title","dr_pub_date")
    ordering = ("-dr_pub_date",)



admin.site.register(Article, ArticleAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Drift, DriftAdmin)