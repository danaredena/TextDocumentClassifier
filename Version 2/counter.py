import os
import re
ind_list = open('index', 'r')
ind_all = ind_list.read()
ind_arr = ind_all.split()
ind_list.close()

ex_list = open('exception.txt', 'r')
ex_all = ex_list.read()
ex_arr = ex_all.split()
ex_list.close()

cat_dict = {'alt.atheism':0, 'comp.graphics':1, 'comp.os.ms-windows.misc':2,
'comp.sys.ibm.pc.hardware':3, 'comp.sys.mac.hardware':4, 'comp.windows.x':5,
'misc.forsale':6, 'rec.autos':7, 'rec.motorcycles':8, 'rec.sport.baseball':9,
'rec.sport.hockey':10, 'sci.crypt':11, 'sci.electronics':12, 'sci.med':13, 'sci.space':14,
'soc.religion.christian':15, 'talk.politics.guns':16, 'talk.politics.mideast':17,
'talk.politics.misc':18, 'talk.religion.misc':19}

dict_list = open('f-dictionary.txt', 'r')
dict_all = dict_list.read()
dict_arr = dict_all.split()
dict_list.close()

def char_check(char):
    if (char.isalpha()):
        return True
    if (char.isdigit()):
        return True
    return False

def pre_word(word):
    if (word==""):
        return ""
    while (char_check(word[-1]) == False):
        if (len(word) == 1):
            return ""
        word = word[:-1]

    while (char_check(word[0]) == False):
        if (len(word) == 1):
            return ""
        word = word[1:]
    return word.lower()

def bin_search(word, word_array):
    i = 0
    j = len(word_array) - 1
    while (j >= i):
        mid = int((i+j)/2)
        if (word_array[mid] == word):
            return mid
        if (max(word, word_array[mid]) == word):
            i = mid + 1
        else:
            j = mid - 1
    return False

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data/"
dir_path = os.path.join(script_dir, rel_path)

def readFile(filename):
    textfile = open(filename)
    text_all = textfile.read()
    textfile.close()
    splitter = re.split("[\s,]",text_all)
    text_arr = []
    for x in range(len(splitter)):
        word = pre_word(splitter[x])
        if (word != "" and bin_search(word, ex_arr) == False):
            text_arr.append(word)
    text_arr = list(set(text_arr))
    text_arr.sort()
    return text_arr

master_counter = []
for i in range(len(dict_arr)):
    master_counter.append([])

