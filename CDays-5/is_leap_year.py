
from datetime import datetime


class TimeUtil:
    def __init__(self):
        today = datetime.today()
        self.default_year = today.year

    def is_leap_year(self, start_year=0, end_year=0):
        # 判断闰年条件，满足年份模 400 为 0，或者模 4 为 0 但模 100不为 0。
        if start_year == 0:
            start_year = self.default_year
        if end_year == 0:
            end_year = start_year
        if end_year < start_year:
            raise Exception("end_year must greater than start year")
        is_leap_year = dict()
        for year in range(start_year, end_year+1):
            leap_year1 = year % 400
            leap_year2 = year % 4
            leap_year3 = year % 100
            if leap_year1 == 0 \
            or (leap_year2 == 0 and leap_year3 != 0):
                # is leap year
                is_leap_year[year] = True
            else:
                is_leap_year[year] = False
            # print(f"{year} is {is_leap_year.get(year)} leap year")
        return is_leap_year
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='year to check leap year')
    parser.add_argument('-sy', '--start_year', type=int, default=0, help='year to check leap year')
    parser.add_argument('-ey', '--end_year', type=int, default=0, help='year to check leap year')
    args = parser.parse_args()
    s_year = args.start_year
    e_year = args.end_year
    tu = TimeUtil()
    is_leap_year = tu.is_leap_year(s_year,e_year)
    for k,v in is_leap_year.items():
        if v:
            print(f"{k} is {v} leap year")
