


# ['describ', 'histori', 'oil', 'industri']
# 4
# 59190 : describ
# 95290 : histori
# 80442 : oil
# 74518 : industri
# 59190 : describ
# describ
# {'59190': [1852]}
# 95290 : histori
# histori
# {'59190': [1852], '95290': [2769, 5544, 8338, 11169, 14032, 16905, 19789, 22693, 25611, 29521]}
# 80442 : oil
# oil
# {'59190': [1852], '95290': [2769, 5544, 8338, 11169, 14032, 16905, 19789, 22693, 25611, 29521], '80442': [1144, 2296, 3454, 4655, 5860, 7075, 8297]}
# 74518 : industri
# industri
# {'59190': [1852], '95290': [2769, 5544, 8338, 11169, 14032, 16905, 19789, 22693, 25611, 29521], '80442': [1144, 2296, 3454, 4655, 5860, 7075, 8297], '74518': [938, 2086, 3395]}
#
# Process finished with exit code 0



# dic = {'59190': [1852],
#        '95290': [2769, 5544, 8338, 11169, 14032, 16905, 19789, 22693, 25611, 29521],
#        '80442': [1144, 2296, 3454, 4655, 5860, 7075, 8297]}

dic = {'59190': [1852],
       '80442': [1144, 1852, 3454, 4655, 5860, 7075, 8297]}



dic_keys = list(dic.keys())
len = len(dic_keys)

present = True

match_number = -2
for i in range(len-1):
    list1 = dic[dic_keys[i]]
    list2 = dic[dic_keys[i+1]]
    match_number = match_number + 1

    for item in list1:
        if match_number == -1:
            match_number = item + 1

        if match_number in list2:
            present = True
            break
        else:
            match_number = -1
            present = False

    if present == False:
        break


print(present)


my = ['work' , 'from' , 'home']


print(my[0])

for i in range(3-2):
    print(i)
# bi_word = []
#
# for k in range(len(my)-1):
#     i = 0
#     for item in my:
#         bi_word.append(item)
#         i = i + 1
#         if i == 2:
#             my.pop()
#         break
    #fucntion call




