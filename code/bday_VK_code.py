


import pylab as pl
import pandas as pd
import matplotlib.pyplot as plt



#Read csv
group1 = pd.read_csv("C:/Users/Wanda/Desktop/F_BD_DE_24032000.csv",sep=';')
group2 = pd.read_csv("C:/Users/Wanda/Desktop/F_BD_DE_50785137.csv",sep=';')
group3 = pd.read_csv("C:/Users/Wanda/Desktop/F_BD_DE_55447193.csv",sep=';')

#create variables group 1 Matplotlib analytics
yearbdate1= group1.loc[:,'year.bdate']
count1= group1.loc[:,'bday.count']
#create variables group 1 Matplotlib analytics format lists
listyearbdate1= yearbdate1.tolist()
listcount1= count1.tolist()

#create variables group 2 Matplotlib analytics
yearbdate2= group2.loc[:,'year.bdate']
count2= group2.loc[:,'bday.count']
#create variables group 2 Matplotlib analytics format lists
listyearbdate2= yearbdate2.tolist()
listcount2= count2.tolist()

#create variables group 3 Matplotlib analytics
yearbdate3= group3.loc[:,'year.bdate']
count3= group3.loc[:,'bday.count']
#create variables group 3 Matplotlib analytics format lists
listyearbdate3= yearbdate3.tolist()
listcount3= count3.tolist()

#Plot the figure
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)

ax.plot(yearbdate1, count1,color= "r", label= "Group 1",linewidth= "4")
ax.plot(yearbdate2, count2, "b", label= "Group 2",linewidth= "4")
ax.plot(yearbdate3, count3, "g", label= "Group 3",linewidth= "4")


fig.savefig('fig1.png', dpi = 1000)
pl.xticks(rotation = 90)
plt.xlabel("Birthday year")
plt.title("Followers of groups in VKontakte interested in Finnish products/ year of birth  ")
plt.ylabel("Amount of followers of Group 1 2 and 3")
plt.legend(loc= "upper left")

plt.xlim(1983, 2000)

plt.style.use(['dark_background'])











