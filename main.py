from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
# from re import *
# from algorithms import *
from searching_algorithms import *
from sorting_Arr import *

id = []
brandName = []
price = []
Discription = []
returnPolicy = []
instalment = []
Discount = []
seller_Name = []

sid = []
sbrandName = []
sprice = []
sDiscription = []
sreturnPolicy = []
sinstalment = []
sDiscount = []
sseller_Name = []


def loadDataFromFile():
    price = []
    pf = pd.read_csv("scrap.csv")
    id = pf["id"].values.tolist()
    brandName = pf["Brand Name"].values.tolist()
    pri = pf["price"].values.tolist()
    for i in pri:
        new = i.replace('Rs.', '')
        price.append(new)
    Discription = pf["Discription"].values.tolist()
    returnPolicy = pf["Warranty"].values.tolist()
    instalment = pf["instalment"].values.tolist()
    Dis = pf["Discount"].values.tolist()
    for j in Dis:
        ds = j.replace('%', '')
        Discount.append(ds)
    seller_Name = pf["Seller Name"].values.tolist()
    return [id, brandName, price, Discription, returnPolicy, instalment, Discount, seller_Name]


id, brandName, price, Discription, returnPolicy, instalment, Discount, seller_Name, = loadDataFromFile()


class Form_dashScreen(QDialog):
    def __init__(self):
        super(Form_dashScreen, self).__init__()
        loadUi("Form_dash.ui", self)
        self.btnDashboard.clicked.connect(self.pageDashboard)
        self.btnScrapping.clicked.connect(self.pageScrap)
        self.btnProduct.clicked.connect(self.pageProduct)
        self.btnAlgoritm.clicked.connect(self.pageAlgo)
        self.btnExit.clicked.connect(self.pageExit)

    def pageDashboard(self):
        dash = Form_dashScreen()
        widget.addWidget(dash)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageScrap(self):
        scrp = Form_scrapScreen()
        widget.addWidget(scrp)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageProduct(self):
        pro = Form_prodScreen()
        widget.addWidget(pro)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageAlgo(self):
        newPage = Form_algoScreen()
        widget.addWidget(newPage)
        widget.setCurrentIndex(widget.currentIndex() + 4)

    def pageExit(self):
        widget.close()


