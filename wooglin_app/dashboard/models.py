from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here


class Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    legal_name = models.CharField(max_length=127)
    phone = models.CharField(max_length=15, default="000.000.0000")
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=80)
    rollnumber = models.IntegerField()
    member_score = models.IntegerField()
    inactive_flag = models.BooleanField()
    abroad_flag = models.BooleanField()
    present = models.IntegerField()
    position = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='static/UserMedia/', default='/static/images/default.jpg')

    def __str__(self):
        return self.name


class SoberBros(models.Model):
    date = models.DateField(null=False)
    start_time = models.TimeField(blank=True, default='08:00:00')
    end_time = models.TimeField(blank=True, default='23:59:59')
    sb_1 = models.ForeignKey(Members, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='sb_1')
    sb_2 = models.ForeignKey(Members, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='sb_2')
    sb_3 = models.ForeignKey(Members, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='sb_3')
    sb_4 = models.ForeignKey(Members, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='sb_4')
    sb_5 = models.ForeignKey(Members, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='sb_5')

    def __str__(self):
        return self.date


class SoberBroSheets(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    open_to_chapter_date = models.DateField(null=False)
    open_to_chapter_time = models.TimeField()
    lock_sheet = models.DateTimeField(null=False)
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=1023)

    def __str__(self):
        return self.name