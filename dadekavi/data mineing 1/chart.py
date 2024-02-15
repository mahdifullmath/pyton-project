import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
step=6
data=pd.read_excel('dadekavi\data mineing 1\edited_zagros.xlsx')
final_price = data['end_price'].to_list()
#print(final_price)
final_price1=[]
final_price2=[]
for item in final_price:
    final_price1.append(item)
    final_price2.append(item)

for i in range(0,len(final_price1)-step,step):
    avg=sum(final_price1[i:i+step])/step
    mini=min(final_price2[i:i+step])
    maxi=max(final_price2[i:i+step])
    for j in range(0,step):
        final_price1[i+j]=avg
        if (final_price2[i+j]>=(maxi-mini)/2+mini):
            final_price2[i+j]=maxi
        else:
             final_price2[i+j]=mini

#plt.plot(range(0,100),final_price[:100],'r--',final_price1[:100],'b',final_price2[:100],'g',)
plt.plot(range(0,len(final_price)), final_price,'g--',range(0,len(final_price)),final_price1,'b',final_price2 ,'r')
plt.xlabel('Day')
plt.ylabel('Price (IRR)')
plt.show()