class Form_scrapScreen(QDialog):
    def __init__(self):
        super(Form_scrapScreen, self).__init__()
        loadUi("Form_scrap.ui", self)
        completed = 0
        self.btnScrapping.clicked.connect(self.pageScrap)
        self.btnProduct.clicked.connect(self.pageProduct)
        self.btnAlgoritm.clicked.connect(self.pageAlgo)
        self.btnExit.clicked.connect(self.pageExit)
        self.btnDashboard.clicked.connect(self.pageDashboard)
        self.btnStartScrap.clicked.connect(self.startScrapping)
        self.btnStopScrap.clicked.connect(self.stopScrapping)
        self.pBar.setProperty("value", completed)

        self.tableWidget.setRowCount(len(id))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("id"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setItem(
            0, 2, QtWidgets.QTableWidgetItem("Brand Name"))
        self.tableWidget.setItem(
            0, 3, QtWidgets.QTableWidgetItem("Discription"))
        self.tableWidget.setItem(
            0, 4, QtWidgets.QTableWidgetItem("returnPolicy"))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem("Discount"))
        self.tableWidget.setItem(
            0, 6, QtWidgets.QTableWidgetItem("SellerName"))
        self.tableWidget.setItem(
            0, 7, QtWidgets.QTableWidgetItem("instalment"))
        row = 1
        for i in range(len(id)):
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(id[i])))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(price[i])))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(brandName[i])))
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(Discription[i])))
            self.tableWidget.setItem(
                row, 4, QtWidgets.QTableWidgetItem(str(returnPolicy[i])))

            self.tableWidget.setItem(
                row, 5, QtWidgets.QTableWidgetItem(str(Discount[i])))
            self.tableWidget.setItem(
                row, 6, QtWidgets.QTableWidgetItem(str(seller_Name[i])))
            self.tableWidget.setItem(
                row, 7, QtWidgets.QTableWidgetItem(str(instalment[i])))
            row = row + 1

    def pageScrap(self):
        scrap = Form_scrapScreen()
        widget.addWidget(scrap)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageProduct(self):
        pro = Form_prodScreen()
        widget.addWidget(pro)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageAlgo(self):
        newPage = Form_algoScreen()
        widget.addWidget(newPage)
        widget.setCurrentIndex(widget.currentIndex() + 4)

    def stopScrapping(self):
        self.completed = 0

    def scraping(self):
        completed = 0
        pages = [
            'https://www.daraz.pk/catalog/?_keyori=ss&from=input&page=1&q=telivision&spm=a2a0e.searchlist.search.go.746e4cb1og0pJF',
        ]
        driver = webdriver.Chrome(
            executable_path='C:\Program Files (x86)\chromedriver.exe')
        for links in pages:
            lik = self.getlink(links, 'page=1')
            for u in range(1, 50):
                urls = lik.format(u)
                driver.get(urls)
                context = driver.page_source
                soup = BeautifulSoup(context, 'html.parser')
                data = soup.findAll('div', class_="gridItem--Yd0sa")
                for i in data:
                    link = i.find('a', class_='').attrs['href']
                    driver.get('https:{}'.format(link),)
                    context = driver.page_source
                    soup = BeautifulSoup(context, 'html.parser')
                    new = soup.findAll(
                        'div', class_='pdp-block pdp-block__main-information-detail')
                    for n in new:
                        try:
                            datas = str(datetime.now().strftime("%H:%M:%S.%f"))
                            newData = datas.replace(':', '')
                            final = newData.replace('-', '')
                            id.append(final.split('.')[0])
                        except:
                            datas = str(datetime.now().strftime("%H:%M:%S.%f"))
                            newData = datas.replace(':', '')
                            final = newData.replace('-', '')
                            id.append(final.split('.')[0])
                        try:
                            na = n.find(
                                'a', class_='pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link').text
                            if na == 'No Brand':
                                fName = 'Local Brand '
                                brandName.append(fName)
                            else:
                                brandName.append(n.find(
                                    'a', class_='pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link').text)
                        except:
                            brandName.append('not available name ')
                        try:
                            Discription.append(
                                n.find('span', attrs={'pdp-mod-product-badge-title'}).text)
                        except:
                            Discription.append('no description founded')
                        try:
                            price.append(n.find('span', attrs={
                                         'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl'}).text)
                        except:
                            price.append('0')
                        try:
                            try:
                                a3 = ''
                                aa = n.findAll(
                                    'div', class_={'delivery-option-item delivery-option-item_type_returnPolicy7'})
                                if (len(aa) != 0):
                                    for az in aa:
                                        a1 = az.find(
                                            'div', attrs={'delivery-option-item__title'}).text
                                        a2 = az.find(
                                            'div', attrs={'delivery-option-item__subtitle'}).text
                                        a3 = a1+a2
                                    returnPolicy.append(a3)
                                else:
                                    returnPolicy.append(' not available ')
                            except:
                                returnPolicy.append('warranty not available ')
                        except:
                            print(5, 'warranty not available', 3)
                        try:
                            instalment.append(
                                n.find('p', attrs={'item-content'}).text)
                        except:
                            instalment.append('not available ')
                        try:
                            Discount.append(
                                n.find('span', attrs={'pdp-product-price__discount'}).text)
                        except:
                            Discount.append('0')
                        try:
                            sall = n.findAll(
                                'div', class_={'pdp-block pdp-block__delivery-seller'})
                            for s in sall:
                                sellerName = s.find(
                                    'a', class_="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name").text
                                seller_Name.append(sellerName)
                        except:
                            seller_Name.append('Not available')
                            completed = +1
                    pf = pd.DataFrame({'id': id, 'Brand Name': seller_Name, 'price': price, 'Discription': Discription,
                                      'seller Name': seller_Name, 'instalment': instalment, 'Discount': Discount, 'return Policy': returnPolicy, })
                    pf.to_csv('scrapers.csv', index=False, mode='w',)
                    self.pBar.setValue = completed

    def getlink(self, url, data):
        new = url.replace(data, 'page={}')
        return new

    def pageExit(self):
        widget.close()

    def pageDashboard(self):
        dash = Form_dashScreen()
        widget.addWidget(dash)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def startScrapping(self):
        self.scraping()


