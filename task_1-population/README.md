# Task-1_Popluation

This folder contains 3 files used to manipulate data using 3 different modules.

[pandas_cleaning.ipynb](https://github.com/jivaniyash/data_cleaning/blob/master/task_1-population/pandas_cleaning.ipynb) to read and manipulate data using pandas library.

[id_data.ipynb](https://github.com/jivaniyash/data_cleaning/blob/master/task_1-population/id_data.ipynb) uses [xlwings](https://www.xlwings.org/) to read and write xlsx file.

[csv_population.py](https://github.com/jivaniyash/data_cleaning/blob/master/task_1-population/csv_population.py) uses csv module to read and write data.

### Data properties
'fAST patents v1 vs. v3 comparison.xlsx' file is used in which 1st and 3rd sheet is to be considered.

Using string functions and dictionary & set object, member_id's are seperated from bundle.

Final output file is generated in such a way that in the data:
- No Null/None/Empty strings('') objects are present
- Each family_id contains 1 or more member_id
- All duplicates are removed
