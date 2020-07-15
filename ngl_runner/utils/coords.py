import pyautogui as pag


def listen():
    try:
        while True:
            x, y = pag.position()
            posStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(posStr)
            print("\b" * len(posStr))
    except KeyboardInterrupt:
        print("\n")


if __name__ == "__main__":
    listen()
