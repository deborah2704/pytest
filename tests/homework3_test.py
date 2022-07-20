from homework3 import split_male_female, find_median_average, print_values_above
import pytest

def test_split_male_female(capfd):
    data_set = {
            0: {"name": "deborah", "age": 21, "sex": "female"},
            1: {"name": "esther", "age": 25, "sex": "female"},
            2: {"name": "noa", "age": 34, "sex": "male"}
            }
    split_male_female(data_set)
    out, err = capfd.readouterr()
    assert out == ("[{'name': 'noa', 'age': 34, 'sex': 'male'}]\n"
 "[{'name': 'deborah', 'age': 21, 'sex': 'female'}, {'name': 'esther', 'age': "
 "25, 'sex': 'female'}]\n")
