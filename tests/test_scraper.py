import unittest

import pytest
import Scraper

class TestScraper():

    def test_get_standard_infos(self):
        sc = Scraper.Scraper("https://www.youtube.com/watch?v=BjhW3vBA1QU")
        sc.get_standard_infos()
        assert sc._infos["videoId"] == "BjhW3vBA1QU"
        assert sc._infos["title"] == "J Balvin, Dua Lipa, Bad Bunny, Tainy - UN DIA (ONE DAY)"
        assert sc._infos["author"] == "jbalvinVEVO"
        assert sc._infos["description"] != ""

    def test_get_like(self):
        sc = Scraper.Scraper("https://www.youtube.com/watch?v=BjhW3vBA1QU")
        sc.get_like()
        assert isinstance(sc._infos["like"],int)

    def test_find_link(self):
        sc = Scraper.Scraper("https://www.youtube.com/watch?v=BjhW3vBA1QU")
        sc.find_link()
        assert sc._infos["links"]!=[]