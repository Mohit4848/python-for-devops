Error = 0
Info = 0
Warning = 0

with open("app.log", "r") as file:
    for line in file:
        if "INFO" in line:
            Info += 1
        elif "ERROR" in line:
            Error += 1
        elif "WARNING" in line:
            Warning += 1
        else:
            pass
        
with open("log.txt", "w") as audit:
    audit.write(f"Info = {Info}\n")
    audit.write(f"Error = {Error}\n")
    audit.write(f"Warning = {Warning}\n")

print("Info = ", Info)
print("Error= ", Error)
print("Warning= ", Warning)