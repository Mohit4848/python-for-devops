import psutil

def check_cpu_threshold():
    cpu = int(input("Enter the cpu threshold"))
    
    current_cpu = psutil.cpu_percent()
    print("Current CPU usage is ", current_cpu)
    
    if(current_cpu > cpu):
        print("Alert Mail sent.....")
    else:
        print("Everything is fine and cpu usage is under threshold")
        
check_cpu_threshold()
    