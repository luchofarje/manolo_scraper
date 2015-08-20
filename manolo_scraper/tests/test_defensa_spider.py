# -*- coding: utf-8 -*-
import os
import unittest

from manolo_scraper.spiders.defensa import DefensaSpider
from manolo_scraper.utils import make_hash
from utils import fake_response_from_file


class TestMineduSpider(unittest.TestCase):

    def setUp(self):
        self.spider = DefensaSpider()

    def test_parse_item(self):
        filename = os.path.join('data/defensa', '19-08-2015.html')
        items = self.spider.parse(fake_response_from_file(filename, meta={'date': u'19/08/2015'}))

        item = next(items)
        self.assertEqual(item.get('full_name'), u'AURELIO COREDOR MIRANO')
        self.assertEqual(item.get('time_start'), u'08:38')
        self.assertEqual(item.get('institution'), u'defensa')
        self.assertEqual(item.get('id_document'), u'DNI')
        self.assertEqual(item.get('id_number'), u'43447287')
        self.assertEqual(item.get('entity'), None)
        self.assertEqual(item.get('reason'), u'REUNIÓN DE TRABAJO')
        self.assertEqual(item.get('host_name'), u'HUGO DAVID MEJIA HUAMAN')
        self.assertEqual(item.get('time_end'), None)
        self.assertEqual(item.get('date'), u'2015-08-19')
        self.assertEqual(item.get('sha1'), u'd9f07e3a5effd7f0b9164dfc14822c5395ed3b58')

        item = next(items)
        self.assertEqual(item.get('full_name'), u'LUIS ANIBAL OLIVERA SANTA CRUZ')
        self.assertEqual(item.get('institution'), u'defensa')
        self.assertEqual(item.get('id_document'), u'DNI')
        self.assertEqual(item.get('id_number'), u'09392580')
        self.assertEqual(item.get('entity'), u'FAP')
        self.assertEqual(item.get('reason'), u'REUNIÓN DE TRABAJO')
        self.assertEqual(item.get('host_name'), u'JORGE RICARDO TORRES MONTEZA')
        self.assertEqual(item.get('time_start'), u'08:44')
        self.assertEqual(item.get('time_end'), u'11:49')
        self.assertEqual(item.get('date'), u'2015-08-19')
        self.assertEqual(item.get('sha1'), u'8d0e1ee7b60b8b2ee9e26d30e708d606a8d06a45')

        number_of_items = 1 + sum(1 for _ in items)
        self.assertEqual(number_of_items, 13)

    def test_correct_hash_sha1_for_legacy_data(self):
        item = {
            'date': '2013-10-24',
            'entity': u'',
            'full_name': u'JUAN PONCE VILLARROEL',
            'host_name': u'FERNANDO NOBLECILLA ZUÑIGA',
            'id_document': u'DNI',
            'id_number': u'08882615',
            'institution': u'defensa',
            'location': '',
            'meeting_place': '',
            'office': u'',
            'reason': u'VISITA PERSONAL',
            'time_start': u'17:28',
            'time_end': u'18:00',
            'title': u'',
        }
        result = make_hash(item)
        expected = 'dd3e23e4a1b146e250f759666bd0cfdcf0c3db8d'
        self.assertEqual(expected, result['sha1'])
