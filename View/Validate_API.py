from tkinter import ttk, Tk
from tkinter import *

import re
from requests import get # ответы для прилоджений
from docx import Document



class Validate_API(Tk):
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
        # Допусимые символы
        patterns = r'^[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+$'
        if re.fullmatch(patterns,self.name): #Если в строке только разрешённые символы из patterns
            self.validate_message["text"] = "ФИО не содержит запрещённые символы"
            self.save_result(self.name,"Успешно", "Успешно")
        else:
            self.validate_message["text"] = "ФИО содержит запрещённые символы"
            self.save_result(self.name,"Не успешно", "Не успешно")


    def get_API(self):
        response = get(self.API_url,{"key":"value"})
        self.name = response.json()["value"]
        self.data_value["text"] = self.name


    def save_result(self, name, revers_result, result):
        self.document = "Docs/ТестКейс.docx"
        doc = Document(self.document)
        row_cell = doc.tables[0].add_row().cells
        row_cell[0].text = name
        row_cell[1].text = revers_result
        row_cell[2].text = result

        doc.save(self.document)



if __name__ == "__main__":
    window = Validate_API()
    window.mainloop()