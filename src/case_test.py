#!/usr/bin/env
class SimpleDevice:
    def __init__(self):
        self.state = "locked"
        self.count = 0
    def on_event(self, event):
        match (self.state, event):
            case ("locked", password) : 
                if password != MatchedPassWord:                                   
                   self.state = "locked"
                   self.count = self.count + 1    
                   print("Password is not matched")                           
                else : 
                   self.state = "unlocked"
                   self.count = 0
                   print("Password is matched")                           
            case ("unlocked", password) : 
                if password != MatchedPassWord :
                   self.state = "locked"
                   self.count = self.count + 1    
                   print("Password is not matched")    
                else :                    
                   self.state = "unlocked"
                   self.count = self.count    
                   print("Password is matched")        
            case _:
                # No state change for unknown events
                pass

    def __str__(self):
        return f"Device is {self.state}"

MatchedPassWord = "test11"

# initial state 
device = SimpleDevice()
print("\n")  
print(f"Intial device state {device}")  # Device is locked
print(".............................")  


while device.state != "unlocked":     
    inputNum = input("Put the number in :")
    print(f"You entered {inputNum}") 
    device.on_event(inputNum) 
    if device.state == "unlocked":        
        break
    else:        
        print(f"Count is {device.count}")
        if device.count >= 3: 
            print("You reached to the maximum limit")
            break

#test
#update