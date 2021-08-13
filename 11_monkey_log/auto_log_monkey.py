import csv
import io
import os
import shutil


path='monkey_result'

shutil.rmtree(path) 

num_finish=0
num_abort=0
num_no_event=0

def get_front_2_last (line, front, last):
        begin=line.find(front)+len(front)
        end=line.find(last)
        ss=line[begin:end]
        # print(ss)
        return ss

#func-1 get app name
def get_app_name (line):
        begin=line.find(': com')+2
        end=line.find(' (pid')
        ss=line[begin:end]
        # print(ss)
        return ss


#------------------------ func1/2 to create result_log ------------------------

# New tombstone found

# func1 analysis file--ok
def key_value_analysis(file_name_key,file_name_log,file_name_result):

        tombstone_status=False

        file_key_value=open(file_name_key)
        file_log=io.open(file_name_log,encoding='utf-8')
        file_key_result=open(file_name_result,"w")#use w just save 1 char

        line_log=file_log.readline()

        while line_log:
                #func2{
                file_key_value.seek(0, 0)
                key_value=file_key_value.readline()
                while key_value:
                        key=key_value.strip()           # delete '\n'
                        result_a=key in line_log
                        if result_a == True :
                                break
                        key_value=file_key_value.readline()
                if result_a == True :
                        file_key_result.write(line_log)     #copy one line

                # add tombstone 

                if False == tombstone_status:
                        temp_tomb=':Sending' in line_log
                        if True == temp_tomb:
                                tombstone_status=True
                        else:
                                tombstone_status=False
                if True == tombstone_status:
                        temp_tomb_value='New tombstone found' in line_log
                        if True == temp_tomb_value:
                                file_key_result.write(line_log)
                                # print(line_log)

                line_log=file_log.readline()  #read the next line
                #func2}

        file_log.close
        file_key_value.close
        file_key_result.close

        return 'a'


# ------------------------ func10 get tombstone message ------------------------
def get_tomb_mes (file_name, result_file_name) :
        print('in get_tomb_mes')
        print('file_name',file_name)
        print('result_file_name',result_file_name)
        # f_tomb_name=open(file_name,'r')
        f_tomb_name=open(file_name)
        f_tomb_res_name=open(result_file_name,"a")     #zhuijiamoshi

        f_tomb_res_name.write('\n')
        f_tomb_res_name.write(file_name)
        f_tomb_res_name.write('\n')

        line_log=f_tomb_name.readline()

        while line_log:
                temp='pid' in line_log
                if True == temp:
                        f_tomb_res_name.write(line_log)

                line_log=f_tomb_name.readline()


        f_tomb_name.close()
        f_tomb_res_name.close()
        return





#------------------------ func3/4 to create result_csv ------------------------

