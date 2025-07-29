from datetime import date as date
from update_checker import update_check

last = open("last_check.txt", "r").read()

if str(date.today()) != last:
    print(update_check())
    open("last_check.txt", "w").write(str(date.today()))