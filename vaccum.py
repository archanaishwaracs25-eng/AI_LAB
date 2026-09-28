status_A = "default"
status_B = "default"
location = "A"
def vaccumcleaner(location,status_A,status_B):
    if(status_A == "clean" and status_B == "clean"):
        print ("both rooms are clean")
    
    
    while(status_A != "clean" or status_B != "clean"):
        if(location == "A"):
            if(status_A == "dirty"):
                print("pick the dust in A")
                status_A = "clean"
                print("location A is clean")
            else:
                location = "B"
                print ("move to B")
        if(location == "B"):
            if(status_B != "clean"):
                print("pick the dust")
                status_B = "clean"
                print("B is clean")
            else:
                location = "A"
                print("move to A")


    return 

vaccumcleaner("A","dirty","dirty")    
print("next")   
vaccumcleaner("B","clean","dirty")
print("next")
vaccumcleaner("B","clean","clean")
