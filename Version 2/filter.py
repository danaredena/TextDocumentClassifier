import re
dict_list = open('dictionary_sorted.txt', 'r')
dict_all = dict_list.read()
dict_arr = dict_all.split()
dict_list.close()

dictionary = open("filtered.txt", 'w')

print(len(dict_arr))
for x in range(len(dict_arr)):
    print(x)
    if (dict_arr[x].isalpha()):
        dictionary.write(dict_arr[x]+"\n")
    elif(re.match("[a-z]+((\-|_)[a-z]+)+$", dict_arr[x])):
        dictionary.write(dict_arr[x]+"\n")
        #print(dict_arr[x])
    '''
    elif (re.match("[0-9]+--[0-9]+$", dict_arr[x])):
        dictionary.write("_n--n_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]+-[0-9]+$", dict_arr[x])):
        dictionary.write("_n-n_"+"\n")
        #print(dict_arr[x])
    elif (re.match("(([0-9]{4})|([0-9]{1,2}))-[0-9]{1,2}-(([0-9]{4})|([0-9]{1,2}))$", dict_arr[x])):
        dictionary.write("_date-_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]{3}-[0-9]{3}-[0-9]{4}$", dict_arr[x])):
        dictionary.write("_tel_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]{3}-[0-9]{2}-[0-9]{2}$", dict_arr[x])):
        dictionary.write("_tel_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]{3}-[0-9]{4}-[0-9]{2}$", dict_arr[x])):
        dictionary.write("_serial_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]+-[0-9]+-[0-9]+$", dict_arr[x])):
        dictionary.write("_n-n-n_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-1]-[0-9]+-[0-9]+-[0-9]$", dict_arr[x])):
        dictionary.write("_isbn_"+"\n")
        #print(dict_arr[x])
    elif (re.match("1-[0-9]{3}-[0-9]{3}-[0-9]{4}$", dict_arr[x])):
        dictionary.write("_fax_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]+(-[0-9]+)+$", dict_arr[x])):
        dictionary.write("_n-n+_"+"\n")
        #print(dict_arr[x])
    elif (re.search("mb/s", dict_arr[x])):
        dictionary.write("_mb/s_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]+\.?[0-9]*\"x[0-9]", dict_arr[x])):
        dictionary.write("_dimen_"+"\n")
        #print(dict_arr[x])
    elif (re.search("/each$", dict_arr[x])):
        dictionary.write("_each_"+"\n")
        #print(dict_arr[x])
    elif (re.search("mph$", dict_arr[x])):
        dictionary.write("_mph_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-1]{8}b", dict_arr[x])):
        dictionary.write("_bin_"+"\n")
        #print(dict_arr[x])
    elif (re.match("(([0][0-9])|([1][0-2]))(:[0-6][0-9]){1,2}(pm)?(am)?$", dict_arr[x])):
        dictionary.write("_time_"+"\n")
        #print(dict_arr[x])
    elif (re.match("(([0-1][0-9])|([2][0-4]))(:[0-6][0-9]){1,2}(pm)?(am)?$", dict_arr[x])):
        dictionary.write("_time_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]+(:[0-9]+)+$", dict_arr[x])):
        dictionary.write("_n:n+_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[a-z0-9][^@]+@[a-z]+-?[a-z]+\.[a-z]+$", dict_arr[x])):
        dictionary.write("_email_"+"\n")
        #print(dict_arr[x])
    elif (re.match("(([0-9]{4})|([0-9]{1,2}))/[0-9]{1,2}/(([0-9]{4})|([0-9]{1,2}))$", dict_arr[x])):
        dictionary.write("_date/_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]+(/[0-9]+)+$", dict_arr[x])):
        dictionary.write("_n/n+_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[0-9]+h$", dict_arr[x])):
        dictionary.write("_nh_"+"\n")
        #print(dict_arr[x])
    elif (re.search("\"pne", dict_arr[x])):
        dictionary.write("_pne_"+"\n")
        #print(dict_arr[x])
    elif (re.search("f9", dict_arr[x])):
        dictionary.write("_f9_"+"\n")
        #print(dict_arr[x])
    elif (re.search("@\(\"", dict_arr[x])):
        dictionary.write("_@_"+"\n")
        #print(dict_arr[x])
    elif (re.search("b8", dict_arr[x])):
        dictionary.write("_b8_"+"\n")
    elif (re.match("[x][a-z]+\(", dict_arr[x])):
        dictionary.write("_x(_"+"\n")
        #print(dict_arr[x])
    elif (re.search("bhj", dict_arr[x])):
        dictionary.write("_bhj_"+"\n")
        #print(dict_arr[x])
    elif (re.search("7e", dict_arr[x])):
        dictionary.write("_7e_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[a-z_\-]+(\.[a-z_\-]+)+$", dict_arr[x])):
        dictionary.write("_dots_"+"\n")
        #print(dict_arr[x])
    elif (re.match("[a-z_\-]+\([a-z0-9_@&\-\$]+$", dict_arr[x])):
        dictionary.write("_func_"+"\n")
    '''
dictionary.close()
