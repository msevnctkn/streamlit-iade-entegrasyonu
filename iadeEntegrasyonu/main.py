#.streamlit/secrets.toml

import streamlit as st

st.set_page_config(layout = "wide", page_title="ÖMAS KONSEPT İADE ENTEGRASYONU")
from trendyol_iade_entegrasyonu import *
from analiz import fetchAnalysis
from bekleyen_siparisler import WaitingShipmentPackages
st.header("ÖMAS KONSEPT PANEL")

sidebarButton = st.sidebar.selectbox("Menü", ["Trendyol İadeler",
                                              "Hepsiburada İadeler",
                                              "Stoklar",
                                              "Saat Siparişleri",
                                              "Serbest Alan"])

if sidebarButton == "Trendyol İadeler":
#İADELERİ GETİR.
    st.subheader("Trendyol İade Entegrasyonu")
    st.columns(9)

    col10, col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(10)

    with col10:

        bekleyenSiparisler = st.button("Bekleyen Siparişler")
        

    with col1:
        
        allReturnsButton = st.button("Bütün İadeler")
        if allReturnsButton:
            st.write(fetchAllReturns())
    with col2:
        createdReturnsButton = st.button("Talep Oluşturulan")
        if createdReturnsButton:
            fetchCreatedReturns()

    with col3:
        st.button("Kargoya Verilen")
        

    with col4:
        waitingInActionButton = st.button("Aksiyonda Bekleyen")

    with col5:
        acceptedButton = st.button("Onaylanan")
        if acceptedButton:
            st.write(fetchAccepted())

    with col6:
        rejectedButton = st.button("Reddedilen")
        if rejectedButton:
            st.write(fetchRejected())

    with col7:
        analysisButton = st.button("Analiz")
        

    with col8:
        unresolvedButton = st.button("İhtilaflı")
        if unresolvedButton:
            st.write(fetchUnresolved)

    with col9:
        cancelledButton = st.button("İadesi İptal Edilen")
        if cancelledButton:
            st.write(fetchCancelled())


###########################################################################








    if bekleyenSiparisler:
        WaitingShipmentPackages()


    if waitingInActionButton:
        fetchWaitingInAction()

    if analysisButton:
            fetchAnalysis()