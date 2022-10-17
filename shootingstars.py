from month import Month


class ShootingStars:
    def __init__(self, year_capacity):
        self.star_count = dict()
        self.year_capacity = year_capacity

        for i in range(0, year_capacity):
            year = dict()
            if i == 0:
                year[Month.NOVEMBER.name] = [0] * Month.NOVEMBER.val
                year[Month.DECEMBER.name] = [0] * Month.DECEMBER.val
            else:
                for m in Month:
                    year[m.name] = [0] * m.val
            self.star_count[i] = year

    def increase_capacity(self, additional_capacity):
        for i in range(self.year_capacity, self.year_capacity + additional_capacity):
            year = dict()

            for m in Month:
                year[m.name] = [0] * m.val
            self.star_count[i] = year
        self.year_capacity += additional_capacity

    # indexing of years and days start from 1 from an outside point of view
    def add(self, year, month, day, value):
        try:
            self.star_count[year - 1][month.name][day - 1] = value
        except KeyError:
            raise Exception("Invalid month/date/day")

    def get_count_for_day(self, day):
        count = 0
        for year in self.star_count.values():
            for days in year.values():
                try:
                    count += days[day - 1]
                except IndexError:
                    count += 0
        return count

    def get_count_for_month(self, month):
        count = 0
        for year in self.star_count.values():
            count += sum(year.get(month.name, []))
        return count

    def print(self):
        for year in self.star_count.values():
            for month, days in year.items():
                print('%-10s: ' % month, end="")
                for day in days:
                    print("%-3s" % day, end="")
                print()
