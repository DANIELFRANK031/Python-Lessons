# import pandas as pd 
# df=pd.read_csv('dataset.csv')
# data={'0':'Female','1':'Male'}
# df['Gender']=df['Gender'].astype(str).map(data)
# newdf=df.drop(['Own_car','Own_property','Work_phone','Phone','Email','Unemployed','Num_children'], axis=1)
# newdf['Years_employed']=newdf['Years_employed'].astype(int)
# newdf.to_csv('Cleaned data')
# print('Cleaned has been saved')

import pandas as pd
def extractdata(file):
    df=pd.read_csv(file)
    data={'0':'Female','1':'Male'}
    df['Gender']=df['Gender'].astype(str).map(data)
    newdf=df.drop(['Own_car','Own_property','Work_phone','Phone','Email','Unemployed','Num_children'], axis=1)
    newdf['Years_employed']=newdf['Years_employed'].astype(int)
    newdf.to_csv('Cleaned data')
    print('Cleaned has been saved')
