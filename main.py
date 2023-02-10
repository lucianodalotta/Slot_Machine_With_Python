import machine.machine_operation  as funciones

              
def main():
 balance = funciones.deposit()
 while True:
     print(f"Tu sueldo actual es: ${balance}")
     answer = input("Toca enter para jugar o s para salir:")
     if answer.lower() == "s":
         break
     balance +=  funciones.spin(balance)
     
 print(f"Te retiraste con ${balance}")

main()