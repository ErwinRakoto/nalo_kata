"""
nalo.ice_cream_app.views
"""


from rest_framework import decorators
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.mixins import ListModelMixin

from django.db import IntegrityError

from nalo.ice_cream_app.models import IceSerializer, IceBowlSerializer, IceBowl, Command, CommandSerializer

import logging
from datetime import datetime


class IceBowlViewSet(GenericViewSet,
                     ListModelMixin):
    """
    Ice cream view Set
    """
    serializer_class = IceSerializer

    def get_queryset(self):
        """
        Get initial queryset
        :return: PotGlace model
        """
        return IceBowl.objects.all()

    @decorators.action(methods=['GET'], detail=False)
    def list_bowl(self, req, *args, **kwargs):
        """
        GET method : [No arguments needed]
            Give list of all ice cream bowl
        :param req:
        :param args:
        :param kwargs:
        :return: PotGlaceSerializer
        """
        queryset = self.get_queryset()

        return Response(IceBowlSerializer(queryset, many=True).data, status=status.HTTP_200_OK)

    @decorators.action(methods=['GET'], detail=False)
    def list_command(self, req, *args, **kwargs):
        """
        GET method : [ arguments needed ]
            Give list of the requested command
        :param req:
        :param args: num_commande=int()
        :param kwargs:
        :return: CommandeSerializer
        """
        data = self.request.GET
        order_command = data.get('num_commande')

        if order_command:
            queryset = Command.objects.filter(order_command=order_command)
        else:
            # Dangerous, only for dev mod ..
            queryset = Command.objects.all()

        return Response(CommandSerializer(queryset, many=True).data, status=status.HTTP_200_OK)

    @decorators.action(methods=['GET'], detail=False)
    def ice_command(self, req, *args, **kwargs):
        """
        GET method : [2 arguments needed]
            Use API to make an ice cream command
        :param req:
        :param args: glace_id=id() ; nb_boule=int()
        :param kwargs:
        :return: dict(price, order_number)
        """

        data = self.request.GET

        glace_id = data.get('glace_id')
        number_ice_scoop = int(data.get('nb_boule'))

        if not glace_id or not number_ice_scoop:
            # TODO : Empty URL's to complete
            return Response('Veullez renseigner les params glace_id et nb_boule', status.HTTP_206_PARTIAL_CONTENT)

        queryset = self.get_queryset()
        queryset = queryset.filter(ice_id=glace_id)

        ## PAY METHOD
        try:
            queryset.update(scoop_number=queryset.last().scoop_number - number_ice_scoop)
        except IntegrityError as IEe:
            logging.info(IEe)
            return Response('Not enough ice cream, only : ' + str(queryset.last().scoop_number) + ' missed',
                            status=status.HTTP_206_PARTIAL_CONTENT)
        except AttributeError as AEe:
            logging.warning(AEe)
            return Response('Incorect Data requested', status=status.HTTP_404_NOT_FOUND)

        ## COMMAND METHOD
        actual_tms = int(datetime.timestamp(datetime.now()))
        new_command = Command(ice_id=glace_id, ask_scoop_number=number_ice_scoop, order_command=actual_tms)
        new_command.save()

        response = {'price': int(number_ice_scoop) * 2, 'order_number': actual_tms}

        return Response(response, status=status.HTTP_200_OK)
