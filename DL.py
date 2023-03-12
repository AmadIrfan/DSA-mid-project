from BL import *
import pandas as pd
from sorting_Arr import *
dataList = []


@staticmethod
def loadDataFromFile():
    price = []
    pf = pd.read_csv("scrap.csv")
    id = pf["id"].values.tolist()
    print(id)
    brandName = pf["Brand Name"].values.tolist()
    pri = pf["price"].values.tolist()
    for i in pri:
        new = i.replace('Rs.', '')
        price.append(new)
    Discription = pf["Discription"].values.tolist()
    returnPolicy = pf["Warranty"].values.tolist()
    instalment = pf["instalment"].values.tolist()
    Discount = pf["Discount"].values.tolist()
    seller_Name = pf["Seller Name"].values.tolist()
    for o in range(len(id)):
        obj = product(
            
            id[o], brandName[o], price[o], Discription[o], returnPolicy[o], instalment[o], Discount[o], seller_Name
        )
        dataList.append(obj)
