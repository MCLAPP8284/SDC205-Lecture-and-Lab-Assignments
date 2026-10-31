from datetime import datetime
date = datetime.now()
print("miccla8284")
print(date)

import pandas as pd
import matplotlib.pyplot as plt

#set array for 10 students and the subjects
students = ['Mark', 'Mary', 'Jeff', 'Pam', 'Chuck', 'Quinn', 'Brett',
            'Chandler', 'Rachel', 'Steven']
subjects = ['CST', 'SDC', 'CST', 'SDC', 'CST', 'SDC', 'CST', 'SDC',
            'CST', 'SDC']

#create the MultiIndex
index = pd.MultiIndex.from_arrays([students, subjects],
                                  names=('Student', 'Subject'))

#display the dataframe
df = pd.DataFrame({'Grade': [80,90,96,88,92,84,90,80,86,94]}, index=index)

#display the dataframe
print(df)

#calculate the subject grade averages
averageGrade = df.groupby(by=["Subject"]).mean()
print(averageGrade)

averageGrade['Grade'].plot(kind='bar')

plt.xlabel("Average Grade by Subject")
plt.xticks(rotation=0)
plt.show()
