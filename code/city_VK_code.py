import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
#Get the file
Merged = pd.read_csv("C:/Users/Wanda/Desktop/merged_file.csv",sep=';')
citytitle1= Merged.loc[:,'city.title']
amountcity1= Merged.loc[:,'amount.city']
#create variables merged Matplotlib analytics format lists
citytitlelist1= citytitle1.tolist()
amountcitylist1= amountcity1.tolist()
# Get the cities and draw bar
print(citytitlelist1)
plt.rcParams.update({'font.size': 20})
x = np.arange(19)
fig, ax = plt.subplots()
fig = plt.figure(figsize=(20,10))
pl.xticks(rotation = 90)
plt.xlabel("Cities")
plt.ylabel("Amount")
plt.title("Location of Russian speaking people interested in Finish products (VKontakte)  ")
plt.bar(x, amountcitylist1)
plt.xticks(x, ('Perm', 'Nizhny Novgorod', 'Novosibirsk', 'Yekaterinburg', 'Gomel', 'Donetsk', 'Mogilev', 'Murmansk', 'Vologda', 'Petrozavodsk', 'Kharkiv', 'Kazan', 'Dnipropetrovsk Dnipro', 'Odessa', 'Lviv', 'Minsk', 'Kyiv', 'Moscow', 'Saint Petersburg'))
plt.show()