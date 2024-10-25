import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange():
    code = combobox.get()

    if code:
        try:
            responce = requests.get('https://open.er-api.com/v6/latest/USD')
            responce.raise_for_status()
            data = responce.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {code} за 1 доллар')
                                                                # Сокращаем до 2 знаков после запятой
            else:
                mb.showerror('Ошибка!', "Валюта с таким кодом не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", 'Введите код валюты')


window = Tk()
window.title('Курсы отмена валют')
window.geometry('360x180')

Label(text='Выберите код валюты').pack(padx=10, pady=10)
cur = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD', 'AMD']
combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()
