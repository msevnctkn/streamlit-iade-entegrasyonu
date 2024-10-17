
from trendyol_sdk.api import TrendyolApiClient
from trendyol_sdk.services import ReturnedOrdersIntegrationService
from dataframes import waitingInActionDataframe
import streamlit as st
import pandas as pd
import __time as t
import streamlit_antd_components as stc
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from sellerInfo import OMASARMATUR_API


iadeler = OMASARMATUR_API.iadeler

# bütün iade kargolar ()
def fetchAllReturns():
    tum_iadeler = iadeler.get_shipment_packages(filter_params={})
    for i in tum_iadeler["content"]:
        for j in i["items"]:
            st.write(j["orderLine"]["productName"])


# talep oluşturulan - müşteri iade butonuna tıkladığı anda oluşur.-
def fetchCreatedReturns():
    tum_iadeler = iadeler.get_shipment_packages(filter_params={"claimItemStatus":"Created"})
    for i in tum_iadeler["content"]:
        for j in i["items"]:
            st.write(j["orderLine"]["productName"])

# aksiyonda bekleyen kargolar
def fetchWaitingInAction():
    aksiyondaBekleyen = iadeler.get_shipment_packages(filter_params={"claimItemStatus":"WaitingInAction"})
    aksiyondaBekleyenIadeSayisi = aksiyondaBekleyen["totalElements"]
    st.write("Aksiyonda Bekleyen İade Sayısı: ", aksiyondaBekleyenIadeSayisi)
  

    while aksiyondaBekleyenIadeSayisi > 0:
        for i in aksiyondaBekleyen["content"]:
            
            orderNumber = i["orderNumber"]
            orderDate = i["orderDate"]
            claimDate = i["claimDate"]
            customerFirstName = i["customerFirstName"]
            customerLastName = i["customerLastName"]
            cargoProviderName = i["cargoProviderName"]
            cargoTrackingNumber = i["cargoTrackingNumber"]
            cargoTrackingLink = i["cargoTrackingLink"]
            
            lastModifiedDate = i["lastModifiedDate"]
            automaticAcceptDate = i["lastModifiedDate"] + 172800000 # 172800000 ms = 2 days


            #REDDEDİLEN PAKETLE İLGİLİ BİR DETAY YOK. 
            # cargoTrackingNumber2 = i["rejectedpackageinfo"]["cargoTrackingNumber"]
            # cargoSenderNumber = i["rejectedpackageinfo"]["cargoSenderNumber"]
            # cargoProviderName2 = i["rejectedpackageinfo"]["cargoProviderName"]
            # packageid = i["rejectedpackageinfo"]["packageid"]
            # items = i["rejectedpackageinfo"]["items"][0]

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
                    resolved = k["resolved"]
                    autoAccepted = k["autoAccepted"]
                    acceptedBySeller = k["acceptedBySeller"]


            df = pd.DataFrame.from_dict(    {"Sipariş Numarası": [str(orderNumber)],
                                                "Sipariş Tarihi": [t.ms_to_datetime(int(orderDate))],
                                                "İade Tarihi": [t.ms_to_datetime(int(claimDate))],
                                                "Müşteri Adı ": [customerFirstName],
                                                "Müşteri Soyadı": [customerLastName],
                                                "Barkod": [barcode],
                                                "Ürün Adı": [productName],
                                                "Kargo Adı": [cargoProviderName],
                                                "Kargo Kodu": [str(cargoTrackingNumber)],
                                                "Kargo Takip Link": [cargoTrackingLink],
                                                #"İade Sebebi": [None for i in range(3)],
                                                "Mağazaya Teslim Tarihi" : [t.ms_to_datetime(int(lastModifiedDate))],
                                                #"Durum": [None for i in range(3)],
                                                "Otomatik Onay Tarihi" : [t.ms_to_datetime(int(automaticAcceptDate))],
                                                "id" : [id],
                                                "orderLineItemId" : [orderLineItemId],
                                                "customerClaimItemReasonID" : [customerClaimItemReasonID],
                                                "customerClaimItemReasonNAME" : [customerClaimItemReasonNAME],
                                                "customerClaimItemReasonExternalReasonId" : [customerClaimItemReasonExternalReasonId],
                                                "customerClaimItemReasonCODE" : [customerClaimItemReasonCODE],
                                                "trendyolClaimItemReasonID" : [trendyolClaimItemReasonID],
                                                "trendyolClaimItemReasonNAME" : [trendyolClaimItemReasonNAME],
                                                "trendyolClaimItemReasonExternalReasonId" :[trendyolClaimItemReasonExternalReasonId],
                                                "trendyolClaimItemReasonCODE" : [trendyolClaimItemReasonCODE],
                                                "autoApproveDate" : [t.ms_to_datetime(autoApproveDate)],
                                                "note" : [note],
                                                #"resolved" : [resolved],
                                                #"autoAccepted" : [autoAccepted],
                                                #"acceptedBySeller" : [acceptedBySeller]

                                                })
        

            gd = GridOptionsBuilder.from_dataframe(df)
            gd.configure_pagination(enabled=True)
            gd.configure_default_column(editable=True, groupable=True)
            gd.configure_selection(use_checkbox=True)
            gridoptions = gd.build()

            gridTable = AgGrid(df, gridOptions=gridoptions, update_mode=GridUpdateMode.SELECTION_CHANGED, height=500, allow_unsafe_jscode=True, theme="alpine")
            sel_row = gridTable["selected_rows"]
            # st.write(sel_row)
            # st.session_state["df.note"] = df["note"]
            # st.write(df["note"])

            #session state oluştur note'un içine "ONAYLA" yazılması lazım, session state ile bunu al. onaylayı görürse -> id çeksin. Çekilen id ile trendyoldan devam et.
    else:
        st.subheader("Aksiyonda Bekleyen İade yok.")


# onaylanan iadeler
def fetchAccepted():
    pass

# reddedilen iadeler
def fetchRejected():
    pass


# ihtilaftaki iadeler
def fetchUnresolved():
    pass

# iadesi iptal edilen kargolar
def fetchCancelled():
    pass


