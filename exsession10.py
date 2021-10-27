#%%
#number 1

def convert_to_days():
   Hours = int(input("Enter number of hours: "))
   Minutes = int(input("Enter number of minutes: "))
   Seconds = int(input("Enter number of second: "))
   d = getdays(Hours, Minutes, Seconds)
   print("The number of day is: ",d)

def getdays(Hours, Minutes, Seconds):
   days = (Hours/24) + (Minutes/(24*60)) + (Seconds/(24*60*60))
   return round(days,4)
 
convert_to_days()

#%%
#number 2

def calc_weight_on_planet(m=int, g=23.1):
    w = (m*g)/9.8
    if g == 9.8: 
        print (w)
    elif g == 23.1 :
        print (w)
    else :
        print (calc_weight_on_planet().format(w))
        
calc_weight_on_planet()

#%%
#number 2 alternative
def calc_weight_on_planet(m=int, g=23.1):
    w = (m*g)/9.8
    print(w)
    
calc_weight_on_planet()


#%%
#number 3
def num_atoms(amount=int, weight=196.97):
    numatoms = (amount/weight)*6.022*10**23
    print(numatoms)
    
num_atoms()


#%%
#number 4

def calc_new_height():
    cw = int(input("Enter the current width: "))
    ch = int(input("Enter the current height: "))
    dw = int(input("Enter the desired width: "))
    x = get_corresponding_height(ch, cw, dw)
    print ("The correspond height : ",x)
    
def get_corresponding_height(ch, cw, dw):
    ascRatio = (cw/ch)
    nw = (dw/ascRatio)
    return float (nw)

calc_new_height()

#%%
#number 5

def convert_temp():
    Tf = eval(input("Enter a temperature in Farenheit: "))
    c = convert_celc(Tf)
    k = convert_kelv(c)
    print("The temperature in Farenheit:",Tf)
    print("The temperature in Celcius: ",c)
    print("The temperature in Kelvin: ",k)
    

def convert_celc(Tf):
    Tc = 5/9*(Tf - 32)
    return float (Tc)
    
def convert_kelv(Tc):
    Tk = Tc + 273.15
    return float (Tk)
    
convert_temp()