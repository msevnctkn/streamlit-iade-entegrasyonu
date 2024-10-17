from sellerInfo import OMASARMATUR_API
import streamlit as st
import pandas as pd
import __time as t
import sys



def WaitingShipmentPackages():
    bekleyenSiparisler = OMASARMATUR_API.siparisler.get_shipment_packages(filter_params={"status": "Picking"})
    bekleyenSiparisSayisi = bekleyenSiparisler["totalElements"]
    st.subheader(f"Bekleyen Sipariş Sayısı: {bekleyenSiparisSayisi}")
    for i in bekleyenSiparisler["content"]:
        ### TESLİMAT ADRESİ İLE İLGİLİ BİLGİLER
        id              = i["shipmentAddress"]["id"]
        firstName       = i["shipmentAddress"]["firstName"]
        lastName        = i["shipmentAddress"]["lastName"]
        company         = i["shipmentAddress"]["company"]
        address1        = i["shipmentAddress"]["address1"]
        address2        = i["shipmentAddress"]["address2"]
        city            = i["shipmentAddress"]["city"]
        cityCode        = i["shipmentAddress"]["cityCode"]
        district        = i["shipmentAddress"]["district"]
        districtId      = i["shipmentAddress"]["districtId"]
        postalCode      = i["shipmentAddress"]["postalCode"]
        countryCode     = i["shipmentAddress"]["countryCode"]
        neighborhoodId  = i["shipmentAddress"]["neighborhoodId"]
        neighborhood    = i["shipmentAddress"]["neighborhood"]
        phone           = i["shipmentAddress"]["phone"]
        fullName        = i["shipmentAddress"]["fullName"]
        fullAddress     = i["shipmentAddress"]["fullAddress"]
        orderNumber     = i["orderNumber"]
        ###

        # FATURA ADRESİ İLE İLGİLİ BİLGİLER ESGEÇİLMİŞTİR.
        customerFirstName       = i["customerFirstName"]
        customerEmail           = i["customerEmail"]
        customerId              = i["customerId"]
        customerLastName        = i["customerLastName"]
        id                      = i["id"]
        # cargoTrackingNumber     = i["cargoTrackingNumber"]
        # cargoTrackingLink       = i["cargoTrackingLink"]
        # cargoSenderNumber       = i["cargoSenderNumber"]
        # cargoProviderName       = i["cargoProviderName"]

        st.write(customerFirstName, customerLastName)
        st.write(sys.version)