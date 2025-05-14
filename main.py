from tkinter import *
from functions import (find_minimal_element,
                       find_average, 
                       find_second_max,
                       find_sum_among_even, 
                       is_monotonous)

def button_handler(func):
    def find():
        string = entry.get().split(', ')
        try:
            lst = [int(s) for s in string]
            result = func(lst)
            assert result is not None
        except (ValueError, AssertionError):
            label.config(text='При вычислении произошла ошибка, убедитесь\nЧто все написано по шаблону.')
        else:
            if isinstance(result, bool):
                result = 'Да' if result else 'Нет'

            label.config(text=f'Результат: {result}')
    return find

win = Tk()
win.title('Функции списков')
win.geometry('400x220')

find_min_button = Button(win, text='Найти минимум', command=button_handler(find_minimal_element))
find_avg_button = Button(win, text='Найти среднее', command=button_handler(find_average))
find_even_sum_button = Button(win, text='Найти сумму четных', command=button_handler(find_sum_among_even))
find_sec_max_button = Button(win, text='Найти второй максимум', command=button_handler(find_second_max))
is_mono_button = Button(win, text='Этот список монотонный?', command=button_handler(is_monotonous))

label = Label(win, text='Введите через запятую несколько натуральных чисел, например:\n1, 2, 3, 4\nИ выберите одну из опций.')
entry = Entry(win)

find_min_button.pack()
find_avg_button.pack()
find_even_sum_button.pack()
find_sec_max_button.pack()
is_mono_button.pack()

entry.pack()
label.pack()

win.mainloop()
