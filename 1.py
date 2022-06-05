
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

#1
df = pd.read_csv('vehicles_dataset_upd.csv')
pd.set_option('display.max_columns', None)
print(df.head())


#2
plt.figure(figsize=(8,5))
plt.hist(df.price, color="indigo", bins= 1000)
plt.xlabel("Цена")
plt.ylabel("Частота")
plt.title("Распределение цены")

#3
plt.figure(figsize=(5, 15))
plt.boxplot(df.price, sym='+' )
plt.ylabel('Цена')
plt.title('Ящик с усами для цены')  

#4
print(df.price.describe().apply(lambda x: f"{x:0.3f}"))

#5
boundaries = (df.price.quantile(0.25), df.price.quantile(0.75))
print('25% = ', boundaries[0], ', 75% = ', boundaries[1])

#6
is_outlier = (df.price < boundaries[0]) | (df.price > boundaries[1]) 
print("Количество выбросов:", is_outlier.sum()) 

#7
# print(df[(df.price < boundaries[0]) | (df.price > boundaries[1])].sort_values(['price']))

#8 
print( df[(df.price < boundaries[0]) | (df.price > boundaries[1])].sort_values(['price'])[-15:])

#9
df_new = df.drop(df[(df.price < boundaries[0]) | (df.price > boundaries[1])].index)
print(df_new.head())

#Zadacha 2

#1
df_years = df_new.groupby('year').mean()[['price']]
print(df_years)

#2
plt.figure(figsize=(10,10))
plt.scatter(df_years.index, df_years.price)
plt.ylabel("Price")
plt.xlabel("Year")
plt.title("Зависимость стоимости от года выпуска автомобиля")

#3
print(df_new.groupby('year').count()[['lat']].rename(columns = {'lat':'count'}))

#4
df_new = df_new[(df_new.year < 2021)]
print(df_new.head())

#5
df_years_filt = df_new.groupby('year').mean()[['price']].rename(columns = {'price':'meanprice'})
print(df_years_filt)

#6
plt.figure(figsize=(10,10))
plt.plot( df_years_filt.index,df_years_filt.meanprice, color='blue', marker = 'D', markerfacecolor = 'orange')
plt.ylabel("meanprice")
plt.xlabel("year")
plt.title("Зависимость стоимости от года автомобиля (линейный график)")

#7
print(df_years_filt.reset_index().corr())
#№1 так как коэффициент корреляции не нулевой, линейная связь между стоимостью автомобиля и годом его производства существует
#№2 можно, так как коэффициент близок к 1
#№3 существуемая связь является прямой, так как коэффициент пололжительный

#8
plt.figure(figsize=(8,5))
plt.hist(df_new.price, bins = 20, color='indigo')
plt.xlabel("Price")
plt.ylabel("Lat")
plt.title("Гистограмма распределения стоимости автомобиля")
# plt.show()

#9
df_new.to_csv('vehicles_dataset_upd2.csv', index = False)

#Zadacha 3
#1
colors = {'low': 'green', 'medium': 'orange', 'high': 'red'}
fig, ax = plt.subplots(figsize=(12, 8))

for price_category in colors:
    color = colors[price_category]
    data = df_new[df_new['price_category'] == price_category]

    ax.hist(data['price'], color=color, alpha = 0.7, bins = 20)

ax.legend(colors, loc='upper right', title="Ценовая категория")

plt.ylabel('Количество')
plt.xlabel('Цена')
plt.title('Распределение стоимости автомобиля по ценовой категории')

#2
colors = {'low': 'green', 'medium': 'orange', 'high': 'red'}
fig, ax = plt.subplots(figsize=(12, 8))
for price_category in colors:
    color = colors[price_category]
    data = df_new[df_new['price_category'] == price_category]

    ax.scatter(data['price'], data['year'], c=color, )

ax.legend(colors, loc='lower right', title="Ценовая категория")
plt.title("Зависимость цены от года выпуска")
plt.xlabel('Price')
plt.ylabel('Год выпуска')

#Zadacha 4
#1
df_proizvod = df_new.groupby('manufacturer').count()[['lat']].rename(columns = {'lat': 'count'})
print(df_proizvod)

#2
plt.figure(figsize=(20,10))
plt.bar(df_proizvod.index, df_proizvod['count'], width=0.9, color = ['springgreen', 'dodgerblue'])
plt.xlabel('Manufacturer')
plt.xticks(rotation = 45)
plt.ylabel('count')
plt.title('Распределение произваодителей')

#3
df_trans = df_new.groupby('transmission').count()[['lat']].rename(columns={'lat':'count'})
print(df_trans)

#4
plt.figure(figsize=(12,8))
plt.pie(df_trans['count'], labels=df_trans.reset_index()['transmission'], labeldistance=1.2, autopct = '%1.0f%%')
plt.legend()
plt.title('Распределение типа коробки передач')
plt.show()