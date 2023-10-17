
import finpy_tse as tse
import matplotlib.pyplot as plt

daste=6
#jamavari dade haye yek sal saham khodro---------------------------------------
final_price=tse.Get_Price_History(
    stock='خودرو',
    start_date='1400-01-01',
    end_date='1401-01-01',
    ignore_date=False,
    adjust_price=False,
    show_weekday=False,
    double_date=False)
#-----------------------------------------------------------------------------------


# init----------------------------------------
final_price1=[]
final_price2=[]
final_price0=[]


for item in final_price.Close._values:
    final_price0.append(item)
    final_price1.append(item)
    final_price2.append(item)

#----------------------------------------------------------------


# hamvar sazi________________________________________________
for i in range(0,len(final_price1)-daste,daste):
# hamvar sazi ba miangin-----------------------------------
    avg=sum(final_price1[i:i+daste])/daste
#----------------------------------------------------------
#hamvar sazi karani---------------------------------------
    min1=min(final_price2[i:i+daste])
    max1=max(final_price2[i:i+daste])
    for j in range(0,daste):
        final_price1[i+j]=avg
        if (final_price2[i+j]>=(max1+min1)/2):
            final_price2[i+j]=max1
        else:
             final_price2[i+j]=min1
#-----------------------------------------------------------
#__________________________________________________________________

#rasm nemoodar------asli abi khat chin-----hamvar shode ba miangin germez -----hamvar shode karani sabz--------------------------------------
plt.plot(range(0,len(final_price0)), final_price0,'b--',range(0,len(final_price0)),final_price1,'r',final_price2 ,'g')
plt.xlabel('Day')
plt.ylabel('Price (IRR)')
plt.show()