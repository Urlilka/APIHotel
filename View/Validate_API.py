from tkinter import ttk, Tk
from tkinter import *

import re
from requests import get # ответы для прилоджений
from docx import Document



class Validate_API(Tk):
    """Окно проверки данных, получаемых из API
    """
    def __init__(self):
        super().__init__()
        self.test_case_file = "ТестКейс.docx"


        # Получить API
        self.API_url = "http://prb.sylas.ru/TransferSimulator/fullName"

        # Окно
        self.title("Валидация Данных")
        self.geometry("550x160")


        # Первая строка
        # Фрейм
        self.data_API = ttk.Frame(self)
        self.data_API.pack(fill=X,padx=10,pady=10, anchor="center")

        # Кнопка
        self.data_button = ttk.Button(self.data_API,text="Получить Данные",command=self.get_API)
        self.data_button.grid(sticky=NSEW,row=0,column=0,ipadx=50,ipady=10,padx=5,pady=5)

        # Текст
        self.data_value = ttk.Label(self.data_API, text="")
        self.data_value.grid(sticky=E,row=0,column=1,ipadx=5,ipady=10,padx=5,pady=5)


        # Вторая строка
        # Фрейм
        self.validate_API = ttk.Frame(self)
        self.validate_API.pack(anchor="center",fill=X,padx=10,pady=10)
        
        # Кнопка
        self.validate_button = ttk.Button(self.validate_API, text="Отправить результат теста",command=lambda: self.send_API(self.name))
        self.validate_button.grid(sticky=E,row=0,column=0,ipadx=5,ipady=10,padx=5,pady=5)

        # Текст
        self.validate_message = ttk.Label(self.validate_API,text="")
        self.validate_message.grid(sticky=E,row=0,column=1,ipadx=5,ipady=10,padx=5,pady=5)



    def send_API(self, name):
        """Проверяет полученное имя из "get_API()" И проверяет на запрещённые сиволы, вызывает и вносит данные в "save_result(name, waiting_result, result)"

        Args:
            name (str): Имя, полученное из "get_API()"
        """
        # Допусимые символы
        patterns = r'^[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+$'
        if re.fullmatch(patterns,self.name): #Если в строке только разрешённые символы из patterns
            self.validate_message["text"] = "ФИО не содержит запрещённые символы"
            waiting_result = self.clear_text(self.name)
            self.save_result(self.name, waiting_result, "Успешно")
        else:
            self.validate_message["text"] = "ФИО содержит запрещённые символы"
            waiting_result = self.clear_text(self.name)
            self.save_result(self.name, waiting_result, "Не успешно")


    def get_API(self):
        """Получает данные из API в виде списка{"key":"value"}, и записывает значение в переменную
        """
        response = get(self.API_url,{"key":"value"})
        self.name = response.json()["value"]
        self.data_value["text"] = self.name


    def save_result(self, name, waiting_result, result):
        """Вводит данные в "Docs/ТестКейс.docx"

        Args:
            name (str): Идёт в первую колонку таблицы
            waiting_result (str): Идёт во вторую колонку таблицы
            result (str): Идёт в третью колонку таблицы
        """
        self.document = "Docs/ТестКейс.docx"
        doc = Document(self.document)
        row_cell = doc.tables[0].add_row().cells
        row_cell[0].text = f"Проверка на запрещённые символы:\n{name}"
        row_cell[1].text = waiting_result
        row_cell[2].text = result

        doc.save(self.document)


    def clear_text(self, name):
        """Очищает вводимые данные от запрещёных знаков

        Args:
            name (str): Вводимое имя, которое нужно очистить

        Returns:
            str: То же имя, но без запрещённых символов
        """
        return re.sub(r'[^а-яА-ЯёЁ\s]',"",name)


# if __name__ == "__main__":
#     window = Validate_API()
#     window.mainloop()