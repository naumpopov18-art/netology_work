from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for i in range(1, len(contacts_list)):
    record = contacts_list[i]
    
    fio_string = " ".join(record[:3])
    
    fio_parts = fio_string.split()
    
    if len(fio_parts) >= 1:
        record[0] = fio_parts[0]
    if len(fio_parts) >= 2:
        record[1] = fio_parts[1]
    if len(fio_parts) >= 3:
        record[2] = fio_parts[2]

phone_pattern = r'(?:\+7|8)\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})'
add_pattern = r'(?:доб\.?|доп\.?)\s*(\d+)'

for i in range(1, len(contacts_list)):
    record = contacts_list[i]
    phone = record[5]
    
    if phone:
        main_match = re.search(phone_pattern, phone)
        if main_match:
            formatted_phone = f"+7({main_match.group(1)}){main_match.group(2)}-{main_match.group(3)}-{main_match.group(4)}"
            
            add_match = re.search(add_pattern, phone, re.IGNORECASE)
            if add_match:
                formatted_phone += f" доб.{add_match.group(1)}"
            
            record[5] = formatted_phone

unique_contacts = {}
headers = contacts_list[0]

for i in range(1, len(contacts_list)):
    record = contacts_list[i]
    lastname = record[0]
    firstname = record[1]
    
    key = (lastname, firstname)
    
    if key not in unique_contacts:
        unique_contacts[key] = record
    else:
        existing_record = unique_contacts[key]
        
        for j in range(len(record)):
            if not existing_record[j] and record[j]:
                existing_record[j] = record[j]
            elif j == 2 and not existing_record[2] and record[2]:
                existing_record[2] = record[2]

final_contacts_list = [headers]

for record in unique_contacts.values():
    final_contacts_list.append(record)

pprint(final_contacts_list)

# TODO 2: сохраняем получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts_list)
