from tkinter import *
from tkinter import ttk
import pandas as pd
from bs4 import BeautifulSoup
import requests

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tool Crawling")
        self.tag_name = "h3"
        self.class_name = {'class':'s-item__title'}
        self.minsize(640, 400)
        self.urls = []
        self.initUI()
        #self.wm_iconbitmap('icon.ico')

    def link_import(self):
        self.urls.append(str(self.url.get()))
        print(self.urls[0])
        # print(type(self.urls[0]))
        print(len(self.urls))

    def initUI(self):
        self.url = StringVar()
        self.tag = StringVar()
        self.file_name = StringVar()
        self.label_link = ttk.Label(self, text="Links:")
        self.label_link.grid(column=0, row=1)

        self.label_tag = ttk.Label(self, text="File Name:")
        self.label_tag.grid(column=0, row=2)

        self.input_link = ttk.Entry(self, width=75, textvariable=self.url)
        self.input_link.grid(column=2, row=1)

        self.file_name_entry = ttk.Entry(self, width=30, textvariable=self.file_name)
        self.file_name_entry.grid(column=2, row=2)
        
        self.btn_import = ttk.Button(self, text="Import", command=self.link_import)
        self.btn_import.grid(column=3, row=1)
        self.btn_crawling = ttk.Button(self, text="Crawling", command=self.crawling)
        self.btn_crawling.grid(column=0, row=10)


        
    def crawling(self):

        list_product_title = []
        for url in self.urls:
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "lxml")
            product_titles = soup.find_all(self.tag_name, self.class_name)
            for product_title in product_titles:
                list_product_title.append(product_title.get_text())
        temp_dict = {
            "sentences":list_product_title
        }
        data_frame = pd.DataFrame(temp_dict)
        data_frame.to_csv(self.file_name.get(), index=False)
        print(self.file_name.get())

        


root = Root()
root.mainloop()