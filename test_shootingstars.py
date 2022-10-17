import pytest
from shootingstars import ShootingStars
from month import Month


class TestShootingStars:

    @pytest.fixture(autouse=True)
    def before_each(self):
        self.stars = ShootingStars(5)

    def test_count_for_month(self):
        self.stars.add(1, Month.NOVEMBER, 1, 10)
        self.stars.add(1, Month.NOVEMBER, 2, 10)
        self.stars.add(2, Month.NOVEMBER, 1, 10)
        self.stars.add(2, Month.DECEMBER, 2, 10)

        assert self.stars.get_count_for_month(Month.NOVEMBER) == 30

    def test_count_for_month_empty(self):
        self.stars.add(1, Month.NOVEMBER, 1, 10)
        self.stars.add(1, Month.NOVEMBER, 2, 10)
        self.stars.add(2, Month.NOVEMBER, 1, 10)
        self.stars.add(2, Month.DECEMBER, 2, 10)

        assert self.stars.get_count_for_month(Month.JANUARY) == 0

    def test_count_for_day(self):
        self.stars.add(1, Month.NOVEMBER, 1, 10)
        self.stars.add(1, Month.NOVEMBER, 2, 10)
        self.stars.add(2, Month.NOVEMBER, 3, 10)
        self.stars.add(2, Month.DECEMBER, 3, 10)

        assert self.stars.get_count_for_day(3) == 20

    def test_count_for_day_31th(self):
        self.stars.add(1, Month.NOVEMBER, 1, 10)
        self.stars.add(1, Month.NOVEMBER, 2, 10)
        self.stars.add(2, Month.OCTOBER, 31, 10)
        self.stars.add(2, Month.DECEMBER, 31, 10)

        assert self.stars.get_count_for_day(31) == 20

    def test_count_for_day_empty(self):
        self.stars.add(1, Month.NOVEMBER, 1, 10)
        self.stars.add(1, Month.NOVEMBER, 2, 10)
        self.stars.add(2, Month.NOVEMBER, 3, 10)
        self.stars.add(2, Month.DECEMBER, 3, 10)

        assert self.stars.get_count_for_day(10) == 0

    def test_add_invalid_month_throws_exception(self):
        with pytest.raises(Exception):
            self.stars.add(1, Month.JANUARY, 1, 10)

    def test_add_invalid_day_throws_exception(self):
        with pytest.raises(Exception):
            self.stars.add(1, Month.FEBRUARY, 1, 31)

    def test_add_duplicate_entry(self):
        self.stars.add(2, Month.NOVEMBER, 3, 10)
        self.stars.add(2, Month.NOVEMBER, 3, 10)

        assert self.stars.get_count_for_day(3) == 10
        assert self.stars.get_count_for_month(Month.NOVEMBER) == 10
