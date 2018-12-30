#Research question: 
1. How are Russian speaking people located in the world, who are interested to buy Finnish products, who are subscribed to group 1 2 or 3?  
2. What is the age of this people?

#Pre- hypotheses for testing answering 1 and 2
a) Russian speaking people interested in Finnish products are located on the  border of eastern Finland.

b) Russian speaking people interested in Finnish products belongs to the post- soviet generation.

#The research material is collected from Russian social media VKontakte

Research target: 3 biggest groups collecting people together, who wants to buy Finish products:

Group 1 Товары из Финляндии | Финские товары topic-24032000_29149505 32 754 members 29.12.2018

Group 2 ТОВАРЫ ИЗ ФИНЛЯНДИИ FinRushop topic-50785137_35010610 23 426 members 29.12.2018

Group 3 Товары из Финляндии topic-55447193_28632385 17 586 members 29.12.2018

all these groups 1 2 and 3 contains people who are subscribed as followers of the groups. Detailed information about the followers accounts can be accessed by token.

#Actions in Vkontakte

Create an account in Vkontakte
Create an individual access token connected to your account in Vkontakte. 

Find API instructions here: https://vk.com/dev/manuals

Use Anaconda spyder environment to access the data. 

#Ethics and legal requirements regarding data processing
During collection and data processing, names and VKontakte ID numbers of the subscribers are removed according to the Russian data privacy law federal law 152- FZ.

#See the file access_data_VK_code.py for collection of data


# Prepare the raw data with following steps

Access the information and create 3 different data frames including metadata Group 1, Group 2 and Group 3

Add ID column to all files column A Group 1, Group 2, Group 3
a) Add column year.bdate, calculate to column C the year (year- function)

b) Add column amount.city, calculate to column G the amount of people/ city (countif function)

Prepare 2 different filtered files from each GROUP 1 2 and 3 for the following purposes:

a) city file- answering the question for hypotheses "a" choose the top 12 cities of subscribers add column (amount.city), create a new filtered filed format F_C_DE_XXXXX.csv


b) birthday file- answering question for hypotheses "b"
add column  bday.count, calculate with countif function the appearance of birthday year

remove years 1900- #Value(refering to 29.2) and 2018, these are calculus mistakes in csv 

filter top 15 most common birthday years column (bday.count)

choose the top 12 birthday year of subscribers, create a new filtered filed format F_BD_DE_XXXXX.csv


Processing the answer for hypotheses "a" in anaconda
Prepare csv GROUP 1 2 and 3 sort the column (amount.city) column F to chronological order sort az, before input

Remove duplicates from column (city.title) column E, create a new file for input to anaconda GROUP A B and C and merge #them to one file (create sum of the amount.city) result= merged_file.csv

Processing the answer for hypothese "b" in anaconda.
Prepare csv GROUP 1 2 and 3, sort the rows column (year.bdate) column C to chronological order sort az, before input

#See the file bday_VK_code.py and city_VK_code.py for code

#Answer to questions SUMMARY:

#What are the humanities research questions?

Research question: 
1. How are Russian speaking people located in the world, who are interested to buy Finish products, who are subscribed to #group 1 2 or 3?  
2. What is the age of this people?

#Pre- hypotheses for testing: 

a) Russian speaking people interested in Finnish products are located on the border of eastern Finland
 
b) Russian speaking people interested in Finnish products or trading belongs to the post- soviet generation

#Which data did I use?
Data from Russian social media VKontakte (similar with facebook)

#What did I do to the data (and how can somebody reproduce it)?
create account in Vkontakte, 
create individual access token (you can also use directly my files)
install anaconda spyder,
follow the instructions above for pipline

 
#What does the analysis show, how does it answer the humanities research question?

hypotheses "a" The hypotheses is not clearly true. A big amount of persons interested in Finnish products are located in big cities as St Petersburg and Moscow, but not only on the border area of Finland. 
It seems to be that people from Ukraine and Belarus are also interested in Finnish products. From the viewpoint of post soviet region, it is interesting to notice, that the Baltic countries are not represented on the list. 

As conclusion it might be that people from big cities have better access to international products. People have personal experience as consumers of the products, they are available in special shops and big markets providing international goods. From marketing perspective, it is valuable to put attention where the demand of Finnish products might be high.

hypotheses "b" The hypotheses is true. The biggest amount of the followers belong to the post soviet generation born between 1984 and 2000. The difference between group 1 2 and 3 is big, even if they are following similar concept as group. It is important to notice that regarding hypotheses "b", there might be a statistical anomaly, as the users of social media as VKnontakte usually belong to the younger generation. It is interesting to notice that teenagers are not represented as the biggest group of followers, even if they are an active group in VKontakte. 

#Analyses of pipeline for potential bias and problems. What would still need to be done for the analysis to be trustable?

The data is collected from social media. Data from social media is valuable, but it can also be falls or contain a lot of untrue information. For example in case of marketing fake or robot  accounts are used for sharing information. 

During the collection process, I collected a lot of metadata. It would be possible to find valuable prove that the account is true, for example by using the metadata information about the users (last time online, information if the account is banned etc), with this information I could sort most likely valuable accounts. 

For analyses I used only cities and ages of high value and ignored the smaller values to avoid false results. The visualizations might still show false numerical information (because of fake accounts), but you can get indicative information and answers to the stated hypothesis on high level. 

For future it would be useful to compare statistics made based on VKontakte, how many people lie in social media and remove the prosentual amount from the final result. This could also be done with statistical formula.