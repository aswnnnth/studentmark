
# to create a student csv file
import pandas as pd
data={
    'student_name':['Aswanth','Amal','Vishnu','Arun','Deeraj'],
    'Total_mark':[400,160,450,344,380]
}

df=pd.DataFrame(data)
# print(df)
df.to_csv('student_data.csv', index=False)

df1=pd.read_csv('student_data.csv')  
print(df1)



# calculate percentage
df1['Percentage']=(df1['Total_mark'] / 500)*100
print(df1['Percentage'])


# determine student is pass or not

df1['Result']=df1['Percentage'].apply(lambda x:'pass' if x>40 else 'fail')
print(df1['Result'])
print(df1)
df1.to_csv('Student_result.csv',index=False)