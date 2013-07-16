# -*- coding: utf-8 -*-

import re
import conversion_models


class KanaConversion(object):

    def __init__(self):
        """
        Init dictionaries, regexs
        """
        # Build romaji dictionaries and keys
        self.romaji_dict, romaji_keys = self._build_conversion_dictionary(
            conversion_models.romaji, conversion_models.romaji_asist, False)

        # Build katakana / hiragana dictionaries and keys
        self.kana_dict, kana_keys = self._build_conversion_dictionary(
            conversion_models.romaji, conversion_models.kana_asist, True)

        # Build zenkaku dictionaries and keys
        self.zenkaku_dict, zenkaku_keys = self._build_conversion_dictionary(
            conversion_models.zenkaku, conversion_models.zenkaku_assist, False)

        hiragana_to_katakana_pattern = self._build_conversion_pattern(conversion_models.JOIN_CHAR, conversion_models.hiragana)
        katakana_to_hiragana_pattern = self._build_conversion_pattern(conversion_models.JOIN_CHAR, conversion_models.katakana)
        romaji_to_katakana_pattern   = self._build_conversion_pattern(conversion_models.JOIN_CHAR, romaji_keys)
        romaji_to_zenkaku_pattern    = self._build_conversion_pattern(conversion_models.JOIN_CHAR, zenkaku_keys)
        katakana_to_romaji_pattern   = self._build_conversion_pattern(conversion_models.JOIN_CHAR, kana_keys)

        # Precompile regexes
        self.re_hiragana_to_katakana = re.compile(hiragana_to_katakana_pattern)
        self.re_katakana_to_hiragana = re.compile(katakana_to_hiragana_pattern)
        self.re_romaji_to_katakana   = re.compile(romaji_to_katakana_pattern)
        self.re_romaji_to_zenkaku    = re.compile(romaji_to_zenkaku_pattern)
        self.re_katakana_to_romaji   = re.compile(katakana_to_romaji_pattern)

        self.re_xu  = re.compile(conversion_models.XU__PATTERN)
        self.re_ltu = re.compile(conversion_models.LTU_PATTERN)
        self.re_er  = re.compile(conversion_models.ER__PATTERN)
        self.re_n   = re.compile(conversion_models.N___PATTERN)
        self.re_oo  = re.compile(conversion_models.OO__PATTERN)
        self.re_mba = re.compile(conversion_models.MBA_PATTERN)
        self.re_xtu = re.compile(conversion_models.XTU_PATTERN)
        self.re_a__ = re.compile(conversion_models.A___PATTERN)

    def hiragana_to_katakana(self, text):
        """
        Example conversion -> いあん　ー＞　イアン
        :param text:
        :return: unicode string
        """
        conversion = self._convert_text(self.re_hiragana_to_katakana, conversion_models.hiragana, text)
        return conversion

    def katakana_to_hiragana(self, text):
        """
        Example conversion -> イアン　ー＞　いあん
        :param text:
        :return: unicode string
        """
        conversion = self._convert_text(self.re_katakana_to_hiragana, conversion_models.katakana, text)
        return conversion

    def romaji_to_katakana(self, text):
        """
        Example conversion -> ian　ー＞　イアン
        :param text:
        :return: unicode string
        """
        pre_processed_text = self._pre_process_romaji(text)
        conversion = self._convert_text(self.re_romaji_to_katakana, self.romaji_dict, pre_processed_text)

        return conversion

    def romaji_to_hiragana(self, text):
        """
        Example conversion -> ian　ー＞　いあん
        :param text:
        :return: unicode string
        """
        conversion = self.romaji_to_katakana(text)
        conversion = self.katakana_to_hiragana(conversion)

        return conversion

    def romaji_to_zenkaku(self, text):
        """
        Example conversion -> ian　ー＞　ｉａｎ
        :param text:
        :return: unicode string
        """
        conversion = self._convert_text(self.re_romaji_to_zenkaku, self.zenkaku_dict, text)
        return conversion

    def katakana_to_romaji(self, text):
        """
        Example conversion -> イアン　ー＞　ian
        :param text:
        :return: unicode string
        """
        conversion = self._convert_text(self.re_katakana_to_romaji, self.kana_dict, text)
        post_processed_text = self._post_process_romaji_text(conversion)

        return post_processed_text

    def hiragana_to_romaji(self, text):
        """
        Example conversion -> いあん　ー＞　ian
        :param text:
        :return: unicode string
        """
        conversion = self.hiragana_to_katakana(text)
        conversion = self.katakana_to_romaji(conversion)

        return conversion

    def _build_conversion_pattern(self, word_separator, word_list):
        """
        Create a regex pattern of the given word dict
        :param word_separator: word separator
        :param word_list: words to concatenate
        :return:
        """
        mapped_words = [re.escape(word) for word in word_list]
        pattern = word_separator.join(mapped_words)

        return pattern

    def _build_conversion_dictionary(self, word_dict, assist_dict, is_reverse_keys=False):
        """
        Create a word dictionary merged from the given tables with sorted keys list
        :param word_dict:
        :param assist_dict:
        :param is_reverse_keys:
        :return: merged dictionary, sorted list of dict keys
        """
        conversion_dict = {}

        for table in word_dict, assist_dict:
            for key, value in table.items():
                if is_reverse_keys:
                    conversion_dict[value] = key
                else:
                    conversion_dict[key] = value

        conversion_keys = conversion_dict.keys()
        conversion_keys.sort(key=lambda key: len(key), reverse=True)

        return conversion_dict, conversion_keys

    def _convert_text(self, regex_pattern, conversion_dict, text):
        """
        Use a regex to substitute characters to convert
        :param regex_pattern: precompiled regex pattern
        :param conversion_dict: conversion word dictionary
        :param text: text to convert
        :return: converted text
        """
        conversion = regex_pattern.sub(lambda key: conversion_dict[key.group(0)], text)

        return conversion

    def _pre_process_romaji(self, text):
        """
        Pre processing for difficult words
        :param romaji_text:
        :return: pre processed romaji text
        """
        preprocessed_text = text.lower()
        preprocessed_text = self.re_mba.sub(conversion_models.MBA_SUB_PATTERN, preprocessed_text)
        preprocessed_text = self.re_xu.sub(conversion_models.XU__SUB_PATTERN, preprocessed_text)
        preprocessed_text = self.re_a__.sub(conversion_models.A___SUB_PATTERN, preprocessed_text)

        return preprocessed_text

    def _post_process_romaji_text(self, text):
        """
        Post process for difficult words
        :param romaji_text:
        :return: post processed romaji text
        """
        postprocessed_text = self.re_xtu.sub(conversion_models.XTU_SUB_PATTERN, text)
        postprocessed_text = self.re_ltu.sub(conversion_models.LTU_SUB_PATTERN, postprocessed_text)
        postprocessed_text = self.re_er.sub(conversion_models.ER__SUB_PATTERN, postprocessed_text)
        postprocessed_text = self.re_n.sub(conversion_models.N___SUB_PATTERN, postprocessed_text)
        postprocessed_text = self.re_oo.sub(conversion_models.OO__SUB_PATTERN, postprocessed_text)

        return postprocessed_text

