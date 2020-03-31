#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from django.test import TestCase

from nalo.ice_cream_app.models import Command

from datetime import datetime
from django.test import Client


class AddTestCase(TestCase):
    """
    Class test for ice_cream_app
    """

    def test_make_command(self):
        """
        Test function
        :return:
        """
        c = Client()

        ## Command stock respect
        response_partial = c.get('/api/v1/icebowl/ice_command/?glace_id=2&nb_boule=100')
        self.assertEqual(response_partial.status_code, 404)

        c.get('/cron/cron/init-ice_bowl/')
        response = c.get('/api/v1/icebowl/ice_command/?glace_id=2&nb_boule=10')
        self.assertEqual(response.status_code, 200)

        ## Command Response
        actual_tms = int(datetime.timestamp(datetime.now()))
        content = response.content
        self.assertEqual(eval(content.decode("utf-8")), {'price': 20, 'order_number': actual_tms})

        ## Command list created
        list_commande_response = c.get('/api/v1/icebowl/list_command/?num_commande={}'.format(actual_tms))
        self.assertEqual(list_commande_response.status_code, 200)

        ## Command exist
        command_object = Command.objects.filter(order_command=actual_tms)
        self.assertTrue(command_object)

    def test_reload_bowl(self):
        # TODO : when function ..
        pass


if __name__ == '__main__':
    unittest.main()

