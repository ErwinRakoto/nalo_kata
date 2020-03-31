# -*- coding: utf-8 -*-
"""
Insert tables Init
"""

from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from nalo.ice_cream_app.init_value_list import parfum_list
from nalo.ice_cream_app.models import Ice, IceBowl

import logging


class CronInitIce(APIView):
    """
    First init of ice cream
    Load Ice model ; IceBowl model
    """

    # No secure cron
    # TODO : Make unreacheble URL, Only system can use it

    def get(self, request):
        """
            GET METHOD to lunch init.py
        """

        for i in parfum_list:
            try:
                new_value = Ice.objects.get_or_create(savour=i)
                new_value2 = IceBowl.objects.update_or_create(ice=new_value[0], defaults={'scoop_number': 40})
            except Exception as e:
                # Amelioration possible, érreurs à traiter, redirgier etc.
                logging.error(e)
                raise Response(status=status.HTTP_400_BAD_REQUEST)
            # finally : empty DB ? dépend du besoin ..

        return Response(status=status.HTTP_200_OK)
