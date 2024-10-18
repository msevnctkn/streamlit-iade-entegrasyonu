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
        grossAmount     = i["grossAmount"]
        totalDiscount   = i["totalDiscount"]
        totalTyDiscount = i["totalTyDiscount"]
        taxNumber       = i["taxNumber"]

        ###

        # FATURA ADRESİ İLE İLGİLİ BİLGİLER ESGEÇİLMİŞTİR.
        customerFirstName       = i["customerFirstName"]
        customerEmail           = i["customerEmail"]
        customerId              = i["customerId"]
        customerLastName        = i["customerLastName"]
        id                      = i["id"]
        cargoTrackingNumber     = i["cargoTrackingNumber"]
        # cargoTrackingLink       = i["cargoTrackingLink"]
        # cargoSenderNumber       = i["cargoSenderNumber"]
        cargoProviderName       = i["cargoProviderName"]
    
        for j in i["lines"]:
            quantity                = j["quantity"]
            salesCampaignId         = j["salesCampaignId"]
            productSize             = j["productSize"]
            merchantSku             = j["merchantSku"]
            productName             = j["productName"]
            productCode             = j["productCode"]
            merchantId              = j["merchantId"]
            amount                  = j["amount"]
            discount                = j["discount"]
            tyDiscount              = j["tyDiscount"]
            for k in j["discountDetails"]:
                lineItemPrice           = k["lineItemPrice"]
                lineItemDiscount        = k["lineItemDiscount"]
                lineItemTyDiscount      = k["lineItemTyDiscount"]
            
            currencyCode            = j["currencyCode"]
            lines_id                = j["id"]
            sku                     = j["sku"]
            vatBaseAmount           = j["vatBaseAmount"]
            barcode                 = j["barcode"]
            orderLineItemStatusName = j["orderLineItemStatusName"]
            price                   = j["price"]
            fastDeliveryOptions     = j["fastDeliveryOptions"]
            #tcIdentityNumber        = j["tcIdentityNumber"]

            
        # st.write(i)
        # st.write(customerFirstName, customerLastName)
        df = pd.DataFrame.from_dict(    {"Sipariş Numarası": [str(orderNumber)],
                                             
                                                "Müşteri Adı ": [customerFirstName],
                                                "Müşteri Soyadı": [customerLastName],
                                                "Barkod": [barcode],
                                                "Ürün Adı": [productName],
                                                "Kargo Adı": [cargoProviderName],
                                                "Kargo Kodu": [str(cargoTrackingNumber)],
                                             
                                                #"İade Sebebi": [None for i in range(3)],

                                                })

        st.write(df)


        # currencyCode            = 
        # packageHistories        = 
        # shipmentPackageStatus   = 
        # status                  = 
        # deliveryType            = 
        # timeSlotId              = 
        # estimatedDeliveryStartDate = 
        # estimatedDeliveryEndDate   = 
        # totalPrice                 = 
        # deliveryAddressType        = 
        # agreedDeliveryDate         = 
        # fastDelivery               = 
        # originShipmentDate         = 
        # lastModifiedDate           = 
        # commercial                 = 
        # fastDeliveryType           = 
        # deliveredByService         = 
        # extendedAgreedDeliveryDate =
        # agreedDeliveryExtensionEndDate = 
        # agreedDeliveryExtensionStartDate = 
        # warehouseId = 
        # groupDeal = 
        # micro = 
        # giftBoxRequested = 
        # _3pByTrendyol =
        # containsDangerousProduct = 


