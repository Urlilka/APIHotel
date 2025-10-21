from tkinter import ttk, Tk
from tkinter import *

from requests import *

class Validate_API(Tk):
    def __init__(self):
        super().__init__()
        self.test_case_file = "ТестКейс.docx"

        # Получить API
        self.API_url = "http://prb.sylas.ru/TransferSimulator/fullName"

        self.title("Валидация Данных")
        self.geometry("500x200")

        self.data_API = ttk.Frame(self)
        self.data_API.pack(fill=X,padx=10,pady=10, anchor="center")

        self.data_button = ttk.Button(self.data_API,text="Получить Данные",command=self.get_API)
        self.data_button.pack()

    def get_API(self):
        response = get(self.API_url,{"key":"value"})
        print(response)