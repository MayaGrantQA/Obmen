import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = t_combobox.get()
    name = cur[code]
    currency_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            responce = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            responce.raise_for_status()
            data = responce.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}')
                                                                # Сокращаем до 2 знаков после запятой
            else:
                mb.showerror('Ошибка!', "Валюта с таким кодом не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", 'Введите код валюты')


# Словарь кодов валют и их полных названий
cur = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
    "AMD": "Армянский драм"
}


window = Tk()
window.title('Курсы отмена валют')
window.geometry('360x300')

Label(text='Базовая валюта').pack(padx=10, pady=10)

b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
#b_combobox.bind("<<ComboboxSelected>>", update_currency_label)

Label(text='Целевая валюта').pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)


Button(text='Получить курс обмена', command=exchange).pack(padx=10, pady=10)

window.mainloop()