class Form_prodScreen(QDialog):
    def __init__(self):

        super(Form_prodScreen, self).__init__()
        loadUi("Form_prod.ui", self)
        self.btnDashboard.clicked.connect(self.pageDashboard)
        self.btnScrapping.clicked.connect(self.pageScrap)
        self.btnProduct.clicked.connect(self.pageProduct)
        self.btnAlgoritm.clicked.connect(self.pageAlgo)
        self.btnExit.clicked.connect(self.pageExit)

        self.tableWidget.setRowCount(len(id))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("id"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setItem(
            0, 2, QtWidgets.QTableWidgetItem("Brand Name"))
        self.tableWidget.setItem(
            0, 3, QtWidgets.QTableWidgetItem("Discription"))
        self.tableWidget.setItem(
            0, 4, QtWidgets.QTableWidgetItem("returnPolicy"))
        self.tableWidget.setItem(
            0, 5, QtWidgets.QTableWidgetItem("instalment"))
        self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem("Discount"))
        self.tableWidget.setItem(
            0, 7, QtWidgets.QTableWidgetItem("SellerName"))
        row = 1
        # row = 1
        for i in range(len(id)):
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(id[i])))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(price[i])))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(brandName[i])))
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(Discription[i])))
            self.tableWidget.setItem(
                row, 4, QtWidgets.QTableWidgetItem(str(returnPolicy[i])))
            self.tableWidget.setItem(
                row, 5, QtWidgets.QTableWidgetItem(str(instalment[i])))
            self.tableWidget.setItem(
                row, 6, QtWidgets.QTableWidgetItem(str(Discount[i])))
            self.tableWidget.setItem(
                row, 7, QtWidgets.QTableWidgetItem(str(seller_Name[i])))
            row = row + 1

    def pageScrap(self):
        scrap = Form_scrapScreen()
        widget.addWidget(scrap)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageProduct(self):
        pro = Form_prodScreen()
        widget.addWidget(pro)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageAlgo(self):
        newPage = Form_algoScreen()
        widget.addWidget(newPage)
        widget.setCurrentIndex(widget.currentIndex() + 4)

    def pageExit(self):
        widget.close()

    def pageDashboard(self):
        dash = Form_dashScreen()
        widget.addWidget(dash)
        widget.setCurrentIndex(widget.currentIndex() + 2)


class Form_popUp(QDialog):
    def __init__(self):
        super(Form_popUp, self).__init__()
        loadUi("searching_records.ui", self)
        self.pushButton.clicked.connect(self.pageExit)
        self.tableWidget.setRowCount(len(sid))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("id"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setItem(
            0, 2, QtWidgets.QTableWidgetItem("Brand Name"))
        self.tableWidget.setItem(
            0, 3, QtWidgets.QTableWidgetItem("Discription"))
        self.tableWidget.setItem(
            0, 4, QtWidgets.QTableWidgetItem("returnPolicy"))
        self.tableWidget.setItem(
            0, 5, QtWidgets.QTableWidgetItem("instalment"))
        self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem("Discount"))
        self.tableWidget.setItem(
            0, 7, QtWidgets.QTableWidgetItem("SellerName"))
        row = 1
        for i in range(len(sid)):
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(sid[i])))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(sprice[i])))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(sbrandName[i])))
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(sDiscription[i])))
            self.tableWidget.setItem(
                row, 4, QtWidgets.QTableWidgetItem(str(sreturnPolicy[i])))
            self.tableWidget.setItem(
                row, 5, QtWidgets.QTableWidgetItem(str(sinstalment[i])))
            self.tableWidget.setItem(
                row, 6, QtWidgets.QTableWidgetItem(str(sDiscount[i])))
            self.tableWidget.setItem(
                row, 7, QtWidgets.QTableWidgetItem(str(sseller_Name[i])))
            row = row + 1

    def pageExit(self):
        algo = Form_algoScreen()
        widget.addWidget(algo)
        widget.setCurrentIndex(widget.currentIndex()+2)


