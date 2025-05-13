import tkinter as tk
from tkinter import ttk, messagebox

# Kursy walut względem PLN (stan na 13 maja 2025)
RATES_TO_PLN = {
    'USD': 3.8271,
    'GBP': 5.058,
    'EUR': 4.252,
    'JPY': 0.025827,
    'PLN': 1.0,
}

CURRENCIES = list(RATES_TO_PLN.keys())

def convert():
    """Obsługa przycisku Konwertuj: najpierw na PLN, potem na walutę docelową."""
    try:
        amt = float(amount_var.get().replace(',', '.'))
    except ValueError:
        messagebox.showerror("Błąd", "Nieprawidłowa kwota")
        return

    frm = from_var.get()
    to = to_var.get()
    if frm == to:
        result_var.set(f"{amt:.2f} {to}")
        return

    # konwersja: najpierw na PLN, potem na docelową
    pln = amt * RATES_TO_PLN[frm]
    converted = pln / RATES_TO_PLN[to]
    result_var.set(f"{converted:.2f} {to}")

# --- GUI ---
root = tk.Tk()
root.title("Przelicznik walut (kursy stałe)")

style = ttk.Style(root)
style.theme_use('clam')  # lekkie, nowoczesne

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
