#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    splash = math.sqrt(a)
    return splash


def square(a: float) -> float:
    zoom = a**2
    return zoom


def average(a: float, b: float, c: float) -> float:
    miaou = ((a + b + c)/3)
    return miaou


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    b = angle_mins/60
    c = b + angle_degs
    a = angle_degs*2*(math.pi)/360
    return c


def to_degrees(angle_rads: float) -> tuple:
    total = angle_rads * 360/(2*math.pi)
    degre = int(total)
    reste = total-degre
    totalreste = reste * 60/1
    minute = int(totalreste)
    secondes = int((totalreste-minute)*60)
    #min = (degres - math.floor(degres) * 60
    #sec = (min - math.floor(min)) * 60
    return degre, minute, secondes


def to_celsius(temperature: float) -> float:
    a = (temperature-32)*5/9
    return a


def to_farenheit(temperature: float) -> float:
    b = (temperature * 9/5) + 32
    return b


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
