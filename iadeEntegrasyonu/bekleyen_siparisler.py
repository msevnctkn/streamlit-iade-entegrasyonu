from sellerInfo import OMASARMATUR_API
import streamlit as st
import pandas as pd
import __time as t




def WaitingShipmentPackages():
    bekleyenSiparisler = OMASARMATUR_API.siparisler
    st.write(bekleyenSiparisler.get_shipment_packages(filter_params={"status": "orderDate"}))
    st.write(bekleyenSiparisler.get_shipment_packages(filter_params={"status": "Created"}))
    st.write(bekleyenSiparisler.get_shipment_packages(filter_params={"status": "Picking"}))
    st.write(bekleyenSiparisler.get_shipment_packages(filter_params={"status": "Created"}))