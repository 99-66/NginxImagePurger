from django.contrib import admin
from .models import PurgeLog, ServerList


@admin.register(PurgeLog)
class AdminPurgeLog(admin.ModelAdmin):
    list_display = ['requrl', 'originurl', 'result_code', 'result_text', 'user']
    list_filter = ['originurl', 'result_code']


@admin.register(ServerList)
class AdminServerList(admin.ModelAdmin):
    list_display = ['server', 'status', 'rank']
    list_filter = ['status']
