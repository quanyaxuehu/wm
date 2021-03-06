import pandas as pd
from glob import glob
import click

##in this method: wm change2 change -i csv -o txt

def change_main(i, o):
    if i == 'txt' and o == 'csv':
        files = glob('*.txt')
        for file in files:
            print(file)
            data = pd.read_table(file)
            name = file.split('.')[0]
            data.to_csv(name + '.csv', index=False)
        print('Successfully Finished')

    elif i == 'csv' and o == 'txt':
        files = glob('*.csv')
        for file in files:
            print(file)
            data = pd.read_csv(file)
            name = file.split('.')[0]
            data.to_csv(name + '.txt', sep='\t', index=False)
        print('Successfully Finished')

    elif i == 'xlsx' and o == 'txt':
        files = glob('*.xlsx')
        for file in files:
            print(file)
            data = pd.read_excel(file)
            name = file.split('.')[0]
            data.to_csv(name + '.txt', sep='\t', index=False)
        print('Successfully Finished')

    elif i == 'xlsx' and o == 'csv':
        files = glob('*.xlsx')
        for file in files:
            print(file)
            data = pd.read_excel(file)
            name = file.split('.')[0]
            data.to_csv(name + '.csv', index=False)
        print('Successfully Finished')

    elif i == 'txt' and o == 'xlsx':
        files = glob('*.txt')
        for file in files:
            print(file)
            data = pd.read_table(file)
            name = file.split('.')[0]
            data.to_excel(name + '.xlsx', index=False)
        print('Successfully Finished')

    else:
        print(
            '\nSorry, not supported \nPlease try:\n-----------\ntxt--to--csv/xlsx\ncsv--to--txt\nxlsx--to--csv/txt\n-----------\n')

@click.command(short_help='File format conversion tool')
@click.option('-i',default='txt',help='输入文件的类型',type = str)
@click.option('-o',default='csv',help='输出文件的类型',type = str)
@click.option('-n',default='Angelababy',help='名字',type = str)
def change(i,o,n):
    print("hello:",n,"!")
    change_main(i,o)

if __name__ =='__main__':
    change()