for count in range(11307):
    file_path = os.path.join(dir_path, str(count))
    text_arr = readFile(file_path)
    cat = ind_arr[2*count+1]
    catnum = cat_dict[cat]
    for x in range(0,len(text_arr)):
        if (text_arr[x].isalpha()):
            d = bin_search(text_arr[x],dict_arr)
            if (d != False): #finds word in dict
                master_counter[d].append(catnum)
        elif (re.match(r'[a-z]+((\-|_)[a-z]+)+$', text_arr[x])):
            d = bin_search(text_arr[x],dict_arr)
            if (d != False): #finds word in dict
                master_counter[d].append(catnum)
        '''
        elif (re.match(r'[0-9]+--[0-9]+$', text_arr[x])):
            master_counter[17].append(catnum)
            #_n--n_
        elif (re.match(r'[0-9]+-[0-9]+$', text_arr[x])):
            master_counter[20].append(catnum)
            #_n-n_
        elif (re.match(r'(([0-9]{4})|([0-9]{1,2}))-[0-9]{1,2}-(([0-9]{4})|([0-9]{1,2}))$', text_arr[x])):
            master_counter[5].append(catnum)
            #_date-_
        elif (re.match(r'[0-9]{3}-[0-9]{3}-[0-9]{4}$', text_arr[x])):
            master_counter[26].append(catnum)
            #_tel_
        elif (re.match(r'[0-9]{3}-[0-9]{2}-[0-9]{2}$', text_arr[x])):
            master_counter[26].append(catnum)
            #_tel_
        elif (re.match(r'[0-9]{3}-[0-9]{4}-[0-9]{2}$', text_arr[x])):
            master_counter[25].append(catnum)
            #_serial_
        elif (re.match(r'[0-9]+-[0-9]+-[0-9]+$', text_arr[x])):
            master_counter[19].append(catnum)
            #_n-n-n_
        elif (re.match(r'[0-1]-[0-9]+-[0-9]+-[0-9]$', text_arr[x])):
            master_counter[14].append(catnum)
            #_isbn_
        elif (re.match(r'1-[0-9]{3}-[0-9]{3}-[0-9]{4}$', text_arr[x])):
            master_counter[12].append(catnum)
            #_fax_
        elif (re.match(r'[0-9]+(-[0-9]+)+$', text_arr[x])):
            master_counter[18].append(catnum)
            #_n-n+_
        elif (re.search(r'mb/s$', text_arr[x])):
            master_counter[15].append(catnum)
            #_mb/s_
        elif (re.match(r'[0-9]+\.?[0-9]*\"x[0-9]', text_arr[x])):
            master_counter[7].append(catnum)
            #_dimen_
        elif (re.search(r'/each$', text_arr[x])):
            master_counter[9].append(catnum)
            #_each_
        elif (re.search(r'mph$', text_arr[x])):
            master_counter[16].append(catnum)
            #_mph_
        elif (re.match(r'[0-1]{8}b', text_arr[x])):
            master_counter[4].append(catnum)
            #_bin_
        elif (re.match(r'(([0][0-9])|([1][0-2]))(:[0-6][0-9]){1,2}(pm)?(am)?$', text_arr[x])):
            master_counter[27].append(catnum)
            #_time_
        elif (re.match(r'(([0-1][0-9])|([2][0-4]))(:[0-6][0-9]){1,2}(pm)?(am)?$', text_arr[x])):
            master_counter[27].append(catnum)
            #_time_
        elif (re.match(r'[0-9]+(:[0-9]+)+$', text_arr[x])):
            master_counter[22].append(catnum)
            #_n:n+_
        elif (re.match(r'[a-z0-9][^@]+@[a-z]+-?[a-z]+\.[a-z]+$', text_arr[x])):
            master_counter[10].append(catnum)
            #_email_
        elif (re.match(r'(([0-9]{4})|([0-9]{1,2}))/[0-9]{1,2}/(([0-9]{4})|([0-9]{1,2}))$', text_arr[x])):
            master_counter[6].append(catnum)
            #_date/_
        elif (re.match(r'[0-9]+(/[0-9]+)+$', text_arr[x])):
            master_counter[21].append(catnum)
            #_n/n+_
        elif (re.match(r'[0-9]+h$', text_arr[x])):
            master_counter[23].append(catnum)
            #_nh_
        elif (re.search(r'\"pne', text_arr[x])):
            master_counter[24].append(catnum)
            #_pne_
        elif (re.search(r'f9', text_arr[x])):
            master_counter[11].append(catnum)
            #_f9_
        elif (re.search(r'@\(\"', text_arr[x])):
            master_counter[1].append(catnum)
            #_@_
        elif (re.search(r'b8', text_arr[x])):
            master_counter[2].append(catnum)
            #_b8_
        elif (re.match(r'[x][a-z]+\(', text_arr[x])):
            master_counter[28].append(catnum)
            #_x(_
        elif (re.search(r'bhj',text_arr[x])):
            master_counter[3].append(catnum)
            #_bhj_
        elif (re.search(r'7e', text_arr[x])):
            master_counter[0].append(catnum)
            #_7e_
        elif (re.match(r'[a-z_\-]+(\.[a-z_\-]+)+$', text_arr[x])):
            master_counter[8].append(catnum)
            #_dots_
        elif (re.match(r'[a-z_\-]+\([a-z0-9_@&\-\$]+$', text_arr[x])):
            master_counter[13].append(catnum)
            #_func_
        '''
counter = open('occ_count.txt','w')
final_dict = open('f-dictionary.txt','w')
for x in range(len(master_counter)):
    count_file = 0
    for z in range(20):
        occ = master_counter[x].count(z)
        count_file += occ
    if (count_file > 0):
        #print(dict_arr[x])
        final_dict.write(dict_arr[x]+"\n")
        for y in range(20):
            occ = master_counter[x].count(y)
            counter.write(str(occ) + " ")
        counter.write("\n")
final_dict.close()
counter.close()
