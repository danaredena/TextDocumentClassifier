ind_list = open('index', 'r')
ind_all = ind_list.read()
ind_arr = ind_all.split()
ind_list.close()

cat_list = []
for x in range(1,len(ind_arr),2):
    cat_list.append(ind_arr[x])

cat_list.sort()

cat = list(set(cat_list))
cat.sort()
print(cat)
cat_count = []
for c in range(20):
    cat_count.append(cat_list.count(cat[c]))
print(cat_count)

cat_count_file = open( "cat_count.txt", 'w')
for y in range(20):
    cat_count_file.write(str(cat_count[y]) + "\n")
cat_count_file.close()
