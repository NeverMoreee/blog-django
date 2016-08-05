from django.contrib import admin

# Register your models here.

from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('ms_title', 'ms_pub_date', 'ms_content')
    ordering = ('-ms_pub_date',)


admin.site.register(Message, MessageAdmin)