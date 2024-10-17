import pandas as pd
import streamlit as st
class DATAFRAME:

    
    _dataframe = {"Sipariş Numarası": [],
                 "Sipariş Tarihi": [],
                 "İade Tarihi": [],
                 "Müşteri Adı ": [],
                 "Müşteri Soyadı": [],
                 "Barkod": [],
                 "Ürün Adı": [],
                 "Kargo Adı": [],
                 "Kargo Kodu": [],
                 "Kargo Takip Link": [],
                 #"İade Sebebi": [None for i in range(3)],
                 "Mağazaya Teslim Tarihi" : [],
                 #"Durum": [None for i in range(3)],
                 "Otomatik Onay Tarihi" : [],
                }

class allReturnsDataframe(DATAFRAME):
    pass

class createdReturnsDataframe (DATAFRAME):
    pass

class kargoyaVerilenDataframe(DATAFRAME):
    pass

class waitingInActionDataframe(DATAFRAME):
    pass

class acceptedDataframe(DATAFRAME):
    pass

class rejecteDataframe(DATAFRAME):
    pass

class analysisDataframe(DATAFRAME):
    pass

class unresolvedDataframe(DATAFRAME):
    pass

class cancelledDataframe(DATAFRAME):
    pass
