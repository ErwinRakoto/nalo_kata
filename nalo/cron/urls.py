"""
Url list
"""
from django.conf.urls import url

from nalo.cron.init_glace import (
    CronInitIce
)


urlpatterns = [
    url(r'^cron/init-ice_bowl/', CronInitIce.as_view()),
]