class Form_algoScreen(QDialog):
    def __init__(self):
        super(Form_algoScreen, self).__init__()
        loadUi("Form_algo.ui", self)
        comboBox_4l = ["Ascending", 'Descending']
        comboBox_5l = ["id", 'brand name/Product name', 'discount', 'All',
                       'price', 'seller Name']
        sortingAlgo = ["Bubble Sort", 'Insertion Sort',
                       'Merge Sort', 'Selection Sort','Quick Sort',]
        searchingAlgo = ["linear search", "Binary search"]
        searchBy = ['seller Name', "brandName", 'price', 'Discount']
        sid = id
        sbrandName = brandName
        sprice = price
        sDiscription = Discription
        sreturnPolicy = returnPolicy
        sinstalment = instalment
        sDiscount = Discount
        sseller_Name = seller_Name

        self.btnScrapping.clicked.connect(self.pageScrap)
        self.btnDashboard.clicked.connect(self.pageDashboard)
        self.btnApply.clicked.connect(self.applyAlgorithm)
        self.btnProduct.clicked.connect(self.pageProduct)
        self.btnAlgoritm.clicked.connect(self.pageAlgo)
        self.btnExit.clicked.connect(self.pageExit)
        self.comboBox.addItems(sortingAlgo)
        self.comboBox_2.addItems(searchingAlgo)
        self.comboBox_3.addItems(searchBy)
        self.comboBox_4.addItems(comboBox_4l)
        self.comboBox_5.addItems(comboBox_5l)
        self.tableWidget.setRowCount(len(id))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("id"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setItem(
            0, 2, QtWidgets.QTableWidgetItem("Brand Name"))
        self.tableWidget.setItem(
            0, 3, QtWidgets.QTableWidgetItem("Discription"))
        self.tableWidget.setItem(
            0, 4, QtWidgets.QTableWidgetItem("returnPolicy"))
        self.tableWidget.setItem(
            0, 5, QtWidgets.QTableWidgetItem("instalment"))
        self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem("Discount"))
        self.tableWidget.setItem(
            0, 7, QtWidgets.QTableWidgetItem("SellerName"))
        row = 1
        for i in range(len(id)):
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(id[i])))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(price[i])))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(brandName[i])))
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(Discription[i])))
            self.tableWidget.setItem(
                row, 4, QtWidgets.QTableWidgetItem(str(returnPolicy[i])))
            self.tableWidget.setItem(
                row, 5, QtWidgets.QTableWidgetItem(str(instalment[i])))
            self.tableWidget.setItem(
                row, 6, QtWidgets.QTableWidgetItem(str(Discount[i])))
            self.tableWidget.setItem(
                row, 7, QtWidgets.QTableWidgetItem(str(seller_Name[i])))
            row = row + 1

    def pageScrap(self):
        scrap = Form_scrapScreen()
        widget.addWidget(scrap)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageProduct(self):
        pro = Form_prodScreen()
        widget.addWidget(pro)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def pageAlgo(self):
        newPage = Form_algoScreen()
        widget.addWidget(newPage)
        widget.setCurrentIndex(widget.currentIndex() + 4)

    def pageExit(self):
        widget.close()

    def applyAlgorithm(self):
        popUp = Form_popUp()
        arr = []
        get_Sort = self.comboBox.currentText()
        get_By_Order = self.comboBox_4.currentText()
        get_Column_For_Sort = self.comboBox_5.currentText()
        print(get_By_Order, get_Column_For_Sort, get_Sort)
        if (get_Column_For_Sort == "brand name/Product name"):
            arr = brandName
            print(get_Sort)
        if (get_Sort == 'Bubble Sort'):
            if get_By_Order == "Ascending":
                if (get_Column_For_Sort == 'id'):
                    arr = id
                    # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'price'):
                    arr = price
                    # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'seller Name'):
                    arr = seller_Name
                    # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'discount'):
                    arr = Discount
                    # new_arr = BubbleSort(arr, 'Ascending')
                # if ('All'):
                    # get_Column_For_Sort==
                print(new_arr, 10)
            else:
                if (get_Column_For_Sort == 'id'):
                    arr = id
                    # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'price'):
                    arr = price
                    # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'seller Name'):
                    arr = seller_Name
                    # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'discount'):
                    arr = Discount
                    # new_arr = BubbleSort(arr, 'Descending')
                print(new_arr, 11)
        elif (get_Sort == 'Insertion Sort'):
            if get_By_Order == "Ascending":
                if (get_Column_For_Sort == 'id'):
                    arr = id
                new_arr = insertionSort(arr, 'Ascending')
                # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'price'):
                    arr = price
                new_arr = insertionSort(arr, 'Ascending')
                # new_arr = BubbleSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'seller Name'):
                    arr = seller_Name
                new_arr = insertionSort(arr, 'Ascending')
                if (get_Column_For_Sort == 'discount'):
                    arr = Discount
                new_arr = insertionSort(arr, 'Ascending')
            else:
                if (get_Column_For_Sort == 'id'):
                    arr = id
                    new_arr = insertionSort(arr, 'Descending')
                if (get_Column_For_Sort == 'price'):
                    arr = price
                    new_arr = insertionSort(arr, 'Descending')
                if (get_Column_For_Sort == 'seller Name'):
                    arr = seller_Name
                    new_arr = insertionSort(arr, 'Descending')
                if (get_Column_For_Sort == 'discount'):
                    arr = Discount
                    new_arr = insertionSort(arr, 'Descending')
        elif (get_Sort == 'Selection Sort'):
            if get_By_Order == "Ascending":
                new_arr = SelectionSort(arr, 'Ascending')
                print(new_arr, 30)
            else:
                new_arr = SelectionSort(arr, 'Descending')
                print(new_arr, 31)
        elif (get_Sort == 'Merge Sort'):
            if get_By_Order == "Ascending":
                if (get_Column_For_Sort=='id'):
                    arr = id
                if (get_Column_For_Sort=='price'):
                    arr = price
                if (get_Column_For_Sort=='seller Name'):
                    arr = seller_Name
                if (get_Column_For_Sort=='discount'):
                    arr = Discount
                print(new_arr, 40)
            else:
                if (get_Column_For_Sort=='id'):
                    arr = id
                # new_arr = MerageSort(arr, 'Descending')
                if (get_Column_For_Sort=='price'):
                    arr = price
                # new_arr = MerageSort(arr, 'Descending')
                if (get_Column_For_Sort=='seller Name'):
                    arr = seller_Name
                # new_arr = MerageSort(arr, 'Descending')
                if (get_Column_For_Sort=='discount'):
                    arr = Discount
                # new_arr = MerageSort(arr, 'Descending')
                print(new_arr, 41)

        # search Algorithm
        get_Search = self.comboBox_2.currentText()
        get_SearchBy = self.comboBox_3.currentText()
        search = self.SVEdilt.text()
        sid.clear(), sbrandName.clear(), sDiscount.clear(), sDiscription.clear(
        ), sprice.clear(), sinstalment.clear(), sreturnPolicy.clear(), sseller_Name.clear()
        if (get_Search == "linear search"):
            if get_SearchBy == 'brandName' and get_Search == "linear search" and search != '':
                arr = LinearSarch(brandName, search)
                for i in range(0, len(arr)):
                    sid.append(id[arr[i]])
                    sbrandName.append(brandName[arr[i]])
                    sDiscount.append(Discount[arr[i]])
                    sDiscription.append(Discription[arr[i]])
                    sseller_Name.append(seller_Name[arr[i]])
                    sinstalment.append(instalment[arr[i]])
                    sprice.append(price[arr[i]])
                    sreturnPolicy.append(returnPolicy[arr[i]])
                widget.addWidget(popUp)
                widget.setCurrentIndex(widget.currentIndex() + 2)

            elif (get_SearchBy == 'seller Name' and get_Search == "linear search" and search != ''):
                arr = LinearSarch(seller_Name, search)
                for i in range(0, len(arr)):
                    sid.append(id[arr[i]])
                    sbrandName.append(brandName[arr[i]])
                    sDiscount.append(Discount[arr[i]])
                    sDiscription.append(Discription[arr[i]])
                    sseller_Name.append(seller_Name[arr[i]])
                    sinstalment.append(instalment[arr[i]])
                    sprice.append(price[arr[i]])
                    sreturnPolicy.append(returnPolicy[arr[i]])
                widget.addWidget(popUp)
                widget.setCurrentIndex(widget.currentIndex() + 2)

            elif (get_SearchBy == 'price' and get_Search == "linear search" and search != ''):
                arr = LinearSarch(price, search)
                for i in range(0, len(arr)):
                    sid.append(id[arr[i]])
                    sbrandName.append(brandName[arr[i]])
                    sDiscount.append(Discount[arr[i]])
                    sDiscription.append(Discription[arr[i]])
                    sseller_Name.append(seller_Name[arr[i]])
                    sinstalment.append(instalment[arr[i]])
                    sprice.append(price[arr[i]])
                    sreturnPolicy.append(returnPolicy[arr[i]])
                widget.addWidget(popUp)
                widget.setCurrentIndex(widget.currentIndex() + 2)
            elif (get_SearchBy == 'Discount' and get_Search == "linear search" and search != ''):
                arr = LinearSarch(Discount, search)
                for i in range(0, len(arr)):
                    sid.append(id[arr[i]])
                    sbrandName.append(brandName[arr[i]])
                    sDiscount.append(Discount[arr[i]])
                    sDiscription.append(Discription[arr[i]])
                    sseller_Name.append(seller_Name[arr[i]])
                    sinstalment.append(instalment[arr[i]])
                    sprice.append(price[arr[i]])
                    sreturnPolicy.append(returnPolicy[arr[i]])
                widget.addWidget(popUp)
                widget.setCurrentIndex(widget.currentIndex() + 2)
            elif (get_SearchBy == "none" or get_Search == "none" or search != ''):
                # self.btnApply.clicked.connect(self.messageBox)
                print("none")
                return
        else:
            if get_SearchBy == 'brandName' and get_Search == "Binary search" and search != '':
                arr = BinarySearch(brandName, search)
                for i in range(0, len(arr)):
                    sid.append(id[arr[i]])
                    sbrandName.append(brandName[arr[i]])
                    sDiscount.append(Discount[arr[i]])
                    sDiscription.append(Discription[arr[i]])
                    sseller_Name.append(seller_Name[arr[i]])
                    sinstalment.append(instalment[arr[i]])
                    sprice.append(price[arr[i]])
                    sreturnPolicy.append(returnPolicy[arr[i]])
                widget.addWidget(popUp)
                widget.setCurrentIndex(widget.currentIndex() + 2)

            if get_SearchBy == 'brandName' and get_Search == "Binary search" and search != '':
                arr = BinarySearch(brandName, search)
                for i in range(0, len(arr)):
                    sid.append(id[arr[i]])
                    sbrandName.append(brandName[arr[i]])
                    sDiscount.append(Discount[arr[i]])
                    sDiscription.append(Discription[arr[i]])
                    sseller_Name.append(seller_Name[arr[i]])
                    sinstalment.append(instalment[arr[i]])
                    sprice.append(price[arr[i]])
                    sreturnPolicy.append(returnPolicy[arr[i]])
                widget.addWidget(popUp)
                widget.setCurrentIndex(widget.currentIndex() + 2)

            if get_SearchBy == 'brandName' and get_Search == "Binary search" and search != '':
                arr = BinarySearch(brandName, search)
                for i in range(0, len(arr)):
                    sid.append(id[arr[i]])
                    sbrandName.append(brandName[arr[i]])
                    sDiscount.append(Discount[arr[i]])
                    sDiscription.append(Discription[arr[i]])
                    sseller_Name.append(seller_Name[arr[i]])
                    sinstalment.append(instalment[arr[i]])
                    sprice.append(price[arr[i]])
                    sreturnPolicy.append(returnPolicy[arr[i]])
                widget.addWidget(popUp)
                widget.setCurrentIndex(widget.currentIndex() + 2)

# search Algorithm
    # def messageBox(self):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setText("This is a message box")
    #     msg.setInformativeText("This is additional information")
    #     msg.setWindowTitle("MessageBox demo")
    #     msg.setDetailedText("The details are as follows:")
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def pageDashboard(self):
        dash = Form_dashScreen()
        widget.addWidget(dash)
        widget.setCurrentIndex(widget.currentIndex() + 2)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
popUp = Form_popUp()
prod = Form_prodScreen()
scrap = Form_scrapScreen()
algo = Form_algoScreen()
dash = Form_dashScreen()
widget.addWidget(dash)
widget.setFixedWidth(1230)
widget.setFixedHeight(720)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Page doesn't exist")