# func3 judge one hot_word in line and save to value--ok
# hot_word_filename=file_name
def apply_file (file_name, result_excel_name):
        hot_word_crash="// CRASH:"
        hot_word_notresp="NOT RESPONDING:"
        hot_word_tombstone="New tombstone found"
        hot_word_abort="** Monkey aborted due to error."                #3 status
        hot_word_finish="// Monkey finished"                #3 status
        hot_word_cmd="args: ["

        hot_word_crash_status=0
        hot_word_anr_status=0
        crash_mes=''
        anr_mes=''

        # judge priority crash > despond > tombstone > abort > finish
        f_name=io.open(file_name,encoding='utf-8')
        line_log=f_name.readline()
        value_crash=""
        value_despond=""
        value_tombstone=""
        value_abort=False
        value_finish=False
        value_status=""
        value_cmd=""




        while line_log:

                a=hot_word_crash in line_log
                if  True == a :
                        # send and sleeping case
                        tem_b=':Sending' in line_log
                        tem_c='Sleeping' in line_log
                        tem_d=tem_b+tem_c

                        if True == tem_b:
                                # print("have sending ")
                                begin=line_log.find(':Sending')
                                end=line_log.find('// CRASH:')
                                if begin > end:
                                        ss=line_log[end:begin]
                                        line_log=ss+'\n'
                                else:
                                        ss=line_log[begin:end+1]
                                        line_log=line_log.replace(ss,'/')
                                # print('begin',begin)
                                # print('end',end)
                                # print(ss)

                        if True == tem_c:
                                # print("have sleeping")
                                begin=line_log.find('Sleeping')
                                end=line_log.find('// CRASH:')
                                if begin > end:
                                        ss=line_log[end:begin]
                                        line_log=ss+'\n'
                                else:
                                        ss=line_log[begin:end+1]
                                        line_log=line_log.replace(ss,'/')
                                # print('begin',begin)
                                # print('end',end)
                                # print(ss)
                        hot_word_crash_status=1
                        
                                
                        temp=get_app_name(line_log)+'\n'
                        value_crash=value_crash+temp
                        # print(value_crash)
                else:
                        a=hot_word_notresp in line_log
                        if True == a : 
                                
                                # value_despond=value_despond+get_app_name(line_log)
                                temp=get_app_name(line_log)+'\n'
                                value_despond=value_despond+temp

                                hot_word_anr_status=1

                        else :
                                
                                a=hot_word_tombstone in line_log
                                if  True == a :
                                        
                                        # print(value_crash)

                                        # get tombstone message
                                        begin=line_log.find('tombstone_')
                                        end=line_log.find(',')
                                        file_tomb_name=line_log[begin:end]
                                        # print('file name is ',file_name)
                                        file_tomb_path=file_name.replace('monkey_result','monkey_log')
                                        temp_file_name=os.path.basename(file_name)
                                        # bottom=file_tomb_path.find('\log_')# quition
                                        # file_tomb_path_name=file_tomb_path[0:bottom+1]+file_tomb_name+'.txt'
                                        # file_tomb_path_name=file_tomb_path[0:bottom+1]+file_tomb_name
                                        file_tomb_path_name=file_tomb_path.replace(temp_file_name,file_tomb_name)
                                        file_tomb_res_path=file_tomb_path_name.replace('monkey_log','monkey_result')+'.txt'
                                        # file_tomb_path_name=
                                        print('tomb file is',file_tomb_name)
                                        print('tomb path is',file_tomb_path)
                                        print('tomb path and file',file_tomb_path_name)
                                        print('file_tomb_res_path',file_tomb_res_path)
                                        # get_tomb_mes(file_tomb_path_name, file_tomb_res_path)
                                        print(file_tomb_path_name)
                                        f_exit=os.path.exists(file_tomb_path_name)
                                        if True == f_exit:
                                                get_tomb_mes(file_tomb_path_name, 'tombstone.txt')
                                        else:
                                                print('loss suit tombstone.')
                                        value_tombstone=value_tombstone+file_tomb_path_name+'\n'

                                else:
                                        
                                        a=hot_word_abort in line_log
                                        # print('finish is ', a)
                                        if  True == a :
                                                value_abort=True
                                                global num_abort
                                                num_abort=num_abort+1


                                                value_status="monkey abort"
                                                # print(value_crash)
                                        else:

                                                a=hot_word_finish in line_log
                                                # print('finish is ', a)
                                                if  True == a :
                                                        value_finish=True
                                                        global num_finish
                                                        num_finish=num_finish+1
                                                        value_status="monkey finish"
                                                        # print(value_crash)
                                                # else:
                                                #         print("nothing line")

                a=hot_word_cmd in line_log
                if True == a:
                        value_cmd=get_front_2_last(line_log, hot_word_cmd, ']')

                temp_crash_mes="// Build Label" in line_log
                if True == temp_crash_mes:
                        hot_word_crash_status=0

                if hot_word_crash_status == 1:
                        crash_mes=crash_mes+line_log

                if hot_word_anr_status == 1:
                        anr_mes=anr_mes+line_log

                temp_anr_mes="Reason:" in line_log
                if True == temp_anr_mes:
                        hot_word_anr_status=0

                line_log=f_name.readline()  #read the next line
        
        crash_mes=crash_mes.strip()
        anr_mes=anr_mes.strip()

        temp_status_x=value_abort+value_finish
        # print(temp_status_x)
        if temp_status_x == False:
                value_status="monkey not get event"
                print("monkey not get event")
                global num_no_event
                num_no_event=num_no_event+1

        print('\n')
        print('file_name ---- ',file_name)
        #print result to csv file
        print("value_crash : ")
        print(value_crash)

        print("value_despond : ")
        print(value_despond)

        print("value_tombstone : ")
        print(value_tombstone)

        print("value_status : ",value_status)

        print("value_cmd : ",value_cmd)

        print('\n')

        

        # mix file name from crash1.txt too crash01.txt {
        flie_name_key=io.open('cmd/file_name_1_2_01.txt',encoding='utf-8')

        flie_name_key_replace=io.open('cmd/file_name_1_2_01_replace.txt',encoding='utf-8')
        temp_f_name_key_line=flie_name_key.readline()
        temp_f_name_key_line_replace=flie_name_key_replace.readline()

        
        while temp_f_name_key_line:
                temp_f_name_key_line=temp_f_name_key_line.strip()          # delete '\n'
                temp_f_name_key_status=temp_f_name_key_line in file_name
                # temp_f_name_key_status='crash9.txt' in file_name

                # print("---------------------")
                # print("key=",temp_f_name_key_line)
                # print("status=",temp_f_name_key_status)
                # print("file_name=",file_name)

                # print("file_name=",file_name)
                # print("key=",temp_f_name_key_line)
                # print("status=",temp_f_name_key_status)
                # print("replace=",temp_f_name_key_line_replace)

                if temp_f_name_key_status == True:
                        file_name=file_name.replace(temp_f_name_key_line,temp_f_name_key_line_replace)
                        # file_name=file_name.replace("crash9.txt","crash09.txt")
                        # print("file_name=",file_name)
                #read next name
                temp_f_name_key_line_replace=flie_name_key_replace.readline()
                temp_f_name_key_line=flie_name_key.readline()

        flie_name_key.close()
        flie_name_key_replace.close()
        # } mix file name from crash1.txt too crash01.txt




        value_crash=value_crash.strip()
        value_despond=value_despond.strip()
        value_tombstone=value_tombstone.strip()
        file_name=file_name.strip()
        field_order = ["path_file", 'monkey_status', 'crash_app' , 'crash_mes', 'not_respond_app', 'anr_mes','tombstone' ,  'monkey_cmd']
        with open(result_excel_name, 'a+') as csvfile:
                writer = csv.DictWriter(csvfile, field_order)
                # writer.writeheader()
                # writer.writerow(dict(zip(field_order, [file_name, value_status, value_crash, value_despond, value_tombstone])))
                writer.writerow(dict(zip(field_order, [file_name, value_status,  value_crash, crash_mes , value_despond, anr_mes , value_tombstone, value_cmd])))

        csvfile.close()
        f_name.close()
        return True



