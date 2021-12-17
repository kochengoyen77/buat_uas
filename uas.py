#IMPORT AWAL
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
import matplotlib.colors as colors
import streamlit as st
from fileHandler import csvHandler,jsonHandler

#READ DATA JSON
with open("kode_negara_lengkap.json", "r") as read_file:
    data = json.load(read_file)
# for i in data:
#     print(type(i))
print(data[0])
dfJ = pd.DataFrame(data)

#READ DATA CSV
csv = pd.read_csv("produksi_minyak_mentah.csv")
df = pd.DataFrame(csv)
print(df)


#MEMBUAT DATA FRAME 
st.title('Data Produksi Minyak Mentah')
st.header('UAS Pemrograman Komputer')
st.header('Tan Manuel Widjaja - 12220012')
ch_ = csvHandler('produksi_minyak_mentah.csv')
jh_ = jsonHandler('kode_negara_lengkap.json')
csv_ = ch_.dataFrame
df_info = jh_.dataFrame
negara_li = df_info['name'].tolist()

#LETAK OUTPUT
st.sidebar.title("Settings")
st.sidebar.header('Pengaturan Jumlah Produksi Per Bulan')
left_col, mid_col, right_col = st.columns(3)
negara = st.sidebar.selectbox('Pilih negara : ',negara_li) 

kode = df_info[df_info['name']==negara]['alpha-3'].tolist()[0]
color = ['red', 'green', 'black']
st.sidebar.write('Kode negara : ',kode, color = "green")
st.sidebar.write('Negara : ',negara, color = "red")

