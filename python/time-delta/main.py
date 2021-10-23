from datetime import datetime


def calc_time_delta(date1, date2):
    form = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(date1, form)
    d2 = datetime.strptime(date2, form)
    diff = (d2-d1).total_seconds()
    return abs(int(diff))

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print(calc_time_delta(input(), input()))
