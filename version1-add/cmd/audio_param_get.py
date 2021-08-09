import os
import csv
import numpy as np
import json

def char2int (char):
    if char =='':
        print('no set choose 2')
        return 2
    elif char =='1':
        return 2
    elif char =='2':
        return 2
    elif char =='3':
        return 3
    elif char =='4':
        return 4
    return 2

def get_begin_2_word (line, word):
        # begin=line.find(front)+len(front)
        # word=line[begin:]
        # print(line)
        line=line.strip()
        end=line.find(word)
        # print('end=',end)
        # print("begin=",begin,"end=",end)
        ss=line[:end]
        # print(ss)
        return ss

def get_word_2_end (line, word):
        # begin=line.find(front)+len(front)
        # word=line[begin:]
        # print(line)
        line=line.strip()
        end=line.find(word)
        # print('end=',end)
        # print("begin=",begin,"end=",end)
        ss=line[end+1:]
        # print(ss)
        return ss

def search_fun (lib_file_name):

    
    return



def cut_word(word,lib_file_name, lib_word_num, search_word_line):
    print('word',word)
    result=''
    temp = False
    word_temp=word
    temp = '\n' in word_temp
    result_row=[]
    
    # cut word in cut_word_row[]
    while 1 :
        # word is none
        if word =='':
            break
        
        #print("word_temp====",word_temp)
        
        if False == temp:
            # no '\n' , maybe just one value
            result_row.append(word_temp)
            break
        elif True == temp:
            # not one line
            # cut word - search - save -change word
            result_row.append(get_begin_2_word(word_temp,'\n'))
            word_temp=get_word_2_end(word_temp,'\n')
            # print('next=',word_temp)
        else:
            print('wrong.')
            return ''

        temp = '\n' in word_temp
    #print("result_row",result_row)


    # open lib_file
    print('lib_file_name',lib_file_name)
    with open(lib_file_name, mode='r') as f_search:
        reader = csv.reader(f_search)
        lib_row = [row for row in reader]
        (temp_m, temp_n) = np.shape(lib_row)
        #print('temp_m',temp_m)
        #print('temp_n',temp_n)
        lib_search_line=0
        for temp_n_line in  range(temp_n):
            if lib_row[0][temp_n_line] == search_word_line:
                lib_search_line=temp_n_line
                print('search_word_line : ',search_word_line)
                print('match word in line',lib_search_line)

        for temp_value in result_row:
            print('temp_value******',temp_value)
            # if result != '':
            #     result=result+'\n'
            xx=''
            for temp_mm in range(temp_m):
                if temp_mm == 0:
                    continue
                #print('temp_mm',temp_mm)
                if temp_value == lib_row[temp_mm][lib_search_line]:
                    #print('find word')

                    for temp_word_num in range(lib_word_num):
                        #print(lib_word_num)
                        #print(temp_word_num)
                        
                        if xx == '':
                            xx=lib_row[temp_mm][temp_word_num]
                        else:
                            xx=xx+' '+lib_row[temp_mm][temp_word_num]
                    #print('xx',xx)
            if result == '':
                result=xx
            else:
                result=result+'\n'+xx
    f_search.close()


    # print("result")
    # print(result)
    # print('cut_word end')
    return result


def search_snd_dev(search_word):
    snd_mes=''
    with open('lib/lib_snd_dev.csv', mode='r') as f_search:
        reader = csv.reader(f_search)
        for row in reader:
            # print(row)
            if row[0] == search_word:
                snd_mes=row[0]+'  '+row[1]+'  '+row[2]
                #print(snd_mes)
    f_search.close()
    return snd_mes

def search_audio_dev(search_word):
    snd_mes=''
    with open('lib/lib_audio_dev.csv', mode='r') as f_search:
        reader = csv.reader(f_search)
        for row in reader:
            # print(row)
            if row[0] == search_word:
                snd_mes=row[0]+'  '+row[2]
                #print(snd_mes)
            if row[1] == search_word:
                snd_mes=row[1]+'  '+row[2]
                #print(snd_mes)
    f_search.close()
    return snd_mes

def search_acdb(search_word):
    snd_mes=''
    with open('lib/lib_acdb.csv', mode='r') as f_search:
        reader = csv.reader(f_search)
        for row in reader:
            # print(row)
            if row[0] == search_word:
                snd_mes=row[0]+'  '+row[1]
                #print(snd_mes)
    f_search.close()
    return snd_mes


