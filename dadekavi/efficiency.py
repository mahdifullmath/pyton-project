import finpy_tse as tse
import matplotlib.pyplot as plt
import statistics

def bazdehi(sorce_list,bazdehi_list,len):
    for i in range(0,len-1):
        bazdehi_list.append((sorce_list[i+1] - sorce_list[i])/sorce_list[i+1])


DF1 = tse.Get_Price_History(stock='اپال',
                            start_date='1400-01-01',
                            end_date='1401-01-01',
                            ignore_date=False,
                            adjust_price=True,
                            show_weekday=True,
                            double_date=True)
closed_apal = DF1['Close'].values.tolist()
DF2= tse.Get_Price_History(stock='خودرو',
                            start_date='1400-01-01',
                            end_date='1401-01-01',
                            ignore_date=False,
                            adjust_price=True,
                            show_weekday=True,
                            double_date=True)

closed_khodro = DF2['Close'].values.tolist()
DF3= tse.Get_Price_History(stock='آبادا',
                            start_date='1400-01-01',
                            end_date='1401-01-01',
                            ignore_date=False,
                            adjust_price=True,
                            show_weekday=True,
                            double_date=True)
closed_abada= DF3['Close'].values.tolist()
bazdehi_apal=[]
bazdehi_khodro=[]
bazdehi_abada=[]
bazdehi(closed_apal,bazdehi_apal,len(closed_apal))
bazdehi(closed_khodro,bazdehi_khodro,len(closed_khodro))
bazdehi(closed_abada,bazdehi_abada,len(closed_abada))

print(f"bazdehi saham apal = {(100*sum(bazdehi_apal)/len(bazdehi_apal)) }%" )

print(f"bazdehi saham khodro = {(100*sum(bazdehi_khodro)/len(bazdehi_khodro))} %" )

print(f"bazdehi saham abada = {(100*sum(bazdehi_abada)/len(bazdehi_abada))} %" )










