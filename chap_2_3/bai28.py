import openpyxl
import matplotlib.pyplot as plt

wb_obj = openpyxl.load_workbook('./../data_sample/data_2_3/crosstab2.xlsx', data_only=True, read_only=True)
sheet_obj = wb_obj.active
m_row = sheet_obj.max_row
data = []
# x:
# min: 13, max 84, step: 20
# 10-29, 30-49, 50-69, 60-79, 80-99
# y:
# min: 21, max: 99, step: 20
# 40-59, 60-79, 80-99
data_input = {
    'X': {
        '10_29': 0,
        '30_49': 0,
        '50_69': 0,
        '60_79': 0,
        '80_99': 0,
    },
    'Y': {
        '40_59': 0,
        '60_79': 0,
        '80_99': 0,
    }
}


def import_data_array():
    for i in range(2, m_row + 1):
        cell_x_obj = sheet_obj.cell(row=i, column=2)
        cell_y_obj = sheet_obj.cell(row=i, column=3)

        if cell_x_obj.value and cell_y_obj.value is not None:
            cell_value = [cell_x_obj.value, cell_y_obj.value]
            data.append(cell_value)


def calc_data():
    for val in data:
        lbl_row = val[0]
        lbl_col = val[1]

        for key in data_input['X']:
            key_val_arr = str(key).split('_')
            key_val1 = int(key_val_arr[0])
            key_val2 = int(key_val_arr[1])

            if key_val1 <= lbl_row <= key_val2:
                data_input['X'][key] += 1

        for key in data_input['Y']:
            key_val_arr = str(key).split('_')
            key_val1 = int(key_val_arr[0])
            key_val2 = int(key_val_arr[1])

            if key_val1 <= lbl_col <= key_val2:
                data_input['Y'][key] += 1


def show_crosstab_data():
    fig, ax = plt.subplots(1, 1)
    ax.axis('tight')
    ax.axis('off')
    column_labels = ['', '40-59', '60-79', '80-99', 'Total']
    table_data = []


import_data_array()
calc_data()
