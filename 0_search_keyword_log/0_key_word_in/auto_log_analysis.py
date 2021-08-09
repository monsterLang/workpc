import os


def get_front_2_last (line, front, last):
        begin=line.find(front)+len(front)
        end=line.find(last)
        ss=line[begin:end]
        # print(ss)
        return ss



def apply_file (log_name, log_key):
        file_log=open(log_name)
        # file_key_value=open("log1.txt",errors='ignore',encoding='utf-8')

        file_key_value=open(log_key)
        #file_key_result=open("key_result_usecase.txt","a")#use w just save 1 char

        result_name=log_name.replace('log_','result_')
        print(result_name)
        print(log_name)
        # result_name="log_file/result_log1.txt"
        file_key_result=open(result_name,"w")#use w just save 1 char
        file_key_result.truncate()              #delete now contect

        line_log=file_log.readline()

        while line_log:
                #func2{
                file_key_value.seek(0, 0)
                key_value=file_key_value.readline()
                while key_value:
                        key=key_value.strip()
                        result_a=key in line_log
                        if result_a == True :
                                break
                        key_value=file_key_value.readline()
                        
                temp="adev_open_input_stream:" in line_log
                if temp == True :
                        print("xxx")
                        file_key_result.write("\n")

                if result_a == True :
                        file_key_result.write(line_log)     #copy one line

                line_log=file_log.readline()  #read the next line
                #func2}

        file_log.close
        file_key_value.close
        file_key_result.close

        return



# func get java file path
def get_file_path(path, file_type, func, log_key):
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
                                print(file_path)
                                print('file_name: ',f)
                                apply_file(file_path, log_key)
        return

dir_path="logfile"
file_type_a=".txt"
function_a="apply_file"
log_key="cmd/key_value_mediacodec_GraphicBufferSource.txt"

get_file_path(dir_path, file_type_a, function_a,log_key)
