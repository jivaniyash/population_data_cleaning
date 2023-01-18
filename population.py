# %%
import csv

# %%
with open('v1.csv','r',) as data:
    data_v1 = csv.reader(data)
    v1 = list(data_v1)
header = v1[0][1:]

# %%
d = {}
for row in range(1,len(v1)):
    if v1[row][1] == '' or v1[row][2] == '': # checks if member/family_id is empty
        continue
    member_id_set = set(v1[row][1].split(' | ')) # list of member_ids
    if v1[row][2] not in d: # check if family id not in dict
        d[v1[row][2]] = member_id_set # create new key with values as list of member_ids
    else:
        d[v1[row][2]].union(member_id_set) # add new member_id in existing family_id

# %%
with open('v1_final.csv','w',newline='') as data:
    v1_file = csv.writer(data)
    v1_file.writerow(header)
    for family_id in d:
        rows = [[member_id,family_id] for member_id in d[family_id]]
        v1_file.writerows(rows)

# %%
with open('v3.csv','r',) as data:
    data_v3 = csv.reader(data)
    v3 = list(data_v3)
header = v3[0][1:]

# %%
d = {}
for row in range(1,len(v3)):
    if v3[row][1] == '' or v3[row][2] == '': # checks if member/family_id is empty
        continue
    member_id_set = set(v3[row][1].strip('[]').strip('"').split(',')) # list of member_ids
    if v3[row][2] not in d: # check if family id not in dict
        d[v3[row][2]] = member_id_set # create new key with values as list of member_ids
    else:
        d[v3[row][2]].union(member_id_set) # add new member_id in existing family_id

# %%
with open('v3_final.csv','w',newline='') as data:
    v3_file = csv.writer(data)
    v3_file.writerow(header)
    for family_id in d:
        rows = [[member_id,family_id] for member_id in d[family_id]]
        v3_file.writerows(rows)


