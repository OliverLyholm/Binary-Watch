from datetime import datetime
from zoneinfo import ZoneInfo


def updateClock(window, clock, timezoneLabel, timezone):
    currentTime = datetime.now(ZoneInfo(timezone.get()))
    clock.config(text=currentTime.strftime("%H:%M:%S"))
    timezoneLabel.config(text=timezone.get())
    window.after(1000, updateClock, window, clock, timezoneLabel, timezone)
