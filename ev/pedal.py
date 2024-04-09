import asyncio

import evdev
from xdo import Xdo  # type: ignore

"""
time 1685160043.952755 type 4 (EV_MSC), code 4    (MSC_SCAN), value 458831
time 1685160043.952755 type 1 (EV_KEY), code 23   (KEY_I), value 1
time 1685160043.952755 --------- SYN_REPORT --------
time 1685160043.952769 type 4 (EV_MSC), code 4    (MSC_SCAN), value 458831
time 1685160043.952769 type 1 (EV_KEY), code 23   (KEY_I), value 0
time 1685160043.952769 --------- SYN_REPORT --------
time 1685160057.369108 type 4 (EV_MSC), code 4    (MSC_SCAN), value 458832
time 1685160057.369108 type 1 (EV_KEY), code 1    (KEY_ESC), value 1
time 1685160057.369108 --------- SYN_REPORT --------
time 1685160057.369158 type 4 (EV_MSC), code 4    (MSC_SCAN), value 458832
time 1685160057.369158 type 1 (EV_KEY), code 1    (KEY_ESC), value 0

---

InputEvent(1685160120, 424949, 4, 4, 458831)
InputEvent(1685160120, 424949, 1, 23, 1)
InputEvent(1685160120, 424949, 0, 0, 0)
InputEvent(1685160120, 425034, 4, 4, 458831)
InputEvent(1685160120, 425034, 1, 23, 0)
InputEvent(1685160120, 425034, 0, 0, 0)
InputEvent(1685160121, 769043, 4, 4, 458831)
InputEvent(1685160121, 769043, 1, 23, 1)
InputEvent(1685160121, 769043, 0, 0, 0)
InputEvent(1685160121, 769125, 4, 4, 458831)
InputEvent(1685160121, 769125, 1, 23, 0)
InputEvent(1685160121, 769125, 0, 0, 0)
"""

NAME = "KOPPO"
WHITELIST = ["alacritty"]


def get_device():
    for path in evdev.list_devices():
        candidate = evdev.InputDevice(path)
        if candidate.name == NAME:
            return candidate


async def foo(dev):
    x = Xdo()
    fake = evdev.UInput()
    async for ev in dev.async_read_loop():
        window = x.get_focused_window_sane()
        wname = x.get_window_name(window).decode("utf-8").lower()
        if wname not in WHITELIST:
            continue

        if ev.type == evdev.ecodes.EV_KEY:
            # print(ev)
            print(evdev.categorize(ev))
            print(ev, ev.type, ev.code, ev.value)
            print("---")
            fake.write(ev.type, ev.code, ev.value)
            fake.syn()

    fake.close()


def main():
    device = get_device()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(foo(device))


if __name__ == "__main__":
    main()
