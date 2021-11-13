import os
import csv
import numpy as np
import json



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

def cut_word(word,func):
    result=''
    temp = False
    word_temp=word
    temp = '\n' in word_temp
    
    while 1 :

        if False == temp:
            # print('in false',word_temp)
            if result == '':
                result=func(word_temp)
            else:
                result=result+'\n'+func(word_temp)
            return result

        elif True == temp:
            
            # cut word - search - save -change word
            if result == '':
                result=func(get_begin_2_word(word_temp,'\n'))
                
            else:
                result=result+'\n'+func(get_begin_2_word(word_temp,'\n'))
            word_temp=get_word_2_end(word_temp,'\n')
            # print('next=',word_temp)

        else:
            print('wrong.')
            return

        temp = '\n' in word_temp
    print('cut_word end')
    return 


def search_snd_dev(search_word):
    snd_mes=''
    with open('lib/lib_snd_dev.csv', mode='r') as f_search:
        reader = csv.reader(f_search)
        for row in reader:
            # print(row)
            if row[0] == search_word:
                snd_mes=row[0]+'  '+row[1]+'  '+row[2]
                print(snd_mes)
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
                print(snd_mes)
            if row[1] == search_word:
                snd_mes=row[1]+'  '+row[2]
                print(snd_mes)
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
                print(snd_mes)
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
                print(snd_mes)
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
                print(snd_mes)
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

def get_front_2_end (line, front):
        begin=line.find(front)+len(front)
        word=line[begin:]
        ss=word
        # print(ss)
        return ss

def get_test_time (file_name_1):
    time=get_front_2_last(file_name_1, '-', '.')
    time=time.replace('-',':')
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


def apply_file (file_name,num,row_x):

        f_log=open(file_name,'r', encoding='UTF-8')
        # f_log=open(file_name,'r',encoding='gbk',encoding='utf-8')


        line_log=f_log.readline()

        # set result[] to save value
        result_x=[]
        x=0
        for x in range(num):
            result_x.append('')


        time_handle=0       # judge if need to handle time
        time_status=0       # if need to handle time ,judge if line_log is up to time
        test_time=''


        time_in_filename="-" in file_name
        if True == time_in_filename:
            time_handle=1
            time_status=0
            test_time=get_test_time(file_name)
        else:
            time_handle=0


        while line_log:
                # print(line_log)
                if time_handle == 1:
                    
                    time_type=test_time in line_log
                    if True == time_type:
                        time_status=1
                    
                    if time_status == 0 :
                        line_log=f_log.readline()
                        continue
                
                
                
                temp=0
                for key in rows[1]:
                    a=key in line_log
                    if  True == a :
                        key_val=get_front_2_last(line_log,rows[2][temp],rows[3][temp])
                        # print("key_val=",key_val)
                        temp_x= key_val in result_x[temp]
                        if False == temp_x :
                            result_x[temp]=result_x[temp]+key_val+'\n'

                    temp=temp+1

                line_log=f_log.readline()  #read the next line

        f_log.close()

        x=0
        for x in range(num):
            temp=result_x[x]
            temp=temp.strip()
            result_x[x]=temp


        # zhuijia 0 weizhi zifuchuan
        result_x.insert(0,file_name)

        with open("result_key_word_snddevice.csv","a+", newline='\n') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(result_x)
            # writer.writerow(['a','b'])
            #写入多行用writerows
            # writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
        csvfile.close()

        return True

# get key word
with open('lib/key_word_snddevice.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
csvfile.close()

# global n
(m, n) = np.shape(rows)

# save headline
row_temp=rows[0]
row_temp.insert(0,'file_name')
# print(rows[1])
row_temp1=rows[1]
# print(rows[1])
row_temp1.insert(0,'keyword')
# print(rows[1])

with open("result_key_word_snddevice.csv","w", newline='\n') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(row_temp)
    writer.writerow(rows[1])
csvfile.close()

row_temp1.remove(rows[1][0])
print(rows[1])

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
                        apply_file(log_file,n,rows[0])
                        # print(get_test_time(log_file))












# print('----------- result to csv -----------')
# result_excel_name="2_result_key_word.csv"

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

