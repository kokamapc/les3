informations = {'Имя' : 'Иванов Иван Иванович',
             'Родился':'1965',
             'Город':'Москва',
             'Учился':'Сельхоз академия',
             'Работа':'Тракторист'}
print('Введите данные: ')
data = input()
if data in informations:
    print(informations[data])
