
def split_male_female(data_set: dict):
    """
    :param data_set: dict
    :return:
    """
    male = []
    female = []
    for key, item in data_set.items():
        if item["sex"] == "male":
            male.append(item)
        else:
            female.append(item)
    print(male)
    print(female)

def find_median_average(data_set: dict):
    """
    :param data_set: dict
    :return:
    """
    aavg = []
    for key, item in data_set.items():
        aavg.append(item["age"])
    avg = sum(aavg) / len(aavg)
    aavg = sorted(aavg)
    print(aavg)
    print(avg)

def print_values_above(data_set, min = 0):
    """
    :param data_set: dict
    :param min: int
    :return:
    """
    res = {}
    for key, item in data_set.items():
        if item["age"] >= min:
            res[key] = item
    print(res)

def main():
    data_set = {
            0: {"name": "deborah", "age": 21, "sex": "female"},
            1: {"name": "esther", "age": 25, "sex": "female"},
            2: {"name": "noa", "age": 34, "sex": "male"}
            }
    split_male_female(data_set)
    find_median_average(data_set)
    print_values_above(data_set, 22)

if __name__ == '__main__':
    main()
