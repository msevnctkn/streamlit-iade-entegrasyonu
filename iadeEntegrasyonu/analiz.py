from trendyol_sdk.api import TrendyolApiClient
from trendyol_sdk.services import ReturnedOrdersIntegrationService
from sellerInfo import OMASARMATUR_API
import streamlit as st
import pandas as pd
import __time as t

# analizdeki kargolar
def fetchAnalysis():
    analizdeBekleyen = OMASARMATUR_API.iadeler.get_shipment_packages(filter_params={"claimItemStatus":"InAnalysis"})
    #st.write(analizdeBekleyen)
    analizdeBekleyenIadeSayisi = analizdeBekleyen["totalElements"]
    
    if analizdeBekleyenIadeSayisi > 0:
        for i in analizdeBekleyen["content"]:
            orderNumber = i["orderNumber"]
            orderDate = i["orderDate"]
            claimDate = i["claimDate"]
            customerFirstName = i["customerFirstName"]
            customerLastName = i["customerLastName"]
            cargoProviderName = i["cargoProviderName"]
            cargoTrackingNumber = i["cargoTrackingNumber"]
            cargoTrackingLink = i["cargoTrackingLink"]
            
            lastModifiedDate = i["lastModifiedDate"]
            automaticAcceptDate = i["lastModifiedDate"] + 2073600000 # 2073600000 ms = 24 days
            for j in i["items"]:
                barcode = j["orderLine"]["barcode"]
                productName = j["orderLine"]["productName"]

            
                for k in j["claimItems"]:
                
                    id = k["id"]
                    orderLineItemId = k["orderLineItemId"]
                    customerClaimItemReasonID = k["customerClaimItemReason"]["id"] #iade nedeni kodu ----->  iadeyi onaylamak için kullanılır
                    customerClaimItemReasonNAME = k["customerClaimItemReason"]["name"]    # müşteri iade nedeni
                    customerClaimItemReasonExternalReasonId = k["customerClaimItemReason"]["externalReasonId"]  
                    customerClaimItemReasonCODE = k["customerClaimItemReason"]["code"]
                    trendyolClaimItemReasonID = k["trendyolClaimItemReason"]["id"] #trendyol iade nedeni kodu
                    trendyolClaimItemReasonNAME = k["trendyolClaimItemReason"]["name"]
                    trendyolClaimItemReasonExternalReasonId = k["trendyolClaimItemReason"]["externalReasonId"]
                    trendyolClaimItemReasonCODE = k["trendyolClaimItemReason"]["code"]
                    autoApproveDate = k["autoApproveDate"]
                    note = k["note"]
                    customerNote = k["customerNote"]
                    resolved = k["resolved"]
                    autoAccepted = k["autoAccepted"]
                    acceptedBySeller = k["acceptedBySeller"]
                    
            df = pd.DataFrame.from_dict(    {
                
                "Sipariş Numarası": [str(orderNumber)],
                    "Sipariş Tarihi": [t.ms_to_datetime(int(orderDate)).strftime("%d-%B-%Y %H:%M")],
                    "İade Tarihi": [t.ms_to_datetime(int(claimDate)).strftime("%d-%B-%Y %H:%M")],
                    "Müşteri Adı ": [customerFirstName],
                    "Müşteri Soyadı": [customerLastName],
                    "Barkod": [barcode],
                    "Ürün Adı": [productName],
                    "İade Nedeni" : [customerClaimItemReasonNAME],
                    "Müşteri Notu": customerNote,
                    "Otomatik Onay Tarihi" : [t.ms_to_datetime(int(automaticAcceptDate)).strftime("%d-%B-%Y %H:%M")],
                    #"Otomatik Onay Tarihi 1" : [t.ms_to_datetime(autoApproveDate).strftime("%d-%B-%Y %H:%M")],
                    "Kargo Adı": [cargoProviderName],
                    "Kargo Kodu": [str(cargoTrackingNumber)],
                    "Kargo Takip Link": [cargoTrackingLink],
                    #"İade Sebebi": [None for i in range(3)],
                    "Mağazaya Teslim Tarihi" : [t.ms_to_datetime(int(lastModifiedDate)).strftime("%d-%B-%Y %H:%M")],
                    #"Durum": [None for i in range(3)],
                    
                    # "id" : [id],
                    # "orderLineItemId" : [orderLineItemId],
                    # "customerClaimItemReasonID" : [customerClaimItemReasonID],
                    
                    # "customerClaimItemReasonExternalReasonId" : [customerClaimItemReasonExternalReasonId],
                    # "customerClaimItemReasonCODE" : [customerClaimItemReasonCODE],
                    # "trendyolClaimItemReasonID" : [trendyolClaimItemReasonID],
                    # "trendyolClaimItemReasonNAME" : [trendyolClaimItemReasonNAME],
                    # "trendyolClaimItemReasonExternalReasonId" :[trendyolClaimItemReasonExternalReasonId],
                    # "trendyolClaimItemReasonCODE" : [trendyolClaimItemReasonCODE],
                    
                    # "note" : [note],
                    #"resolved" : [resolved],
                    #"autoAccepted" : [autoAccepted],
                    #"acceptedBySeller" : [acceptedBySeller]

                                                })
            st.write(df)
    else:
        st.subheader("Analizde Bekleyen İade Yok")