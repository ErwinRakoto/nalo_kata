#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CRON TEST
"""

import unittest

from django.test import TestCase, Client

from nalo.ice_cream_app.models import Ice, IceBowl


class AddTestCase(TestCase):
    """
    Test method for all crons
    """

    def test_call_cron_url(self):
        """
        Call init
        :return: True/False
        """
        c = Client()

        response = c.get('/cron/cron/init-ice_bowl/')
        self.assertEqual(response.status_code, 200)

        # Do create
        glace = Ice.objects.all().filter(savour='Chocolat Orange')
        parfum_A = glace.last().savour
        self.assertEqual(parfum_A, 'Chocolat Orange')

        # Do not duplicate Create
        response = c.get('/cron/cron/init-ice_bowl/')
        response = c.get('/cron/cron/init-ice_bowl/')
        count_a = glace.count()
        count_b = IceBowl.objects.filter(ice__savour='Chocolat Orange').count()
        self.assertEqual(count_a, 1)
        self.assertEqual(count_b, 1)

        # Identical Id
        self.assertEqual(glace.last().id, Ice.objects.all().filter(savour='Chocolat Orange').last().id)


if __name__ == '__main__':
    unittest.main()
