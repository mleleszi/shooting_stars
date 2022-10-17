from enum import Enum


class Value:
    def __init__(self, value):
        self.value = value


class Month(Enum):
    JANUARY = Value(31)
    FEBRUARY = Value(28)
    MARCH = Value(30)
    APRIL = Value(31)
    MAY = Value(30)
    JUNE = Value(30)
    JULY = Value(31)
    AUGUST = Value(31)
    SEPTEMBER = Value(30)
    OCTOBER = Value(31)
    NOVEMBER = Value(30)
    DECEMBER = Value(31)

    @property
    def val(self):
        return self.value.value
