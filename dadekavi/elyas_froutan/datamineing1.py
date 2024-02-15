
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('dadekavi/elyas_froutan/exel/AAPL.xlsx')

final_price1=[]
final_price2=[]
final_price0=[]

for item in data["Adj Close"]:
    final_price0.append(item)
    final_price1.append(item)
    final_price2.append(item)

for i in range(0,len(final_price1)-5,5):
    avg=sum(final_price1[i:i+5])/5
    min1=min(final_price2[i:i+5])
    max1=max(final_price2[i:i+5])
    for j in range(0,5):
        final_price1[i+j]=avg
        if (final_price2[i+j]>=(max1+min1)/2):
            final_price2[i+j]=max1
        else:
             final_price2[i+j]=min1


# asli abi ------------------------------------------------------
# hamvar shode ba miangin sabz ----------------------------------
# hamvar shode karani sorkh--------------------------------------
plt.plot(range(0,len(final_price0)), final_price0,'b',range(0,len(final_price0)),final_price1,'g',final_price2 ,'r')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()