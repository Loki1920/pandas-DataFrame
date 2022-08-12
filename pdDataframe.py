import pandas as pd

data = {
    'calories':[454,567,234],
    'duration':[40,50,60]
}
df = pd.DataFrame(data,index = [1,2,3])
print(df)
#loc[1] return 1st row  
print(df.loc[1])
print(df.loc[[1,2]])
# indexing our own index 
dx = pd.DataFrame(data,index = ['day1','day2','day3'])
print(dx)
#loc 
print('day1 data','\n',dx.loc['day1'])

