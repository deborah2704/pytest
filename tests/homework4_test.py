from homework4 import Date
import pytest
import logging

def test_date_is_not_valid():
    d = Date(33, 12, 2000)
    logging.info(d.__str__())
    assert d.isValid() is False

def test_date_is_valid():
    d = Date(20, 1, 2015)
    logging.info(d.__str__())
    assert d.isValid() is True

def test_next_day():
    d = Date(1, 1, 2022)
    nd = d.getNextDay()
    logging.info(d.__str__())
    logging.info(nd.__str__())
    assert nd.__str__() == '2/1/2022'

def test_get_next_days():
    d = Date(1, 1, 2022)
    n3d = d.getNextDays(3)
    logging.info(d.__str__())
    logging.info(n3d.__str__())
    assert n3d.__str__() == '4/1/2022'

def test_eq():
    d = Date(1, 1, 2022)
    dd = Date(1, 3, 2022)
    logging.info(d.__str__())
    logging.info(dd.__str__())
    assert d.__eq__(dd) is False

def test_lt():
    d = Date(1, 1, 2022)
    dd = Date(1, 3, 2022)
    logging.info(d.__str__())
    logging.info(dd.__str__())
    assert d.__lt__(dd) is True

def test_gt():
    d = Date(1, 1, 2022)
    dd = Date(1, 3, 2022)
    logging.info(d.__str__())
    logging.info(dd.__str__())
    assert d.__gt__(dd) is False

def test_sub():
    d = Date(31, 12, 2000)
    dd = Date(1, 3, 2000)
    logging.info(d.__str__())
    logging.info(dd.__str__())
    assert d.__sub__(dd) == 306


