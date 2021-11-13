import os


def get_front_2_last (line, front, last):
        begin=line.find(front)+len(front)
        end=line.find(last)
        ss=line[begin:end]
        # print(ss)
        return ss



def apply_file (log_name, log_key, blacklist_key):
        file_log=open(log_name, encoding='UTF-8')
        # file_key_value=open("log1.txt",errors='ignore',encoding='utf-8')

        file_key_value=open(log_key)
        #file_key_result=open("key_result_usecase.txt","a")#use w just save 1 char

        # key word black list 
        file_blacklist_key = open(blacklist_key)

        result_name=log_name.replace('log_','result_')
        # print(result_name)
        # print(log_name)
        # result_name="log_file/result_log1.txt"
        file_key_result=open(result_name,"w")#use w just save 1 char
        file_key_result.truncate()              #delete now contect

        temp_name=log_name.replace('log_','temp_')
        file_key_temp=open(temp_name,"w")
        file_key_temp.truncate()

        line_log=file_log.readline()

        while line_log:
                #func2{
                # print(line_log)
                file_key_temp.write(line_log)

                result_a = False

                status_blackword = False

                file_key_value.seek(0, 0)
                key_value=file_key_value.readline()

                file_blacklist_key.seek(0, 0)
                blacklist_value = file_blacklist_key.readline()
                while key_value:
                        key=key_value.strip()
                        result_a = key in line_log
                        if result_a == True :
                                break
                        key_value=file_key_value.readline()
                        
                        # key_value=file_blacklist_key.readline()
                        # judge keyword is in blacklist

                        # file_blacklist_key.seek(0, 0)
                        # blacklist_value = file_blacklist_key.readline()
                        # while blacklist_value:
                        #         if key_value == blacklist_value:
                        #                 status_blackword = True
                        #         else:
                        #                 blacklist_value = file_blacklist_key.readline()


                        # if status_blackword == True:
                        #         print("key_value")
                        #         break
                        # else:



                # if logline match, print '\n' to sign
                temp="adev_open_input_stream:" in line_log
                if temp == True :
                        # print("xxx")
                        file_key_result.write("\n")

                # save match log
                status_log_has_blacklist = False
                file_blacklist_key.seek(0, 0)
                blacklist_value = file_blacklist_key.readline()
                blacklist_value=blacklist_value.replace('\n','')

                if result_a == True :
                        # if logline has blacklist_word, don't save log
                                # print("has blacklist")
                                # status_log_has_blacklist = False
                        while blacklist_value:
                                status_log_has_blacklist = blacklist_value in line_log
                                if status_log_has_blacklist == True:
                                        blacklist_value = file_blacklist_key.readline()
                                        blacklist_value=blacklist_value.replace('\n','')
                                        break
                                else:
                                        blacklist_value = file_blacklist_key.readline()
                                        blacklist_value=blacklist_value.replace('\n','')
                        
                                # print("no blacklist")
                        if status_log_has_blacklist == False:
                                file_key_result.write(line_log)     #copy one line

                line_log=file_log.readline()  #read the next line
                #func2}

        file_log.close
        file_key_value.close
        file_key_result.close
        file_key_temp.close
        file_blacklist_key.close

        return



# func get java file path
def get_file_path(path, file_type, func, log_key,blacklist_key):
        for root, dirs, files in os.walk(path):
                for f in files:
                        # ignore "pass" dir
                        a = "pass" in root
                        if a == True :
                                continue

                        temp1=0
                        temp2=0
                        temp=0
                        temp1=file_type in f    # file type is txt
                        temp2="log_" in f       # file is log not result
                        temp=temp1+temp2
                        if temp == 2 :
                                # print('file_path: ',file_path)
                                file_path=root+'/'+f
                                # print(file_path)
                                print('file_name: ',f)
                                apply_file(file_path, log_key,blacklist_key)
                                print('\n')
        return

dir_path="logfile"
file_type_a=".txt"
function_a="apply_file"
log_key="cmd/key_value_mtkpop.txt"
blacklist_key="cmd/blacklist_pop.txt"

get_file_path(dir_path, file_type_a, function_a,log_key,blacklist_key)
