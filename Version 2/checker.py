index_count = open("index_classify", 'r')
index_count_all = index_count.read()
index_count_list = index_count_all.split("\n")

print("========= 0.01 ===========")
class_count = open("f_classify_0.01.txt", 'r')
class_count_all = class_count.read()
class_count_list = class_count_all.split("\n")

lister = []
count = 0
for x in range(len(index_count_list)):
    if (index_count_list[x] == class_count_list[x]):
        count += 1
        lister.append(index_count_list[x])

class_count.close()
print(count)
print(count/7539)

print("========= 0.1 ===========")
class_count = open("f_classify_0.1.txt", 'r')
class_count_all = class_count.read()
class_count_list = class_count_all.split("\n")
lister = []
count = 0
for x in range(len(index_count_list)):
    if (index_count_list[x] == class_count_list[x]):
        count += 1
        lister.append(index_count_list[x])
print(count)
print(count/7539)
class_count.close()

print("========= 0.2 ===========")
class_count = open("f_classify_0.2.txt", 'r')
class_count_all = class_count.read()
class_count_list = class_count_all.split("\n")
lister = []
count = 0
for x in range(len(index_count_list)):
    if (index_count_list[x] == class_count_list[x]):
        count += 1
        lister.append(index_count_list[x])
print(count)
print(count/7539)
class_count.close()

print("========= 0.5 ===========")
class_count = open("f_classify_0.5.txt", 'r')
class_count_all = class_count.read()
class_count_list = class_count_all.split("\n")
lister = []
count = 0
for x in range(len(index_count_list)):
    if (index_count_list[x] == class_count_list[x]):
        count += 1
        lister.append(index_count_list[x])
print(count)
print(count/7539)
class_count.close()

print("========= 1.0 ===========")
class_count = open("f_classify_1.txt", 'r')
class_count_all = class_count.read()
class_count_list = class_count_all.split("\n")
lister = []
count = 0
for x in range(len(index_count_list)):
    if (index_count_list[x] == class_count_list[x]):
        count += 1
        lister.append(index_count_list[x])
print(count)
print(count/7539)
class_count.close()
