from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image

def icon_clicked(icon):
    print("click")
# Create the systray icon
image = Image.open("icon.png")
#menu = pystray.Menu(pystray.MenuItem("Exit", lambda: exit()))
icona = icon(
    'test name',
    icon=image,
    menu=menu(
    item(
        'With submenu',
        menu(
            item(
                'Submenu item 1',
                lambda icon, item: 1),
            item(
                'Submenu item 2',
                lambda icon, item: 2))))
)

# To finally show you icon, call run
icona.run()