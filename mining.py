#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

stock_data = []
#monthly_averages = []
monthly_averages = {}


def read_stock_data(stock_name, stock_file_name):
    with open(stock_file_name) as fr:
        contents = json.load(fr)
        mul=dict()
        vol=dict()
        for i in contents:
            date = datetime.datetime.strptime(i["Date"], "%Y-%m-%d")
            key = str(date.year)+"/"+str(date.month)
            if key not in mul.keys():
                mul[key]=[]
            if key not in vol.keys():
                vol[key]=[]
            if key not in monthly_averages.keys():
                monthly_averages[key]=0

            mul[key].append(i["Volume"]*i["Close"])
            vol[key].append(i["Volume"])
            monthly_averages[key] = sum(mul[key])/sum(vol[key])

        print(mul)
        print(vol)
        print(monthly_averages)
    return

read_stock_data("GOOG", "data/GOOG.json")
list_of_values = list(monthly_averages.values())
list_of_keys = list(monthly_averages.keys())

def six_best_months():

    list_of_best_six_values = sorted(list_of_values, reverse=True)[0:6]
    best_six_months = []
    for i in list_of_best_six_values:
        #print(i,list_of_keys[list_of_values.index(i)])
        #print(list_of_keys[list_of_values.index(i)],round(i,2))
        best_six_months.append((list_of_keys[list_of_values.index(i)],round(i,2)))
    print(best_six_months)
    return best_six_months
    #return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]

six_best_months()
def six_worst_months():
    list_of_worst_six_values = sorted(list_of_values)[:6]
    worst_six_months = []
    for i in list_of_worst_six_values:
        #print(i,list_of_keys[list_of_values.index(i)])
        #print(list_of_keys[list_of_values.index(i)],round(i,2))
        worst_six_months.append((list_of_keys[list_of_values.index(i)],round(i,2)))
    print(worst_six_months)
    return worst_six_months

    #return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]

six_worst_months()

def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