df['produksi'] = df['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
df['produksi'] = df['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
df['produksi'] = pd.to_numeric(df['produksi'], errors='coerce')

#A
#TABEL A
df2 = pd.DataFrame(df,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['kode_negara']==kode]
df2['produksi'] = pd.to_numeric(df2['produksi'], errors='coerce')

right_col.write(df2)

#OUTPUT GRAFIK A
fig, ax = plt.subplots()
ax = plt.gca()
ax.plot(df2['tahun'], df2['produksi'], label = df2['tahun'], color = 'red')
ax.set_title("Jumlah Produksi Per Tahun di Negara Pilihan")
ax.set_xlabel("Tahun", color="green", fontsize = 20)
ax.set_ylabel("Jumlah Produksi", color="yellow", fontsize = 20)

plt.show()
mid_col.pyplot(fig)

#B
list_kodekumpulannegara = []
for i in list(csv_['kode_negara']) :
    if i not in list(df_info['alpha-3']) :
        list_kodekumpulannegara.append(i)

for i in list_kodekumpulannegara :
    csv_ = csv_[csv_.kode_negara != i]
print(csv_)

st.sidebar.header('Pengaturan Negara dengan Produksi Terbesar')
tahun = st.sidebar.number_input("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.number_input("Pilih Banyak Negara", min_value=1, max_value=None)


dfb = csv_.loc[csv_['tahun'] == tahun]
dfb = dfb.sort_values(by='produksi', ascending = False)
df3 = dfb[:n]
print(df3)
df3.plot.bar(x='kode_negara', y='produksi')
plt.show()
st.pyplot(plt)

#c
list_a = []
kumulatif = []

for i in list (csv_['kode_negara']) :
    if i not in list_a:
        list_a.append(i)
        
for i in list_a :
    a=csv_.loc[csv_['kode_negara'] ==i,'produksi'].sum()
    kumulatif.append(a)
    
dk = pd.DataFrame(list(zip(list_a,kumulatif)), columns = ['kode_negara','kumulatif'])
dk = dk.sort_values(by=['kumulatif'], ascending = False)
dk = dk[:n]

dk.plot.bar(x='kode_negara', y='kumulatif') 
plt.scatter(x='kode_negara', y='kumulatif')
plt.show()
st.pyplot(plt)

#D
list_kodenegara = []
list_regionnegara = []
list_subregionnegara = []
for i in range(len(dataframe_kumulatifnegara)) :
    for j in range(len(dataframe_json)) :
        if list(dataframe_kumulatifnegara['nama_negara'])[i] == list(dataframe_json['name'])[j]:
            list_kodenegara.append(list(dataframe_json['alpha-3'])[j])
            list_regionnegara.append(list(dataframe_json['region'])[j])
            list_subregionnegara.append(list(dataframe_json['sub-region'])[j])

dataframe_kumulatifnegaralengkap = pd.DataFrame(list(zip(list_kodenegara, list_namanegara, list_jumlahkumulatif, list_regionnegara, list_subregionnegara)), columns=['kode_negara', 'nama_negara', 'jumlah_kumulatif', 'region', 'sub-region'])

T2 = st.selectbox("Tahun", list_tahun)

left_col4, right_col4 = st.columns(2)

#left column 4
#terbesar
dataframe_jumlahproduksiterbesar2 = dataframe_gabungan.loc[dataframe_gabungan['tahun'] == T2]
dataframe_jumlahproduksiterbesar2 = dataframe_jumlahproduksiterbesar2.sort_values(by='produksi', ascending=False)
dataframe_jumlahproduksibaru2 = dataframe_jumlahproduksiterbesar2[:1]
with left_col4 :
    st.subheader("Data Negara dengan Produksi Terbesar pada Tahun Tersebut")
    st.dataframe(dataframe_jumlahproduksibaru2)

#right column 4
#terkecil
dataframe_produksitanpanol = dataframe_gabungan[dataframe_gabungan.produksi != 0]
dataframe_jumlahproduksiterkecil = dataframe_produksitanpanol.loc[dataframe_produksitanpanol['tahun'] == T2]
dataframe_jumlahproduksiterkecil = dataframe_jumlahproduksiterkecil.sort_values(by='produksi', ascending=True)
dataframe_jumlahproduksiterkecilbaru = dataframe_jumlahproduksiterkecil[:1]
with right_col4 :
    st.subheader("Data Negara dengan Produksi Terkecil pada Tahun Tersebut")
    st.dataframe(dataframe_jumlahproduksiterkecilbaru)

left_col5, right_col5 = st.columns(2)

#left column 5
#terbesar keseluruhan tahun
dataframe_terbesarkeseluruhantahun = dataframe_kumulatifnegaralengkap.sort_values(by='jumlah_kumulatif', ascending=False)
dataframe_terbesarkeseluruhantahunbaru = dataframe_terbesarkeseluruhantahun[:1]
with left_col5 :
    st.subheader("Data Negara dengan Produksi Kumulatif Terbesar dari Keseluruhan Tahun")
    st.dataframe(dataframe_terbesarkeseluruhantahunbaru)

#right column 5
#terkecil keseluruhan tahun
dataframe_terkecilkeseluruhantahun = dataframe_terbesarkeseluruhantahun.sort_values(by='jumlah_kumulatif', ascending=True)
dataframe_kumulatiftanpanol = dataframe_terkecilkeseluruhantahun[dataframe_terkecilkeseluruhantahun.jumlah_kumulatif != 0]
dataframe_terkecilkeseluruhantahunbaru = dataframe_kumulatiftanpanol[:1]
with right_col5 :
    st.subheader("Data Negara dengan Produksi Kumulatif Terkecil dari Keseluruhan Tahun")
    st.dataframe(dataframe_terkecilkeseluruhantahunbaru)

left_col6, right_col6 = st.columns(2)

#nol
dataframe_produksinol = dataframe_gabungan[dataframe_gabungan.produksi == 0]
dataframe_jumlahproduksinol = dataframe_produksinol.loc[dataframe_produksinol['tahun'] == T2]
with left_col6 :
    st.subheader("Data Negara-Negara dengan Jumlah Produksi sama dengan Nol pada Tahun Tersebut")
    st.dataframe(dataframe_jumlahproduksinol)

#nol keseluruhan tahun
dataframe_kumulatifnol = dataframe_terkecilkeseluruhantahun[dataframe_terkecilkeseluruhantahun.jumlah_kumulatif == 0]
with right_col6 :
    st.subheader("Data Negara-Negara dengan Jumlah Produksi sama dengan Nol dari Keseluruhan Tahun")
    st.dataframe(dataframe_kumulatifnol)
