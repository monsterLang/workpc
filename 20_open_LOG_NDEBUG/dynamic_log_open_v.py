# file ---- dynamic_log_open_v.py

# replay "#define LOG_NDEBUG 0" to "define LOG_NDEBUG 0"

import os

def open_logNDEBUG (filename_code):
    # deal with code
    # filename_code = line_codepath
    filename_code = filename_code.strip()
    print(filename_code)
    file_code = open(filename_code, 'r+')
    line_code = file_code.readline()
    lineseek_num = 0
    status_in_define=False
    while line_code:
        # print(line_code)
        # print("lineseek_num",lineseek_num)
        
        status_define_in_codeline = False
        status_define_in_codeline = "LOG_NDEBUG" in line_code
        if status_define_in_codeline == True:
            line_code = line_code.replace('//#define LOG_NDEBUG 0','#define LOG_NDEBUG 0  ')
            line_code = line_code.replace('\n','')
            # linenum=lineseek_num-1
            
            # print(file_code.tell())
            file_code.seek(lineseek_num)
            file_code.write(line_code)
            # print("lineseek_num---",lineseek_num)
            # print(line_code)
            status_in_define = True
            break

        status_include_in_codeline = "include" in line_code
        if status_include_in_codeline == True:
            if status_in_define == True:
                break
        # print("last seek",file_code.tell())
        lineseek_num = file_code.tell()
        line_code = file_code.readline()
        

    
    file_code.close
    print("-leave open_logNDEBUG")
    return

def close_logNDEBUG (filename_code):
    # deal with code
    # filename_code = line_codepath
    filename_code = filename_code.strip()
    file_code = open(filename_code, 'r+')
    line_code = file_code.readline()
    lineseek_num = 0
    status_in_define=False
    while line_code:
        # print(line_code)
        # print("lineseek_num",lineseek_num)
        
        status_define_in_codeline = False
        status_define_in_codeline = "LOG_NDEBUG" in line_code
        if status_define_in_codeline == True:
            line_code = line_code.replace('#define LOG_NDEBUG 0  ','//#define LOG_NDEBUG 0')
            # line_code = line_code.replace('\n','')
            # linenum=lineseek_num-1
            
            # print(file_code.tell())
            file_code.seek(lineseek_num)
            file_code.write(line_code)
            # print("lineseek_num---",lineseek_num)
            # print(line_code)
            status_in_define = True
            break

        status_include_in_codeline = "include" in line_code
        if status_include_in_codeline == True:
            if status_in_define == True:
                break
        # print("last seek",file_code.tell())

        lineseek_num = file_code.tell()
        line_code = file_code.readline()
        

    
    file_code.close
    print("-leave open_logNDEBUG")
    return


def judge_open_close_log(line_codepath_temp):

    status_o_c_log_temp = False
    line_codepath_temp = line_codepath.strip()
    file_first_code = open(line_codepath_temp)
    line_first_code = file_first_code.readline()
    while line_first_code:
        status_judge_log = "LOG_NDEBUG" in line_first_code
        if status_judge_log == True:
            status_o_c_log_temp = '//#define LOG_NDEBUG 0' in line_first_code
            if status_o_c_log_temp == True:
                break

        line_first_code = file_first_code.readline()


    return status_o_c_log_temp

log_file_path = "dynamic_log_filepath.txt"


file_logcode_path = open(log_file_path)
line_codepath=file_logcode_path.readline()

status_o_c_log = False
status_o_c_log = judge_open_close_log(line_codepath)
file_logcode_path.close


while line_codepath:
    print(line_codepath)

    if status_o_c_log == True:
        open_logNDEBUG(line_codepath)
        print("open log")
    else:
        close_logNDEBUG(line_codepath)
        print("close log")

    # deal with code
    # open/close 2 no error
    # open_logNDEBUG(line_codepath)
    # close_logNDEBUG(line_codepath)
    line_codepath=file_logcode_path.readline()

print("close file_logcode_path")
file_logcode_path.close
