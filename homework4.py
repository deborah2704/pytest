class Date:
    def __init__(self, day, month, year):
        """
        :param day: int
        :param month: int
        :param year: int
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        """
        :return: str
        """
        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)

    def isValid(self):
        """
        :return: bool
        """
        valid = True
        if not (isinstance(self.day, int) and isinstance(self.month, int) and isinstance(self.year, int)):
            valid = False
        if (self.month in [1, 3, 5, 7, 8, 10, 12]):
            valid = self.day <= 31
        if (self.month in [4, 6, 9, 11]):
            valid = self.day <= 30
        if (self.month == 2):
            if (self.year % 4 == 0):
                valid = self.day <= 29
            else:
                valid = self.day <= 28
        if (self.month > 12):
            valid = False
        return valid

    def getNextDay(self):
        """
        :return: Date
        """
        nextDay = Date(self.day + 1, self.month, self.year)
        if (nextDay.isValid()):
            return nextDay
        else:
            nextDay = Date(1, self.month + 1, self.year)
            if (nextDay.isValid()):
                return nextDay
            else:
                return Date(1, 1, self.year + 1)

    def getNextDays(self, daysToAdd):
        """
        :param daysToAdd: int
        :return: Date
        """
        nextDays = self
        for i in range(daysToAdd):
            nextDays = nextDays.getNextDay()
        return nextDays

    def __eq__(self, obj):
        """
        :param obj: Date
        :return: bool
        """
        return self.day == obj.day and self.month == obj.month and self.year == obj.year

    def __lt__(self, obj):
        """
        :param obj: Date
        :return: bool
        """
        d1 = str(self.year).zfill(4) + str(self.month).zfill(2) + str(self.day).zfill(2)
        d2 = str(obj.year).zfill(4) + str(obj.month).zfill(2) + str(obj.day).zfill(2)
        return int(d1) < int(d2)

    def __gt__(self, obj):
        """
        :param obj: Date
        :return: bool
        """
        d1 = str(self.year).zfill(4) + str(self.month).zfill(2) + str(self.day).zfill(2)
        d2 = str(obj.year).zfill(4) + str(obj.month).zfill(2) + str(obj.day).zfill(2)
        return int(d1) > int(d2)

    def __sub__(self, obj):
        """
        :param obj: Date
        :return: int
        """
        days = 0
        found = False
        while not found:
            if self.__eq__(obj):
                found = True
            obj = obj.getNextDay()
            days = days + 1
        return days

def main():
    d = Date(31, 12, 2000)
    print(d.isValid())
    print(d.getNextDay().__str__())
    print(d.getNextDays(33).__str__())

    d1 = Date(1, 3, 2000)
    print(d.__eq__(d1))
    print(d.__lt__(d1))
    print(d.__gt__(d1))
    print(d.__sub__(d1))

if __name__ == '__main__':
    main()
    