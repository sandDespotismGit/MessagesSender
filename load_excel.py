import xlsxwriter
from pars import array

def writer(parameter):
    book = xlsxwriter.Workbook('data.xlsx')
    page = book.add_worksheet('первая партия')

    page.set_column('A:A', 80)
    page.set_column('B:B', 60)
    page.set_column('C:C', 20)
    page.set_column('D:D', 20)
    page.set_column('E:E', 100)

    page.write('A1', 'Наименование компании')
    page.write('B1', 'Почта')
    page.write('C1', 'Отспамили мамонта?')
    page.write('D1', 'Ответ положительный?')
    page.write('E1', 'Категория')
    row = 0
    column = 0
    for item in parameter():
        page.write(row+1, column, item[0])
        page.write(row+1, column+1, item[1])
        page.write(row+1, column+4, item[2])
        row +=1
    book.close()
writer(array)