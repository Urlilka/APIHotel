from tkinter import ttk, Tk
from tkinter import *

from re import fullmatch
from requests import get # ответы для прилоджений



class Validate_API(Tk):
    def __init__(self):
        super().__init__()
        self.test_case_file = "ТестКейс.docx"


        # Получить API
        self.API_url = "http://prb.sylas.ru/TransferSimulator/fullName"

        # Окно
        self.title("Валидация Данных")
        self.geometry("500x200")


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
        patterns = r'^[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+\s[а-яА-ЯёЁ]+&'
        if self.name == "":
            pass
        if re.fullmatch(patterns,name): #Если в строке только разрешённые символы из patterns
            self.validate_message["text"] = "ФИО не содержит запрещённые символы"
        else:
            self.validate_message["text"] = "ФИО содержит запрещённые символы"


    def get_API(self):
        response = get(self.API_url,{"key":"value"})
        self.name = response.json()["value"]
        self.data_value["text"] = self.name


    # def save_result(self, name, result):
    #     doc = Document(self.test_case_file)
    #     row_calls = doc.tables[0].add_row().cells
    #     row_calls[0].text = f"Проверка ФИО {self.data_value}"
    #     row_calls[1].text = name
    #     row_calls[2].text = result
    #     for par in cell.paragraph:
    #         pass



if __name__ == "__main__":
    window = Validate_API()
    window.mainloop()