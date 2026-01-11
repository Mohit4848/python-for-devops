
class Log_chaanbeen:
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.count = {"INFO":0, "ERROR":0, "WARNING":0, "UNKNOWN":0}

    def read_file(self):
        try:
            with open(self.log_file, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("File is not found. Please give a file that is present.")
            return []
        
    def ginti(self, lines):
        for line in lines:
            if "ERROR" in line:
                self.count["ERROR"] += 1
            elif "INFO" in line:
                self.count["INFO"] += 1
            elif "WARNING" in line:
                self.count["WARNING"] += 1
            else:
                self.count["UNKNOWN"] += 1
                
        return self.count

def main():
    detective = Log_chaanbeen("app.log")
    lines = detective.read_file()
    
    if not lines:
        print("File is empty")
    
    result = detective.ginti(lines)
    
    for topic, count in result.items():
        print(f"{topic}: {count}")

if __name__ == "__main__":
    main()
            