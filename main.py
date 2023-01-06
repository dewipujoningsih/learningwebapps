import pandas as pd
import numpy as np
import streamlit as st
st.title("Aplikasi Penghitungan Molaritas")
bobot=st.number_input("Masukkan bobot")
volume=st.number_input("Masukkan volume")
mr=st.number_input("Masukkan nilai massa relatif")
tombol=st.button("Hitung Molaritas")
if tombol:
    nilai=bobot/(volume*mr)
    st.success(f"Nilai Molaritas adalah:",nilai)