import csv
import json

file = "C:\\Users\\karthick\\Downloads\\incomes.json"

with open(file) as train_file:
	dict_train = json.load(train_file)

dict_train_copy = []
for _ in dict_train:
	dict_copy = {}
	for key, value in _.items():
		if type(key) == unicode:
			key = key.encode('utf-8')
		if type(value) == unicode:
			value = value.encode('utf-8')
		dict_copy[key] = value
	dict_train_copy.append(dict_copy)

headers = ["incomeId","number","date","lastChangeDate","supplierArticle","techSize","barcode","quantity","totalPrice","dateClose","warehouseName","nmId"]
print(headers)
file_name = "D:\\dags\\incomes.csv"

with open(file_name, "w") as output_file:
	dict_writer = csv.DictWriter(output_file, headers,extrasaction='ignore')
	dict_writer.writeheader()
	dict_writer.writerows(dict_train_copy)