import numpy as np
import matplotlib.pyplot as plt
import openpyxl


class ExportData14:
    # Number of class: 6
    # Class width: 2
    # 5-6, 7-8, 9-10, 11-12, 13-14, 15-16
    # min value: 6
    # max value: 15.8
    def __init__(self):
        self.wb_obj = openpyxl.load_workbook('./../data_sample/data_2_2/bai14.xlsx')
        self.data_input = {

        }
