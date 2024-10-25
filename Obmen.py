import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = combobox.get()
    name = cur[code]
    currency_label.config(text=name)


def exchange():
    code = combobox.get()

    if code:
        try:
            responce = requests.get('https://open.er-api.com/v6/latest/USD')
            responce.raise_for_status()
            data = responce.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                c_name = cur[code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {c_name} за 1 доллар')
                                                                # Сокращаем до 2 знаков после запятой
            else:
                mb.showerror('Ошибка!', "Валюта с таким кодом не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", 'Введите код валюты')


# Словарь кодов валют и их полных названий
cur = {
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
window.geometry('360x180')

Label(text='Выберите код валюты').pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)


Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()