#func2 analysis monkey_log to result_log--ok
import os
print('----------- log to result -----------')
logdir="monkey_log"
resultdir="monkey_result"
file_name_key="cmd/key_value_monkey.txt"

print('delete resultdir')
# os.removedirs(resultdir)        # digui delete file
if not os.path.isfile('tombstone.txt') :
        print('not tombstone.txt')
else:
        print('delete tombstone.txt')
        os.remove('tombstone.txt')

if not os.path.isdir(resultdir):
        os.makedirs(resultdir)



for root, dirs, files in os.walk(logdir):
        for f in files:
                file_path=root
                log_file=os.path.join(root, f)                  #log_file path\filename
                file_path=file_path.replace(logdir,resultdir)   #result_file path
                if not os.path.isdir(file_path):
                        os.makedirs(file_path)
                result_path = os.path.join(file_path, f)        #result_file path\name


                print('resolve file name is ',root,f)
                file_type_key='.txt'
                file_type=file_type_key in f
                if False == file_type:
                        print('not txt file')
                        continue

                result_file=open(result_path,'w')               #create result_file
                res=key_value_analysis(file_name_key,log_file,result_path)      #analysis log_file to result_file
                
                result_file.close()
                print(res)
                if res =='b':
                        continue


# func4 result_log file to csv
import os
print('----------- result to csv -----------')
resultdir="monkey_result"
result_excel_name="result_monkey_status.csv"

if not os.path.isfile(result_excel_name) :
        print('not',result_excel_name)
else:
        print('delete ',result_excel_name)
        os.remove(result_excel_name)

field_order = ["path_file", 'monkey_status', 'crash_app' ,'crash_mes', 'not_respond_app', 'anr_mes',  'tombstone', 'monkey_cmd']
with open(result_excel_name, 'wb') as csvfile:
        # print('delete csv file content')
        # csvfile.truncate()                    # delete file contect

        writer = csv.DictWriter(csvfile, field_order)
        writer.writeheader()
csvfile.close()

for root, dirs, files in os.walk(resultdir):
        for f in files:
                temp='.txt' in f
                if temp == True :
                        file_path=root
                        log_file=os.path.join(root, f)                  #log_file path\filename

                        apply_file(log_file, result_excel_name)


print('monkey finish num is ',num_finish)
print('monkey abort num is ',num_abort)
print('monkey no event num is ',num_no_event)

#file_name_1_2_01.txt




