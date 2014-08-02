#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import datetime
import tarfile

base_dir = '/data1/home/tlog/logplat/log'
back_dir = '/data1/home/tlog/logplat/log/back'
expired_day = 90

if not os.path.exists(back_dir):
    os.mkdir(back_dir)

date_today = datetime.datetime(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday)
tar_match_file_dict = {}

def tar_file(work_dir,back_work_dir,e_tlog_dir):
    work_dir = work_dir
    back_work_dir = back_work_dir
    e_tlog_dir = e_tlog_dir
    os.chdir(work_dir)
    print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + work_dir + "  START....."

    for e_file in os.listdir(work_dir):
        if not ( os.path.isfile(e_file) and e_file.split('.')[-1] == 'log' ):
            print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + work_dir + os.path.sep + e_file + "  NO log file....."
            pass

        file_mtime = time.localtime(os.stat(e_file).st_ctime)
        file_mtime_date = datetime.datetime(file_mtime.tm_year,file_mtime.tm_mon,file_mtime.tm_mday)

        separated_days = (date_today - file_mtime_date).days
        if separated_days >= expired_day and os.path.isfile(work_dir + os.path.sep + e_file):
            print  "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + work_dir + os.path.sep + e_file + ' log file EXPIRED 90 DAYS  REMOVED!!!'
            os.remove(e_file)
        
        elif separated_days > 1 and os.path.isfile(work_dir + os.path.sep + e_file):
            tar_file_name = str(file_mtime.tm_year) + '_' + str(file_mtime.tm_mon) + '_' + str(file_mtime.tm_mday)
            if tar_file_name in tar_match_file_dict:
                if e_file not in tar_match_file_dict[tar_file_name]:
                    tar_match_file_dict[tar_file_name].append(e_file)
                else:
                    pass
            else:
                tar_match_file_dict[tar_file_name]=[]
                tar_match_file_dict[tar_file_name].append(e_file)
        elif separated_days <= 1:
            print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + work_dir + os.path.sep + e_file + " NO TAR new  log file!!!!"
            pass
        else:
            print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + work_dir + os.path.sep + e_file + " NO EXISTS!!!!"
            pass 
            
    for (e_tar_name, e_tar_file_list) in tar_match_file_dict.items():
        if os.path.isfile(back_work_dir + os.path.sep + e_tar_name + '.tar.gz'):
            os.rename(back_work_dir + os.path.sep + e_tar_name + '.tar.gz', back_work_dir + os.path.sep + e_tar_name + "_" + time.strftime("%Y%m%d%H%M%S",time.localtime()) + '.tar.gz_bak')

        print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + back_work_dir + os.path.sep + e_tar_name + '.tar.gz' + " START TAR...."
        tar = tarfile.open(back_work_dir + os.path.sep + e_tar_name + '.tar.gz', 'w:gz')
        for e_day_file in e_tar_file_list:
            if os.path.isfile(e_day_file):
                log_info =  "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + str(work_dir + os.path.sep + e_day_file) + " ADD IN " + str(back_work_dir + os.path.sep + e_tar_name) + ".tar.gz"
                print log_info
                tar.add(e_day_file)
            else:
                print  "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + e_day_file + " NOT FOUND FOR TAR!!!"
        tar.close()

        if os.path.isfile(back_work_dir + os.path.sep + e_tar_name + '.tar.gz'):
            for e_log_file in e_tar_file_list:
                if os.path.isfile(e_log_file):
                    log_info =  "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + str(e_log_file) + " TAR AND REMOVED!!!!"
                    print log_info
                    os.remove(e_log_file)
                else:
                    log_info =  "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + str(e_log_file) + " TAR AND NOT FOUND REMOVED!!!!"
                    print log_info                  



def remove_pass_tar_log():
    if not os.path.exists(back_dir):
        return
    
    os.chdir(back_dir)
    for e_tarlog_dir in os.listdir(back_dir):
        if not os.path.isdir(e_tarlog_dir):
            pass

        os.chdir(back_dir + os.path.sep + e_tarlog_dir)
        list_dir = [e for e in os.listdir(back_dir + os.path.sep + e_tarlog_dir) \
                        if (e.split(".")[-1] == 'gz' or e.split(".")[-1] == 'gz_bak') and e.split(".")[-2] == 'tar' ]
        for e_tar_file in list_dir:
            e_filename = e_tar_file.split(".")[0]
            file_date = datetime.datetime(int(e_filename.split("_")[0]),int(e_filename.split("_")[1]),int(e_filename.split("_")[2]))

            separated_days = (date_today - file_date).days
            if separated_days >= expired_day:
                log_info = str(os.getcwd() + os.path.sep + e_tar_file) + " tar log file EXPIRED 90 DAYS REMOVED!!!!"
                print log_info
                os.remove(e_tar_file)


def main():
    tlog_dir_list = os.listdir(base_dir)
    for e_tlog_dir in tlog_dir_list:
        work_dir = base_dir + os.path.sep + e_tlog_dir
        back_work_dir = back_dir + os.path.sep + e_tlog_dir

        if  os.path.isdir(work_dir) and back_dir != work_dir and e_tlog_dir.startswith("tlogd"):
            if not os.path.exists(back_work_dir):
                os.mkdir(back_work_dir)
            print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + work_dir
            tar_file(work_dir,back_work_dir,e_tlog_dir)
        else:
            print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] " + work_dir + " DIR NOT TLOG DIR!!!"


if __name__ == '__main__':
    print "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] starting....."
    main()
    remove_pass_tar_log()
    print  "[" + time.strftime("%Y %m %d %H:%M:%S", time.localtime()) + "] fininshed!!!"