import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
step=6
def bazdehi(sorce_list,bazdehi_list,len):
    for i in range(0,len-1):
        bazdehi_list.append((sorce_list[i+1] - sorce_list[i])/sorce_list[i+1])


data=pd.read_excel('dadekavi/data mineing 2/booali-price-history-1400-09-01-to-1401-09-01.xlsx')
final_price_booali = data['end_price'].to_list()
#print(final_price)
data=pd.read_excel('dadekavi/data mineing 2/jam-price-history-1400-09-01-to-1401-09-01.xlsx')
final_price_jam = data['end_price'].to_list()

data=pd.read_excel('dadekavi/data mineing 2/kachad-price-history-1400-08-01-to-1401-09-01.xlsx')
final_price_kachad = data['end_price'].to_list()

data=pd.read_excel('dadekavi/data mineing 2/khorasan-price-history-1400-09-01-to-1401-09-01.xlsx')
final_price_khorasan = data['end_price'].to_list()

data=pd.read_excel('dadekavi/data mineing 2/zagros_farabours-price-history-1400-09-01-to-1401-09-01.xlsx')
final_price_zagros = data['end_price'].to_list()
bazdehi_booali=[]
bazdehi_jam=[]
bazdehi_kachad=[]
bazdehi_khorasan=[]
bazdehi_zagros=[]
# for i in range(0,len(final_price_booali)-1):
#     bazdehi_booali.append((final_price_booali[i+1]-final_price_booali[i])/final_price_booali[i+1])
#     bazdehi_jam.append((final_price_jam[i+1]-final_price_jam[i])/final_price_jam[i+1])
#     # bazdehi_kachad.append((final_price_kachad[i+1]-final_price_kachad[i])/final_price_kachad[i+1])
#     bazdehi_khorasan.append((final_price_khorasan[i+1]-final_price_khorasan[i])/final_price_khorasan[i+1])
#     # bazdehi_zagros.append((final_price_zagros[i+1]-final_price_zagros[i])/final_price_zagros[i+1])
# for i in range(0,len(final_price_kachad)-1):
#     bazdehi_kachad.append((final_price_kachad[i+1]-final_price_kachad[i])/final_price_kachad[i+1])
# for i in range(0,len(final_price_zagros)-1):
#     bazdehi_zagros.append((final_price_zagros[i+1]-final_price_zagros[i])/final_price_zagros[i+1])


bazdehi(final_price_booali,bazdehi_booali,len(final_price_booali))
bazdehi(final_price_jam,bazdehi_jam,len(final_price_jam))
bazdehi(final_price_kachad,bazdehi_kachad,len(final_price_kachad))
bazdehi(final_price_khorasan,bazdehi_khorasan,len(final_price_khorasan))
bazdehi(final_price_zagros,bazdehi_zagros,len(final_price_zagros))
print("avrage of bazdehi_booali =",100*sum(bazdehi_booali)/len(bazdehi_booali),'%')
print("avrage of bazdehi_jam =",100*sum(bazdehi_jam)/len(bazdehi_jam),'%')
print("avrage of bazdehi_kachad =",100*sum(bazdehi_kachad)/len(bazdehi_kachad),'%')
print("avrage of bazdehi_khorasan =",100*sum(bazdehi_khorasan)/len(bazdehi_khorasan),'%')
print("avrage of bazdehi_zagros =",100*sum(bazdehi_zagros)/len(bazdehi_zagros),'%')

    