from evdev import categorize, ecodes, InputDevice, UInput


# https://python-evdev.readthedocs.io/en/latest/tutorial.html#create-uinput-device-with-capabilities-of-another-device

dev = InputDevice('/dev/input/event20')
print(dev.capabilities(verbose=True))
# needs sudo
with UInput() as ui:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            cat = categorize(event)
            if cat.keycode == 'BTN_TOP':
                # write "a"
                ui.write(ecodes.EV_KEY, ecodes.KEY_A, cat.keystate)
                ui.syn()
