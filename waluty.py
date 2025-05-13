#!/usr/bin/env python3

# Mega chujowa wersja: przelicza tylko EUR ↔ PLN
# Kurs stały: 1 EUR = 4.252 PLN (stan na 13 maja 2025)

rate = 4.252

print("=== Źle/*+! Mega chujowa wersja przelicznika EUR/PLN ===")
amt = float(input("Podaj kwotę: "))            # brak ochrony przed błędnym inputem
mode = input("Wybierz kierunek (e – EUR→PLN, p – PLN→EUR): ")

if mode == "e":
    print(f"{amt} EUR = {amt * rate:.2f} PLN")
elif mode == "p":
    print(f"{amt} PLN = {amt / rate:.2f} EUR")
else:
    print("Elo, nie znam tej opcji – użyj 'e' albo 'p'.")
