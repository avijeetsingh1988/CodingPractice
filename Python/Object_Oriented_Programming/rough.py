import pandas as pd 
df=pd.DataFrame({'date':['2019-02-07','2019-02-07','2019-02-08'],
                 'id':[223,223,223],
                 'code':[1234,1234,1234],
                 'value':[4234,34534,23423],
                 'qty':[2,3,4]})

key_col=['date','id','code']
df=df.groupby(key_col).agg({'value':'sum', 'qty':'sum'}).reset_index()
print(df.index.values)