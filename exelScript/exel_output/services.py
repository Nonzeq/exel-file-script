import pandas as pd
from time import sleep
import re



def make_new_file_mount(export_from_data_base):

    zalishok = {}
    d1 = pd.read_excel(f'media/exel/{export_from_data_base}', engine='openpyxl')
    d1["Код"] = d1['Код'].str.replace(' ', '')

    zalushok_dict2 = d1.set_index(["Код"])["Залишок"].to_dict()



    d2 = pd.read_excel('media/exel/NEW_UPDATE_FILE.xlsx',  engine='openpyxl')
    #
    # for key, value in zalushok_dict2.items():
    #     q = zalushok_dict2.get(key)
    #     if zalushok_dict2.get(key) == 0:
    #         zalishok[key] = value
    # print(zalushok_dict2)
    for key,value in zalushok_dict2.items():
        zalishok[key] = value

    print(zalishok)
    index = 0
    for mount in d2["Код_товара"]:
        q = zalishok.get(mount)

        if zalishok.get(mount) == 0:
            d2.loc[index, "Наличие"] = '-'
            index = index + 1
        elif zalishok.get(mount) is not None and zalishok.get(mount) > 0:
            d2.loc[index, "Наличие"] = '+'
            index = index + 1
        else:
            index = index + 1
            continue

    data = pd.DataFrame(d2)
    full = data.to_excel("media/exel/NEW_UPDATE_FILE.xlsx", index=False)
    return full



def make_new_file_price(path:str,export_from_prom):

    d1 = pd.read_excel(path, engine='openpyxl', converters={'title':str,'price':str})
    d1["price"] = d1["price"].str.replace(r',[^,]*$', '')
    start_dict1 = d1.set_index(['title'])['price'].to_dict()


    # for key, value in start_dict1.items():


    d2 = pd.read_excel(f'media/exel/{export_from_prom}',  engine='openpyxl')
    index = 0
    for price in d2["Код_товара"]:
        pr = start_dict1.get(price)
        if start_dict1.get(price):
            d2.loc[index, "Цена"] = start_dict1.get(price)
            index = index + 1
        else:
            index = index + 1
            continue


    # print(start_dict1)
    # d2.loc[0,"Цена"] = '22'
    # d2.loc[1,"Цена"] = '32'
    # print(d2.loc[0,"Код_товара"])

    data = pd.DataFrame(d2)
    data.to_excel('media/exel/NEW_UPDATE_FILE.xlsx', index=False)







def main(export_from_data_base,export_from_prom):


    d1 = pd.read_excel(f'media/exel/{export_from_data_base}', engine='openpyxl')
    for column in d1.columns:
        d1[column] = d1[column].str.replace(' ' , '')

    start_dict1 = d1.set_index(['Код'])['Ціна'].to_dict()


    d2 = pd.read_excel(f'media/exel/{export_from_prom}', engine='openpyxl')

    # d2 = d2.replace(r'\D+', '', regex=True)

    start_dict2 = d2.set_index(["Код_товара"])["Цена"].to_dict()

    # print(start_dict1)
    # print(start_dict2)

    d3 = {}
    d4 = {}
    for key, value in start_dict2.items():
        DATA1 = str(key)
        DATA2 = start_dict1.get(key)
        if start_dict1.get(key):
            d3[key] = DATA2
        else:
            d4[key] = value
            # print('LOADING')
    if len(d3) > 0:
        header = ['title', 'price']
        data = pd.DataFrame(list(d3.items()))
        data.to_excel('media/exel/OUT.xlsx', index=False, header=header)

        # data1 = pd.DataFrame(list(d4.items()))
        # data1.to_excel('QWE.xlsx', index=False,header=header)
    else:
        print('Нічого не знайдено')

    make_new_file_price('media/exel/OUT.xlsx',export_from_prom)
    make_new_file_mount(export_from_data_base)




