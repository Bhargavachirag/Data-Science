from Plot_AQI import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import os
import csv

def meta_data(year,month):
    file_html=open('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/Html_data/{}/{}.html'.format(year,month),'rb')
    plain_text=file_html.read()
    
    
    temp=[]
    final_lst=[]
    soup=BeautifulSoup(plain_text,'lxml')
    
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                temp.append(tr.get_text())
    
    rows=round(len(temp)/15)
    
    for i in range(rows):
        lst=[]
        for j in range(15):
            lst.append(temp[0])
            temp.pop(0)
        final_lst.append(lst)
        
            
                
    final_lst.pop(len(final_lst)-1)
    final_lst.pop(0)
    
    for k in range(len(final_lst)):
        final_lst[k].pop(6)
        final_lst[k].pop(13)
        final_lst[k].pop(12)
        final_lst[k].pop(11)
        final_lst[k].pop(10)
        final_lst[k].pop(9)
        final_lst[k].pop(0)
        

    return final_lst

def data_combine(year,cs):
    for a in pd.read_csv('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/Real_data/real_' +str(year) + '.csv',chunksize=cs):
        df=pd.DataFrame(data=a)
        mylist=df.values.tolist()
    return mylist
        
    
    

if __name__=='__main__':
    
    
    if not os.path.exists('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/Real_data'):
        os.makedirs('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/Real_data')
        
        for year in range(2013,2017):
            final_data=[]
            with open('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/Real_data/real_' +str(year) + '.csv', 'w') as csvfile:
                wr=csv.writer(csvfile,dialect='excel')
                wr.writerow(['T','TM','Tm','SLP','H','VV','V','VM','PM 2.5'])
            for month in range(1,13):
                temp=meta_data(year, month)
                final_data+=temp
                
            pm=getattr(sys.modules[__name__],'avg_data_{}'.format(year))()
            
            if len(pm)==364:
                pm.insert(364,'-')
                
            for i in range(len(final_data)-1):
                final_data[i].insert(8,pm[i])
                    
            with open('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/Real_data/real_' +str(year) + '.csv', 'a') as csvfile:
                wr=csv.writer(csvfile,dialect='excel')
                for row in final_data:
                    flag=0
                    for i in row:
                        if (i=='' or i=='-'):
                            flag=1
                            
                    if flag!=1:
                        wr.writerow(row)
                
                    
    data_2013=data_combine(2013, 600)
    data_2014=data_combine(2014, 600)
    data_2015=data_combine(2015, 600)
    data_2016=data_combine(2016, 600)            
                
    total=  data_2013 + data_2014 + data_2015+ data_2016
    with open('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/Combine_data.csv', 'w') as csvfile:
                wr=csv.writer(csvfile,dialect='excel')
                wr.writerow(['T','TM','Tm','SLP','H','VV','V','VM','PM 2.5'])
                wr.writerows(total)
                    
                
   
       
     

































