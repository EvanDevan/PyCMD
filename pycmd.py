print("PyCMD 1.0 Test Realese")
print("Type 'help' for a list of commands")

while True:

    cmd = input("PyCMD: ")

    if cmd == "help":
        print("PyCMD 1.0 Test     Realese")
        print("￼help, crash, exit￼,  ver, say, python")
        
    if cmd == "crash":
        while True:
            print("PYCMD CRASH TEST REALESE 1.0")
            
    if cmd == "exit":
        break
        
    if cmd == "ver":
        print("PyCMD 1.0 Test Realese")
            
    if cmd == "say":
        say = input("Say: ")
        print(say)
     
    if cmd == "unix":
        import os
        while True:
            unix = input("UNIX: ")
            os.system(unix)
        
