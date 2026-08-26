import tkinter as tk


def createMenu(window, timezone):
    menu = tk.Menu(window)

    timezoneMenu = tk.Menu(menu, tearoff=0)

    europeMenu = tk.Menu(timezoneMenu, tearoff=0)
    
    europeMenu.add_radiobutton(label="Copenhagen", variable=timezone, value="Europe/Copenhagen")
    europeMenu.add_radiobutton(label="London", variable=timezone, value="Europe/London")
    europeMenu.add_radiobutton(label="Paris", variable=timezone, value="Europe/Paris")
    europeMenu.add_radiobutton(label="Berlin", variable=timezone, value="Europe/Berlin")
    europeMenu.add_radiobutton(label="Rome", variable=timezone, value="Europe/Rome")
    europeMenu.add_radiobutton(label="Madrid", variable=timezone, value="Europe/Madrid")
    europeMenu.add_radiobutton(label="Amsterdam", variable=timezone, value="Europe/Amsterdam")
    europeMenu.add_radiobutton(label="Brussels", variable=timezone, value="Europe/Brussels")
    europeMenu.add_radiobutton(label="Vienna", variable=timezone, value="Europe/Vienna")
    europeMenu.add_radiobutton(label="Warsaw", variable=timezone, value="Europe/Warsaw")
    europeMenu.add_radiobutton(label="Prague", variable=timezone, value="Europe/Prague")
    europeMenu.add_radiobutton(label="Athens", variable=timezone, value="Europe/Athens")
    europeMenu.add_radiobutton(label="Helsinki", variable=timezone, value="Europe/Helsinki")
    europeMenu.add_radiobutton(label="Lisbon", variable=timezone, value="Europe/Lisbon")
    europeMenu.add_radiobutton(label="Moscow", variable=timezone, value="Europe/Moscow")
    europeMenu.add_radiobutton(label="Istanbul", variable=timezone, value="Europe/Istanbul")
    
    americaMenu = tk.Menu(timezoneMenu, tearoff=0)
    
    americaMenu.add_radiobutton(label="New York", variable=timezone, value="America/New_York")
    americaMenu.add_radiobutton(label="Chicago", variable=timezone, value="America/Chicago")
    americaMenu.add_radiobutton(label="Denver", variable=timezone, value="America/Denver")
    americaMenu.add_radiobutton(label="Los Angeles", variable=timezone, value="America/Los_Angeles")
    americaMenu.add_radiobutton(label="Phoenix", variable=timezone, value="America/Phoenix")
    americaMenu.add_radiobutton(label="Anchorage", variable=timezone, value="America/Anchorage")
    americaMenu.add_radiobutton(label="Toronto", variable=timezone, value="America/Toronto")
    americaMenu.add_radiobutton(label="Vancouver", variable=timezone, value="America/Vancouver")
    americaMenu.add_radiobutton(label="Mexico City", variable=timezone, value="America/Mexico_City")
    americaMenu.add_radiobutton(label="São Paulo", variable=timezone, value="America/Sao_Paulo")
    americaMenu.add_radiobutton(label="Buenos Aires", variable=timezone, value="America/Argentina/Buenos_Aires")
    
    asiaMenu = tk.Menu(timezoneMenu, tearoff=0)
    
    asiaMenu.add_radiobutton(label="Tokyo", variable=timezone, value="Asia/Tokyo")
    asiaMenu.add_radiobutton(label="Seoul", variable=timezone, value="Asia/Seoul")
    asiaMenu.add_radiobutton(label="Shanghai", variable=timezone, value="Asia/Shanghai")
    asiaMenu.add_radiobutton(label="Hong Kong", variable=timezone, value="Asia/Hong_Kong")
    asiaMenu.add_radiobutton(label="Singapore", variable=timezone, value="Asia/Singapore")
    asiaMenu.add_radiobutton(label="Bangkok", variable=timezone, value="Asia/Bangkok")
    asiaMenu.add_radiobutton(label="Jakarta", variable=timezone, value="Asia/Jakarta")
    asiaMenu.add_radiobutton(label="Manila", variable=timezone, value="Asia/Manila")
    asiaMenu.add_radiobutton(label="Kolkata", variable=timezone, value="Asia/Kolkata")
    asiaMenu.add_radiobutton(label="Dubai", variable=timezone, value="Asia/Dubai")
    asiaMenu.add_radiobutton(label="Jerusalem", variable=timezone, value="Asia/Jerusalem")
    
    
    africaMenu = tk.Menu(timezoneMenu, tearoff=0)
    
    africaMenu.add_radiobutton(label="Cairo", variable=timezone, value="Africa/Cairo")
    africaMenu.add_radiobutton(label="Johannesburg", variable=timezone, value="Africa/Johannesburg")
    africaMenu.add_radiobutton(label="Lagos", variable=timezone, value="Africa/Lagos")
    africaMenu.add_radiobutton(label="Nairobi", variable=timezone, value="Africa/Nairobi")
    africaMenu.add_radiobutton(label="Casablanca", variable=timezone, value="Africa/Casablanca")
    africaMenu.add_radiobutton(label="Tunis", variable=timezone, value="Africa/Tunis")
    africaMenu.add_radiobutton(label="Algiers", variable=timezone, value="Africa/Algiers")
    africaMenu.add_radiobutton(label="Accra", variable=timezone, value="Africa/Accra")
    africaMenu.add_radiobutton(label="Addis Ababa", variable=timezone, value="Africa/Addis_Ababa")
    
    oceaniaMenu = tk.Menu(timezoneMenu, tearoff=0)
    
    oceaniaMenu.add_radiobutton(label="Sydney", variable=timezone, value="Australia/Sydney")
    oceaniaMenu.add_radiobutton(label="Melbourne", variable=timezone, value="Australia/Melbourne")
    oceaniaMenu.add_radiobutton(label="Brisbane", variable=timezone, value="Australia/Brisbane")
    oceaniaMenu.add_radiobutton(label="Perth", variable=timezone, value="Australia/Perth")
    oceaniaMenu.add_radiobutton(label="Adelaide", variable=timezone, value="Australia/Adelaide")
    oceaniaMenu.add_radiobutton(label="Darwin", variable=timezone, value="Australia/Darwin")
    oceaniaMenu.add_radiobutton(label="Auckland", variable=timezone, value="Pacific/Auckland")
    oceaniaMenu.add_radiobutton(label="Wellington", variable=timezone, value="Pacific/Auckland")
    oceaniaMenu.add_radiobutton(label="Fiji", variable=timezone, value="Pacific/Fiji")
    oceaniaMenu.add_radiobutton(label="Honolulu", variable=timezone, value="Pacific/Honolulu")
    
    timezoneMenu.add_cascade(label="Europe", menu=europeMenu)
    timezoneMenu.add_cascade(label="America", menu=americaMenu)
    timezoneMenu.add_cascade(label="Asia", menu=asiaMenu)
    timezoneMenu.add_cascade(label="Africa", menu=africaMenu)
    timezoneMenu.add_cascade(label="Oceania", menu=oceaniaMenu)

    menu.add_cascade(label="Timezone", menu=timezoneMenu)

    window.config(menu=menu)