def search_source_id(search_word):
    snd_mes=''
    with open('lib/lib_source.csv', mode='r') as f_search:
        reader = csv.reader(f_search)
        for row in reader:
            # print(row)
            if row[0] == search_word:
                snd_mes=row[0]+'  '+row[1]
                #print(snd_mes)
    f_search.close()
    return snd_mes

def search_app_type(search_word):
    snd_mes=''
    with open('lib/lib_app_type.csv', mode='r') as f_search:
        reader = csv.reader(f_search)
        for row in reader:
            # print(row)
            if row[0] == search_word:
                snd_mes=row[0]+'  '+row[1]
                #print(snd_mes)
    f_search.close()
    return snd_mes

def get_front_2_last (line, front, last):
        begin=line.find(front)+len(front)
        word=line[begin:]
        end=word.find(last)
        # print("begin=",begin,"end=",end)
        ss=word[:end]
        # print(ss)
        return ss

def get_time (line, front, last):
        begin=line.find(front)+len(front)
        word=line[begin-3:]
        end=word.find(last)
        # print("begin=",begin,"end=",end)
        ss=word[:end]+':'
        # print(ss)
        return ss

def get_front_2_end (line, front):
        begin=line.find(front)+len(front)
        word=line[begin:]
        ss=word
        # print(ss)
        return ss

def get_test_time (file_name_1):
    print(file_name_1)
    time=get_time(file_name_1, '-', '.')
    print(time)
    time=time.replace('-',':')
    print(time)
    return time

def search_row_id (row, key_word):
    search_id=''
    temp_id=0
    for search_id in row:
        if search_id == key_word:
            # print('temp_id = ',temp_id)
            return temp_id
        temp_id=temp_id+1
    return

def search_lib (result_value, num):
    #print(rows)
    #print("flie name",rows[0][num])
    lib_file_name='lib\\lib_'+rows[0][num]+'.csv'
    #print(lib_file_name)

    #print('rows[0][num]',rows[5][num])
    # rows[5][num] ='2' -> int 2

    x=char2int(rows[5][num])
    result_y=cut_word(result_value,lib_file_name,x, rows[0][num])
    #print("result_y",result_y)
    return result_y


