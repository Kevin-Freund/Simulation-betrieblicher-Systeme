import random
from scipy.stats import expon

Takt = 20
anzExp = 1000000
jitter = 5
hit1 = 0
hit2 = 0
hit3 = 0
hit4 = 0


# a) Ankunftsabstand = gleichverteilt von 20ms, Standardabweichung: -1m bis 7ms
# b) Ankunftszeiten = 19ms + Laufzeit(Exponentialverteilt mit Mittelwert = 1ms = 1/lambda)

for i in range(0, anzExp):
    
    a = round(random.uniform(-1, 7))
    b = round(random.uniform(-1, 7))
    c = expon.rvs(loc=19)
    d = expon.rvs(loc=19)
    
    if ((Takt + a) > 25):
        hit1 += 1
        
        if ((Takt + b) > 25):
            hit2 += 1

    if (c > 25):
        hit3 += 1

        if (d > 25):
            hit4 += 1
    
    
        

print("1. a)")
print("Anzahl der *nach* 25ms ankommenden Pakete: " + str(hit1))
print("Gesamtanzahl der durchgef체hrten Versuche: " + str(anzExp))                
print("Verh채ltnis:")
print(float(hit1/anzExp))

print("------------------------")

print("b)")
print("Verh채ltnis:")
print(float(hit3/anzExp))

print("-----------------------")

print("2.")
print("Wahrscheinlichkeit von 2 aufeinanderfolgende Pakete *nach* 25ms: ")
print(float(hit2/anzExp))

print("-----------------------")

print("Verh채ltnis:")
print(float(hit4/anzExp))
    
#-----------------------------------------------------------------------------------------------  
# 1.
# a) Prozent der Pakete, welche nach 25ms ankommen: ca. 18,7..% 
#2.
# Wahrscheinlichkeit, dass zwei aufeinanderfolgende Pakete erst nach 25ms ankommen: ca. 0.035
#-----------------------------------------------------------------------------------------------
