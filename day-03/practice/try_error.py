import psutil

def check_cpu_threshold():
    try:
        cpu = int(input("Enter the cpu threshold :- "))
        
        current_cpu = psutil.cpu_percent()
        print("Current CPU usage is ", current_cpu)
    
        if(current_cpu > cpu):
            print("Alert Mail sent.....")
        else:
            print("Everything is fine and cpu usage is under threshold")
    except ValueError:
        print("Please enter an integer number. Not anything else than an integer number")
        
check_cpu_threshold()