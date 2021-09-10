import pandas as pd 
import matplotlib.pyplot as plt

def avg_data_2013():
    temp=0
    average=[]
    for rows in pd.read_csv('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/AQI/aqi2013.csv',chunksize=24):
        summation=0
        avg=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                summation=summation+i
            elif type(i) is str:
                if i!='NoData'  and i!='PwrFail' and i!='InVld' and i!='---':
                    tem=float(i)
                    summation=summation+tem
        avg=summation/24
        average.append(avg)
        temp+=1
        
    return average
        
    
def avg_data_2014():
    temp=0
    average=[]
    for rows in pd.read_csv('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/AQI/aqi2014.csv',chunksize=24):
        summation=0
        avg=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                summation+=i
            elif type(i) is str:
                if i!='NoData'  and i!='PwrFail' and i!='InVld' and i!='---':
                    tem=float(i)
                    summation=summation+tem
             
            
               
        avg=summation/24
        average.append(avg)
        temp+=1
        
    return average
        


def avg_data_2015():
    temp=0
    average=[]
    for rows in pd.read_csv('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/AQI/aqi2015.csv',chunksize=24):
        summation=0
        avg=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                summation+=i
            elif type(i) is str:
                if i!='NoData'  and i!='PwrFail' and i!='InVld' and i!='---':
                    tem=float(i)
                    summation=summation+tem
        avg=summation/24
        average.append(avg)
        temp+=1
        
    return average
        

def avg_data_2016():
    temp=0
    average=[]
    for rows in pd.read_csv('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/AQI/aqi2016.csv',chunksize=24):
        summation=0
        avg=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                summation+=i
            elif type(i) is str:
                if i!='NoData'  and i!='PwrFail' and i!='InVld' and i!='---':
                    tem=float(i)
                    summation=summation+tem
        avg=summation/24
        average.append(avg)
        temp+=1
        
    return average
        


def avg_data_2017():
    temp=0
    average=[]
    for rows in pd.read_csv('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/AQI/aqi2017.csv',chunksize=24):
        summation=0
        avg=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                summation+=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='InVld' and i!='---':
                    tem=float(i)
                    summation=summation+tem
        avg=summation/24
        average.append(avg)
        temp+=1
        
    return average
        


def avg_data_2018():
    temp=0
    average=[]
    for rows in pd.read_csv('C:/Users/chirag.bhargava/Desktop/Newfolder/Data/Data/AQI/aqi2018.csv',chunksize=24):
        summation=0
        avg=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                summation+=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='InVld' and i!='---':
                    tem=float(i)
                    summation=summation+tem
        avg=summation/24
        average.append(avg)
        temp+=1
        
    return average
        



if __name__=="__main__":
    
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    














