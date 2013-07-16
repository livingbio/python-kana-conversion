# -*- coding: utf-8 -*-

from unittest import TestCase
from kana_conversion import KanaConversion


class TestKanaConversion(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.converter = KanaConversion()

    def test_hiragana_to_katakana(self):
        test_text = u'いあん'
        expected  = u'イアン'
        response  = self.converter.hiragana_to_katakana(test_text)
        self.assertEquals(expected, response, response)

    def test_katakana_to_hiragana(self):
        test_text = u'イアン'
        expected  = u'いあん'
        response  = self.converter.katakana_to_hiragana(test_text)
        self.assertEquals(expected, response, response)

    def test_romaji_to_katakana(self):
        test_text = u'ian'
        expected  = u'イアン'
        response  = self.converter.romaji_to_katakana(test_text)
        self.assertEquals(expected, response, response)

    def test_romaji_to_zenkaku(self):
        test_text = (u'ian', u'IAN')
        expected  = (u'ｉａｎ', u'ＩＡＮ')

        for index, text in enumerate(test_text):
            response  = self.converter.romaji_to_zenkaku(text)
            self.assertEquals(expected[index], response, response)

    def test_romaji_to_hiragana(self):
        test_text = u'ian'
        expected  = u'いあん'
        response  = self.converter.romaji_to_hiragana(test_text)
        self.assertEquals(expected, response, response)

    def test_katakana_to_romaji(self):
        test_text = u'イアン'
        expected  = u'ian'
        response  = self.converter.katakana_to_romaji(test_text)
        self.assertEquals(expected, response, response)

    def test_hiragana_to_romaji(self):
        test_text = u'いあん'
        expected  = u'ian'
        response  = self.converter.hiragana_to_romaji(test_text)
        self.assertEquals(expected, response, response)

    def test_build_conversion_pattern(self):
        test_text = u'hello'
        expected  = u'hello'
        response  = self.converter._post_process_romaji_text(test_text)
        self.assertEquals(expected, response, response)

    def test_build_conversion_dictionary(self):
        test_text = u'hello'
        expected  = u'hello'
        response  = self.converter._post_process_romaji_text(test_text)
        self.assertEquals(expected, response, response)

    def test_convert_text(self):
        test_text = u'hello'
        expected  = u'hello'
        response  = self.converter._post_process_romaji_text(test_text)
        self.assertEquals(expected, response, response)

    def test_pre_process_romaji(self):
        test_text = u'hello'
        expected  = u'hello'
        response  = self.converter._post_process_romaji_text(test_text)
        self.assertEquals(expected, response, response)

    def test_post_process_romaji_text(self):
        test_text = u'hello'
        expected  = u'hello'
        response  = self.converter._post_process_romaji_text(test_text)
        self.assertEquals(expected, response, response)