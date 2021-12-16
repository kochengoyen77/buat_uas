#IMPORT AWAL
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
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


#MEMBUAT DATA FRAME TIAP FILE
st.title('Data Produksi Minyak Mentah')
st.header('UAS Pemrograman Komputer')
ch_ = csvHandler('produksi_minyak_mentah.csv')
jh_ = jsonHandler('kode_negara_lengkap.json')
csv_ = ch_.dataFrame
df_info = jh_.dataFrame
negara_li = df_info['name'].tolist()
'''
list1 = []
for i in list1 (csv_['kode negara']):
    if i not in (json_['alpha-3']):
        list1.append(i)
 '''

#MENGATUR LETAK OUTPUT
st.sidebar.title("Pengaturan")
st.sidebar.header('Pengaturan Jumlah Produksi Per Bulan')
left_col, mid_col, right_col = st.columns(3)
negara = st.sidebar.selectbox('Pilih negara : ',negara_li) 

kode = df_info[df_info['name']==negara]['alpha-3'].tolist()[0]

st.sidebar.write('Kode negara : ',kode)
st.sidebar.write('Negara : ',negara)

# MENGUBAH STRING MENJADI FLOAT
df['produksi'] = df['produksi'].astype(str).str.replace(".", "", regex=True).astype(float)
df['produksi'] = df['produksi'].astype(str).str.replace(",", "", regex=True).astype(float)
df['produksi'] = pd.to_numeric(df['produksi'], errors='coerce')

#OUTPUT TABEL A
df2 = pd.DataFrame(df,columns= ['kode_negara','tahun','produksi'])
df2=df2.loc[df2['kode_negara']==kode]
df2['produksi'] = pd.to_numeric(['produksi'], errors='coerce')

left_col.write(df2)

#OUTPUT GRAFIK A
fig, ax = plt.subplots()
ax.bar(tahun_prod, jumlah_prod, color==colors)
ax.plot(df2['tahun'], df2['produksi'], label = df2['tahun'])
ax.set_title("Jumlah Produksi Per Tahun di Negara Pilihan")
ax.set_xlabel("Tahun", fontsize = 12)
ax.set_ylabel("Jumlah Produksi", fontsize = 12)
ax.legend(fontsize = 2)
plt.show()
right_col.pyplot(fig)

#--b--

st.sidebar.header('Pengaturan Negara dengan Produksi Terbesar')
tahun = st.sidebar.number_input("Pilih Tahun produksi", min_value=1971, max_value=2015)
n = st.sidebar.number_input("Pilih Banyak Negara", min_value=1, max_value=None)
'''
list1 = []
for i in list1 (csv_['kode negara']):
    if i not in (jh_['alpha-3']):
        list1.append(i)
for i in list1:
    df2 = df2[df2['kode negara']!=1]
dfb = csv_.loc[csv_['tahun'] == tahun][:n]
dfb = dfb.sort_values(by='produksi', ascending = False)
dfb = dfb[:n]
'''
dfb.plot.bar(x='kode_negara', y='produksi')
plt.show()
st.pyplot(plt)

#--c--
list_a = []
kumulatif = []
x = st.sidebar.number_input("Pilih Banyak Negara 2", min_value=1, max_value=None)
'''
for i in list (csv_['kode_negara']) :
    if i not in list_a:
        list_a.append(i)
        
for i in list_a :
    a=csv_.loc[csv_['kode_negara'] ==i,'produksi'].sum()
    kumulatif.append(a)
'''
dk = pd.DataFrame(list(zip(list_a,kumulatif)), columns = ['kode_negara','kumulatif'])
dk = dk.sort_values(by=['kumulatif'], ascending = False)
dk = dk[:x]

dk.plot.bar(x='kode_negara', y='kumulatif') 
plt.show()
st.pyplot(plt)
'''
jumlah_produksi = dfb['produksi'][:1]
kode_negara = dfb['kode_negara'][:1]
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(json_)):
    if list(json_['alpha-3'])[i]==kode_negara:
        nama_negara = list(json_['name'])[i]
        region_negara = list(json_['region'])[i]
        subregion_negara = list(json_['sub-region'])[i]

st.right
'''
