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
    binary = format(value, f"0{bits}b")

    for i, bit in enumerate(binary):
        circleY = y - (bits - i - 1) * 30

        if bit == "1":
            color = "#428bff"

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
    
    hourTens = currentTime.hour // 10
    hourOnes = currentTime.hour % 10
    
    minuteTens = currentTime.minute // 10
    minuteOnes = currentTime.minute % 10
    
    secondTens = currentTime.second // 10
    secondOnes = currentTime.second % 10
    

    clock.create_text(50, 280, text="Hours", fill="white")
    clock.create_text(150, 280, text="Minutes", fill="white")
    clock.create_text(250, 280, text="Seconds", fill="white")

    values = [8, 4, 2, 1]

    for i, value in enumerate(values):
        clock.create_text(300, 158 + i * 30, text=value, fill="white")

    drawBinary(clock, hourTens, 20, 240, 2)
    drawBinary(clock, hourOnes, 60, 240, 4)

    drawBinary(clock, minuteTens, 120, 240, 3)
    drawBinary(clock, minuteOnes, 160, 240, 4)

    drawBinary(clock, secondTens, 220, 240, 3)
    drawBinary(clock, secondOnes, 260, 240, 4)
    
    timezoneLabel.config(text=timezone.get())
    window.after(1000, updateClock, window, clock, timezoneLabel, timezone)
