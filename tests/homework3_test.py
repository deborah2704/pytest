from homework3 import split_male_female, find_median_average, print_values_above
import pytest

data_set = {
            0: {"name": "deborah", "age": 21, "sex": "female"},
            1: {"name": "esther", "age": 25, "sex": "female"},
            2: {"name": "noa", "age": 34, "sex": "male"}
            }

def test_split_male_female(capfd):
    split_male_female(data_set)
    out, err = capfd.readouterr()
    assert out == ("[{'name': 'noa', 'age': 34, 'sex': 'male'}]\n"
 "[{'name': 'deborah', 'age': 21, 'sex': 'female'}, {'name': 'esther', 'age': "
 "25, 'sex': 'female'}]\n")

def test_find_median_average(capfd):
    find_median_average(data_set)
    out, err = capfd.readouterr()
    assert out == ("[21, 25, 34]\n26.666666666666668\n")

def test_print_values_above(capfd):
    print_values_above(data_set, 22)
    out, err = capfd.readouterr()
    assert out == ("{1: {'name': 'esther', 'age': 25, 'sex': 'female'}, 2: {'name': 'noa', 'age': 34, 'sex': 'male'}}\n")