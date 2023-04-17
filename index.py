import pystray
from Pillow import Image

def on_exit():
    print("Exiting...")

def on_click(icon):
    print("Icon clicked")

image = Image.open("icon.png")

menu = pystray.Menu(pystray.MenuItem("Exit", on_exit))

icon = pystray.Icon("name", image, "Tooltip", menu)

icon.run(on_click)
