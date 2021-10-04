import os
import time

import RPi.GPIO as GPIO
from binance.client import Client
from RPLCD import CharLCD

from utils import get_capital, get_current_positions, get_value

PIXEL_LENGTH = 16
GPIO.setwarnings(False)

client = Client(os.environ["API_KEY"], os.environ["SECRET_API"])
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)


def main():
    while True:
        capital = get_capital(client)
        current_positions = get_current_positions(client)

        if current_positions != []:
            for string in current_positions:
                len_word = len(string)
                for i in range(PIXEL_LENGTH + len_word):
                    lcd.clear()
                    if i != PIXEL_LENGTH + len_word - 1:
                        position, to_print = get_value(i, len_word, string, PIXEL_LENGTH)

                        lcd.cursor_pos = (0, position)
                        lcd.write_string(to_print)
                    else:
                        pass
                    lcd.cursor_pos = (1, 4)
                    lcd.write_string(f"${capital}$")
                    time.sleep(0.5)

        else:
            lcd.cursor_pos = (0, 0)
            lcd.write_string("BINANCE  FUTURES")

            lcd.cursor_pos = (1, 4)
            lcd.write_string(f"${capital}$")

        time.sleep(0.5)


if __name__ == "__main__":
    main()
