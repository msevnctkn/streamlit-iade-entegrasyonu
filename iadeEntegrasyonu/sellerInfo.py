import streamlit as st
from trendyol_sdk.api import TrendyolApiClient
from trendyol_sdk.services import ReturnedOrdersIntegrationService, OrderIntegrationService



class OMASARMATUR_API:
    # MAĞAZA API KEYLERİ
    TRENDYOL_API_KEY = "f6KXBycO6FJIC4zUPDMf"
    TRENDYOL_API_SECRET = "de1xl3aAjUBQF1A1nwin"
    TRENDYOL_SELLER_ID = "225237"


    api = TrendyolApiClient(api_key=TRENDYOL_API_KEY,
                        api_secret=TRENDYOL_API_SECRET,
                        supplier_id=TRENDYOL_SELLER_ID)

    iadeler = ReturnedOrdersIntegrationService(api)
    siparisler = OrderIntegrationService(api)