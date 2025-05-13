import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Lista obsługiwanych walut
CURRENCIES = ['USD', 'GBP', 'JPY', 'EUR', 'PLN']

def get_rates(base='USD'):
    """
    Pobiera kursy walut względem waluty bazowej (base)
    z darmowego API exchangerate.host.
    Zwraca słownik {'USD': 1.0, 'EUR': 0.92, ...}
    """
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={','.join(CURRENCIES)}"
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    return data['rates']

def convert():
    """Obsługa przycisku Konwertuj"""
    amt_str = amount_var.get()
    try:
        amt = float(amt_str)
    except ValueError:
        messagebox.showerror("Błąd", "Nieprawidłowa kwota")
        return

    frm = from_var.get()
    to = to_var.get()
    if frm == to:
        result_var.set(f"{amt:.2f} {to}")
        return

    try:
        rates = get_rates(base=frm)
        rate = rates[to]
        converted = amt * rate
        result_var.set(f"{converted:.2f} {to}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się pobrać kursu:\n{e}")

# --- GUI ---
root = tk.Tk()
root.title("Przelicznik walut")

# Wygląd i styl
style = ttk.Style(root)
style.theme_use('clam')  # albo 'alt', 'default', 'classic'

frm = ttk.Frame(root, padding=20)
frm.grid(row=0, column=0)

ttk.Label(frm, text="Kwota:").grid(row=0, column=0, sticky='w')
amount_var = tk.StringVar(value="1.00")
ttk.Entry(frm, textvariable=amount_var, width=15).grid(row=0, column=1, padx=5)

ttk.Label(frm, text="Z:").grid(row=1, column=0, sticky='w')
from_var = tk.StringVar(value=CURRENCIES[0])
ttk.Combobox(frm, textvariable=from_var, values=CURRENCIES, state='readonly', width=13).grid(row=1, column=1, padx=5)

ttk.Label(frm, text="Na:").grid(row=2, column=0, sticky='w')
to_var = tk.StringVar(value=CURRENCIES[1])
ttk.Combobox(frm, textvariable=to_var, values=CURRENCIES, state='readonly', width=13).grid(row=2, column=1, padx=5)

ttk.Button(frm, text="Konwertuj", command=convert).grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar(value="—")
ttk.Label(frm, textvariable=result_var, font=('Segoe UI', 14, 'bold')).grid(row=4, column=0, columnspan=2)

root.mainloop()
