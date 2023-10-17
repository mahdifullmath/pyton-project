import numpy as np
import pandas as pd
import math
from sklearn.cluster import KMeans

high_use = pd.read_excel('C:/Users/mahdi/Desktop/pyton project/kar amoozi/inputData.xlsx')

#max available data
numtotal_periods = 48
# last 
last_month = str(max(high_use['NUM_MONTH_USE_SPMUS']))

num_month = int(last_month[4:6])

forecast_horizen = 12 - num_month


pivot_table = high_use.pivot_table(values = 'QTY_NET_USE_SPMUS' , index = 'ITEM_ITEM_ID' , columns = 'NUM_MONTH_USE_SPMUS' , 
                     aggfunc='sum',fill_value = 0 , margins = False)
pivot_table2 = pivot_table.copy()

pivot_table['sum_all'] = pivot_table2.sum(axis = 1)
pivot_table['avg_real'] = pivot_table2.mean(axis = 1)
pivot_table

Category = [-(math.inf), 3, 5.5, 7.5, 11.5, 15.5, 22.5, 32.5, 52.5, 94.5, 225.5, math.inf]


daste = []
for qty in pivot_table['sum_all']:
    for i in range(len(Category)):
        if qty<= Category[i] :
            daste.append(Category[i-1])
            break
                        
pivot_table['daste'] = daste


pivot_table.describe()

daste_group = pivot_table.groupby('daste')['sum_all'].agg(np.sum).to_frame()
daste_ha = list(daste_group.index)
clustered_list = []
for group in daste_ha:
    cluster_group = []
    table_daste = pivot_table[pivot_table['daste'] == group]
    X = table_daste.iloc[: ,33:46 ].values
    kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y = kmeans.fit_predict(X)
    table_daste['cluster'] = y
    clustered_list.append(table_daste)
    

result_kmeans = pd.concat(clustered_list)


final_cluster = []
for i in range(result_kmeans.shape[0]):
    d =str(result_kmeans['daste'].values[i])
    cl = str(result_kmeans['cluster'].values[i])
    f_cluster = d + '_' + cl
    final_cluster.append(f_cluster)
    
result_kmeans['final_cluster'] = final_cluster   

cluster_groupby = result_kmeans.groupby(['final_cluster']).agg(np.mean).iloc[:,:-4]
cluster_groupby2 = cluster_groupby.copy()
sum_cl = result_kmeans.groupby(['final_cluster']).agg(np.sum)
cluster_groupby['sumall'] = list(sum_cl['sum_all'].values)
cluster_groupby['avg_cluster'] = cluster_groupby2.mean(axis = 1)
cluster_groupby

from statsmodels.tsa.arima.model import ARIMA
forecast_result = []
for i in range(cluster_groupby.shape[0]): #22
    serie = cluster_groupby.iloc[i,:-2] # row of i
    model_arima = ARIMA(serie ,order = (1,0,0)) #create object from ARIMA class 
    result_arima = model_arima.fit() #fit the model with input parametters
    output = result_arima.forecast(12) # forecast 12 month further
    forecast_result.append(output) 

result_arima.summary()


predicted_df =  pd.DataFrame(data = np.array(forecast_result), columns=[('month'+str(i+1)) for i in range(12)],
                            index = cluster_groupby.index)


cluster_predict = pd.concat([cluster_groupby,predicted_df],axis =1 )
pd.set_option('display.max_columns', None)
cluster_predict.style.set_sticky(axis="index")
cluster_predict

ratio_total = []
num_total_item=result_kmeans.shape[0]
for i in range(num_total_item):
    item_cluster =result_kmeans['daste'].values[i]
    item_avg_real =result_kmeans['avg_real'].values[i]
    ratio_item = np.mean([np.mean(item_avg_real)/np.mean(item_cluster),np.sum(item_avg_real)/np.sum(item_cluster)])
    ratio_total.append(ratio_item)

final_table=result_kmeans.copy()
final_table["ratio_total"]=ratio_total


merged_df=pd.merge(left=final_table,right=predicted_df,how="left",on='final_cluster')


this_year_predict=[]
t=12-forecast_horizen+1
this_year=last_month[:4]
temp=0
sum_this_year=0
for i in range(num_total_item):
    for x in range(1,forecast_horizen + 1):
        temp = temp + final_table["ratio_total"].values[i] * merged_df[f'month{x}'].values[i]
    # for j in range(1,t):
    #     if j<10:
    #         sum_this_year = sum_this_year + merged_df[int(f'{this_year}0{j}')].values[i]
    #     else:
    #         sum_this_year = sum_this_year + merged_df[f'{this_year}{j}'].values[i]
    # this_year_predict.append(temp+sum_this_year)
    this_year_predict.append(temp)
    temp=0
    sum_this_year=0
merged_df["this_year_predict"]=this_year_predict
final_table["this_year_predict"]=this_year_predict


next_year_predict=[]
temp=0
for i in range(num_total_item):
    for x in range(1,13):
        temp = temp + final_table["ratio_total"].values[i] * merged_df[f'month{x}'].values[i]
    next_year_predict.append(temp)
    temp=0
merged_df["next_year_predict"]=next_year_predict
final_table["next_year_predict"]=next_year_predict

final_table.to_excel("output_high2.xlsx",sheet_name="output")