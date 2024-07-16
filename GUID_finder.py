from bs4 import BeautifulSoup

#В список вносим имена всех параметров, как вы их задавали(или они были по-умолчанию заданы) в T-FLEX CAD.
array_to_find = [
'Комментарий',
'Наименование',
'Объект геометрической структуры',
'Проект',
'Тип элемента',
'CAD ID',
'X',
'Y',
'Z',
'Блокируемые оси',
'Геометрический элемент',
'Длина',
'Пользовательский комментарий',
'Статус официализации',
'Тип отображения',
'X1',
'Y1',
'Z1',
'Ширина призмы',
'I',
'J',
'K',
'Диаметр',
'Диаметр геометрического элемента'
]

max_len = max(map(len, array_to_find))
#Путь, в функции "open" ниже, нужно поменять на свой.
with open(r'<ВАШ ПУТЬ>\GEOM.Спецификация.xml', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file.read(), features='xml')
    with open('result.txt', 'w', encoding='UTF-8') as result_file:
        for i in soup.Parameters.find_all("Parameter"):
            name = i.get("Name")
            id = i.get("ID")
            if name in array_to_find:
                print(f'{name + ' ' * (max_len - len(name))}: {id}', file=result_file)
