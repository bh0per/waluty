

rate = 4.252

print("===")
amt = float(input("Podaj kwotę: "))            
mode = input("Wybierz kierunek (e – EUR→PLN, p – PLN→EUR): ")

if mode == "e":
    print(f"{amt} EUR = {amt * rate:.2f} PLN")
elif mode == "p":
    print(f"{amt} PLN = {amt / rate:.2f} EUR")
else:
    print(" – użyj 'e' albo 'p'.")