def apply_file (file_name,num,row_x):

        f_log=open(file_name,'r',encoding='utf-8')
        # f_log=open(file_name,'r',encoding='gbk')

        # get log
        line_log=f_log.readline()

        # set result[num] to save value  result[num]={"file_name","value1","value2"...,"valuenum-1"}
        result_x=[]
        x=0
        for x in range(num):
            result_x.append('')
        #print("value num",num)

        # save file name
        result_x[0]=file_name

        # time jizhi
        time_handle=0       # judge if need to handle time
        time_status=0       # if need to handle time ,judge if line_log is up to time
        audio_status=0
        test_time=''

        time_in_filename="-" in file_name
        if True == time_in_filename:
            time_handle=1
            time_status=0
            test_time=get_test_time(file_name)
            print('test_time',test_time)
        else:
            time_handle=0

        #  # start 
        # key_value1_row=rows[1]
        # key_value1_row=del(key_value1_row[0])
        # print("key_value1_row",key_value1_row)

        # key_value2_row=rows[2]
        # key_value2_row=del(key_value2_row[0])
        # print("key_value2_row",key_value2_row)



        # start to get value
        while line_log:
                #print(line_log)
                #print('--------------line_log-------------')
                # if now after the time in file name XX-XX ,while pass line
                if time_handle == 1:
                    time_type=test_time in line_log
                    if True == time_type:
                        time_status=1
                        #print(line_log)
                    audio_type= 'adev_open_input_stream: enter: flags' in line_log
                    if True == audio_type:
                        audio_status=1
                    
                    
                    if time_status == 0 :
                        line_log=f_log.readline()
                        continue
                    if audio_status == 0 :
                        line_log=f_log.readline()
                        continue
                
                #print("in time")
                temp=1
                # temp start with 1 because 0 is the head line to explain meaning
                # key is key_value1
                #print(n)
                for temp_key_num in range(num):
                    key_value1=rows[1][temp_key_num]
                    #print('num-----',temp_key_num)
                    #print("key_value1",key_value1)
                    if key_value1 == "key_word1" :
                        #print("list head key1")
                        continue
                    
                    # start set key status
                    key_word1_status=False
                    key_word2_status=False

                    key_word1_status= key_value1 in line_log
                    if  True == key_word1_status :
                        #print("key word1 is yes ")
                        # 1. key_word1 is in log_line, get judge key_word2 is set?
                        if rows[2][temp_key_num] == '':
                            #print("key word2 is no ")
                            key_word2_status = True
                        else:
                            #print("key word2 is yes ")
                            #print('line_log',line_log)
                            #print('key2',rows[2][temp_key_num])
                            key_word2_status = rows[2][temp_key_num] in line_log
                            
                        if key_word2_status == False:
                            #print("key word2 is not support")
                            continue
                        
                        #print("log--",line_log)
                        # get key value 
                        key_val=get_front_2_last(line_log,rows[3][temp_key_num],rows[4][temp_key_num])
                        #print("key_val=",key_val)
                        temp_x= key_val in result_x[temp_key_num]
                        if False == temp_x :
                            if result_x[temp_key_num] == '':
                                result_x[temp_key_num]=key_val
                            else:
                                result_x[temp_key_num]=result_x[temp_key_num]+'\n'+key_val 

                    temp=temp+1

                line_log=f_log.readline()  #read the next line

        f_log.close()

        print('--------file name-------')
        print(result_x[0])

        

        for result_num in range(num) :
            #print('----')
            #print(result_x[result_num])
            m=''
            if result_num == 0:
                continue

            print('--------result-------')
            m=search_lib(result_x[result_num], result_num)
            #print('m',m)
            result_x[result_num]=m
            
            print(m)
            #result_x[num]=m

        #print("result_x",result_x)
        # for result_num in range(num) :
        #     result_x[num]
        # x=0
        # for x in range(num):
        #     temp=result_x[x]
        #     temp=temp.strip()
        #     result_x[x]=temp



        with open("result_audio_param.csv","a+", newline='\n') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(result_x)
            # writer.writerow(['a','b'])
            #写入多行用writerows
            # writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
        csvfile.close()

        return True




# get key word
with open('lib/key_word.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
csvfile.close()

# global n
(m, n) = np.shape(rows)
#print("m",m,"n",n)
value_number=n
# n-1 is how many of value ,the row[X][0] is the head line

#print(rows)

# save headline
row_temp0=rows[0]
row_temp0[0]='file_name'
print(row_temp0)
# print(rows[1])
row_temp1=rows[1]
row_temp2=rows[2]

with open("result_audio_param.csv","w", newline='\n') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(row_temp0)
    writer.writerow(row_temp1)
    writer.writerow(row_temp2)
csvfile.close()


print("rows",rows)

# resolve file dir
resultdir="usecase_result"

for root, dirs, files in os.walk(resultdir):
        for f in files:

                a = "pass" in root
                if a == True :
                        continue
                    
                temp='.txt' in f
                if temp == True :
                        file_path=root
                        log_file=os.path.join(root, f)                  #log_file path\filename
                        print(log_file)
                        apply_file(log_file,value_number,rows[0])
                        # print(get_test_time(log_file))












# print('----------- result to csv -----------')
# result_excel_name="2_result_audio_param.csv"

# if not os.path.isfile(result_excel_name) :
#         print('not',result_excel_name)
# else:
#         print('delete ',result_excel_name)
#         os.remove(result_excel_name)





# field_order = ['file_name','usecase', 'usecase_path', 'p_flags', 'p_audio_device', 'p_acdb_id', 'c_source', 'c_audio_device', 'c_acdb_id',  'snd_device_id']
# with open(result_excel_name, 'a', encoding="utf-8", newline='') as csvfile:
#         # print('delete csv file content')
#         # csvfile.truncate()                    # delete file contect

#         writer = csv.DictWriter(csvfile, field_order)
#         writer.writeheader()
# csvfile.close()

# resultdir="usecase_result"
# for root, dirs, files in os.walk(resultdir):
#         for f in files:
#                 temp='.txt' in f
#                 if temp == True :
#                         file_path=root
#                         log_file=os.path.join(root, f)                  #log_file path\filename

#                         apply_file(log_file)

