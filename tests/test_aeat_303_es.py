#!/usr/bin/env python
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends, doctest_dropdb


class Aeat303EsTestCase(unittest.TestCase):
    '''
    Test AEAT 303 ES module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('aeat_303_es')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            Aeat303EsTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_aeat303.rst',
            setUp=doctest_dropdb, tearDown=doctest_dropdb, encoding='utf-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
