from django.contrib import admin
from .models import Message


admin.site.site_header  = "Sofivite Administration"
admin.site.site_title   = "Sofivite Administration"
@admin.register(Message)
class MessagesAdmin(admin.ModelAdmin):
    list_display=["name", "phone","subject", "email", "message" ]