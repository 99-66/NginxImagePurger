from django.db import models


class PurgeLog(models.Model):
    user = models.ForeignKey('auth.User', on_delete=True)
    requrl = models.URLField()
    originurl = models.URLField()
    result_text = models.CharField(max_length=1024, null=False, blank=False)
    result_code = models.CharField(max_length=8, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return str(self.originurl)


class ServerList(models.Model):
    server = models.GenericIPAddressField()
    status = models.BooleanField(default=False)
    rank = models.PositiveSmallIntegerField(default=1)
    description = models.CharField(max_length=1024, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return str(self.server)