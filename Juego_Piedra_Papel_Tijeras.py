import random

jugador = input("Selecciona una de las opciones  \n1.piedra\n 2.papel\n  3.tijeas\n")


mylist = ["piedra", "papel", "tijeras"]
computadora = random.choice(mylist)
print(f"La computadora ha seleccionado: {computadora}")

if computadora == jugador:
 print ("Es un empate")
elif computadora =="piedra" and jugador == "tijeras":
 print("El jugador acaba de perder")
elif computadora =="tijeras" and jugador == "piedra":
 print("El jugador acaba de ganar")
elif computadora =="papel" and jugador == "tijeras":
 print("El jugador acaba de ganar")




    