from datetime import datetime
from zoneinfo import ZoneInfo


def drawBinary(canvas, value, x, y, bits):
    """function for creating the binary dots

    Args:
        canvas (tk.canvas): canvas for the dots to be drawn on
        value (int): value of the binary number
        x (int): X cordinate of the first dot
        y (int): Y cordinate of the first dot
        bits (int): number of bits to display
    """
    binary = format(value, f"0{bits}b")[::-1]

    for i, bit in enumerate(binary):
        circleY = y + i * 30

        if bit == "1":
            color = "lime"

        else:
            color = "gray"

        canvas.create_oval(x, circleY, x + 20, circleY + 20, fill=color)


def updateClock(window, clock, timezoneLabel, timezone):
    """Function for updating the timeevery second

    Args:
        window (tk.Tk): Main window for clock to be updated
        clock (tk.Canvas): Canvas for displaying the binary clock
        timezoneLabel (tk.Label): label for displaying the timezone
        timezone (tk.StringVar): Variable of the current selected timezone
    """
    currentTime = datetime.now(ZoneInfo(timezone.get()))

    clock.delete("all")
    hours = currentTime.hour
    minutes = currentTime.minute
    seconds = currentTime.second

    clock.create_text(90, 20, text="Hours", fill="white")
    clock.create_text(180, 20, text="Minutes", fill="white")
    clock.create_text(270, 20, text="Seconds", fill="white")

    values = [1, 2, 4, 8, 16, 32]

    for i, value in enumerate(values):
        clock.create_text(300, 58 + i * 30, text=value, fill="white")

    drawBinary(clock, hours, 80, 50, 5)
    drawBinary(clock, minutes, 170, 50, 6)
    drawBinary(clock, seconds, 260, 50, 6)

    timezoneLabel.config(text=timezone.get())
    window.after(1000, updateClock, window, clock, timezoneLabel, timezone)
