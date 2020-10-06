import xlrd
import csv
import datetime

SHEET_PATH = 'CSV/InfoCEI.xls'

def get_sheet_list(sheet_path):
    workbook = xlrd.open_workbook(sheet_path)
    worksheet = workbook.sheet_by_index(0)
    stock_deals_list = []

    for current_row in range(worksheet.nrows):
        stock_company = worksheet.cell(current_row, 6).value.strip()
        stock_date = worksheet.cell(current_row, 1).value.strip()
        stock_op = worksheet.cell(current_row, 3).value.strip()
        stock_amount = worksheet.cell(current_row, 8).value
        stock_price = worksheet.cell(current_row, 9).value
        deal_information = [stock_company, stock_date, stock_op, stock_amount, stock_price]

        if stock_op == 'C' or stock_op == 'V':    
            stock_deals_list.append(deal_information)
    return stock_deals_list


def str_to_date(date):
    date_time_obj = datetime.datetime.strptime(date, '%d/%m/%y')
    return datetime.datetime.strftime(date_time_obj, '%Y%m%d')


def set_stock_operation(operation_type, quantity):
    if operation_type == 'V':
        return f'-{quantity}'
    else:
        return quantity
        

def write_row_rules(writefile, row):
    writefile.writerow([
        f'{row[0]}.SA'.replace('3F','3'),
        str_to_date(row[1]),
        set_stock_operation(row[2], row[3]),
        row[4]
        ])
    pass


def export_yahoo_csv(segmented_stocks=[]):
    sheet = get_sheet_list(SHEET_PATH)

    with open('CSV/yahoo_FIIs_BR.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Symbol','Trade Date','Quantity','Purchase Price'])
        
        for sheet_row in sheet:
            if sheet_row[0].find('11') != -1:
                write_row_rules(writer, sheet_row)

    with open('CSV/yahoo_stocks_BR.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Symbol','Trade Date','Quantity','Purchase Price'])
        
        for sheet_row in sheet:
            if not sheet_row[0].replace('3F','3') in segmented_stocks and sheet_row[0].find('11') == -1:
                write_row_rules(writer, sheet_row)

    with open('CSV/yahoo_segmented_stocks_BR.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Symbol','Trade Date','Quantity','Purchase Price'])
        
        for sheet_row in sheet:
            if sheet_row[0].replace('3F','3') in segmented_stocks:
                write_row_rules(writer, sheet_row)

export_yahoo_csv()