import json


customer = {
    "id": 12345,
    "name": "안준영",
    "history": [
        {"date" : "2024-06-17", "product" : "iPhone 14 Pro"},
        {"date" : "2024-06-18", "product" : "Galaxy s24 Ultra"},
    ]
}

json_string = json.dumps(customer, ensure_ascii = False)
print((json_string))


# jsonString = '''{"name" : "KH", "id" : 123456, "history" : [
#     {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
#     {"date" : "2023-05-24", "item" : "Galuxy S23 Ultra"}
# ]}'''
#
# dict = json.loads(jsonString) #딕셔너리로 변경

# print(dict["name"])
# for h in dict["history"]:
#     print(h["date"], h["item"])

# import csv
#
# f = open('output.csv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(f)
# wr.writerow([1, "안준영", False])
# wr.writerow([2, "고길동", False])
# f.close()