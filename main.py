from datetime import date as date
from update_checker import update_check
import eel

last = open("last_check.txt", "r").read()

eel.init('html stuff')

@eel.expose
def update():
    if str(date.today()) != last:
        open("last_check.txt", "w").write(str(date.today()))
        return update_check()
    else:
        return "Already checked for updates today."

eel.start('index.html', size=(700, 500))