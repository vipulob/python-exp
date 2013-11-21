# How to execute a command on local machine using subprocess?


import subprocess


cmd = "ls"
        
print("cmd:"+cmd)

# Execute the cmd. 
ret_code = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

# Will fetch stdout and stdin
output, error = ret_code.communicate()


# check return code
if ret_code.poll() != 0:
    print("Error:The cmd failed to Execute")
else:
    print(output.split("\n"))
