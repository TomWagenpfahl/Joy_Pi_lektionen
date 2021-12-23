#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import Adafruit_CharLCD as LCD
# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows = 2
# Festlegen des LCDs und der I2C Adresse in die Variable LCD
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
try:
    # Hintergrundbeleuchtung einschalten
    lcd.set_backlight(0)
    # Zwei Worte mit Zeilenumbruch werden ausgegeben
    lcd.message('Hallo\nWelt!')
    # 5 Sekunden warten
    time.sleep(5.0)
    # Cursor anzeigen lassen.
    lcd.clear()
    lcd.show_cursor(True)
    lcd.message('Show cursor')
    time.sleep(5.0)
    # Cursor Blinken Lassen.
    lcd.clear()
    lcd.blink(True)
    lcd.message('Blink cursor')
    time.sleep(5.0)
    # Stoppen den blinkenden Cursors und Cursor ausblenden.
    lcd.show_cursor(False)
    lcd.blink(False)
    # Nachricht von Rechts/Links scrollen lassen.
    lcd.clear()
    message = 'Scroll'
    lcd.message(message)
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
    lcd.move_right()
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
    lcd.move_left()
    # HIntergrundbeleuchtung an und ausschalten.
    lcd.clear()
    lcd.message('Flash backlight\nin 5 seconds...')
    time.sleep(5.0)
    # Hintergrundbeleuchtung ausschalten.
    lcd.set_backlight(1)
    time.sleep(2.0)
    # Nachricht ändern.
    lcd.clear()
    lcd.message('Goodbye!')
    # Hintergrundbeleuchtung einschalten.
    lcd.set_backlight(0)
    # Hintergrundbeleuchtung ausschalten.
    time.sleep(2.0)
    lcd.clear()
    lcd.set_backlight(1)
except KeyboardInterrupt:
    # LCD ausschalten.
    lcd.clear()
    lcd.set_backlight(1)