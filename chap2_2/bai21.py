import openpyxl
import matplotlib.pyplot as plt

wb_obj = openpyxl.load_workbook('./../data_sample/data_2_2/largecorp.xlsx')
sheet_obj = wb_obj.active
m_row = sheet_obj.max_row
data_corp = []
data_input = {
    '0_49': {
        'label': '0 - 49',
        'freq': 0,
        'per_freq': 0.0
    },
    '50_99': {
        'label': '50 - 99',
        'freq': 0,
        'per_freq': 0.0
    },
    '100_149': {
        'label': '100 - 149',
        'freq': 0,
        'per_freq': 0.0
    },
    '150_199': {
        'label': '150 - 199',
        'freq': 0,
        'per_freq': 0.0
    },
    '200_249': {
        'label': '200 - 249',
        'freq': 0,
        'per_freq': 0.0
    },
    '250_299': {
        'label': '250 - 299',
        'freq': 0,
        'per_freq': 0.0
    },
    '300_349': {
        'label': '300 - 349',
        'freq': 0,
        'per_freq': 0.0
    },
    '350_399': {
        'label': '350 - 399',
        'freq': 0,
        'per_freq': 0.0
    },
    '400_449': {
        'label': '400 - 449',
        'freq': 0,
        'per_freq': 0.0
    }
}


# Min 43
# Max 443
# Step: 50
# Start: 0
# 0 - 49
# 50 - 99
# 100 - 149
# 150 - 199
# 200 - 249
# 250 - 299
# 300 - 349
# 350 - 399
# 400 - 449
def import_data_array():
    for i in range(2, m_row + 1):
        cell_obj = sheet_obj.cell(row=i, column=2)

        if cell_obj.value is not None:
            data_corp.append(cell_obj.value)


import_data_array()
