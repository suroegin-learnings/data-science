import csv
import pandas as pd
from datetime import date
from os import remove

ready_list = list()
with open("axelname_freeing_export.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    chars = set('рф-0123456789')
    for row in reader:
        if row[1] == "Возраст":
            row[1] = "Age"
            row.append("Len")
            continue
        if any((c in chars) for c in row[0]):
            pass
        else:
            if len(row[0])-3 < 14:
                row[1] = int(row[1])
                row.append(len(row[0])-3)
                ready_list.append(row)
df = pd.DataFrame(ready_list)
df_new = df.sort_values([1, 6], ascending=[False, True])
_date = date.today()
df_new.to_excel('axelname_freeing_{0}.{1}.{2}.xlsx'.format(_date.day, _date.month, _date.year))
remove("axelname_freeing_export.csv")