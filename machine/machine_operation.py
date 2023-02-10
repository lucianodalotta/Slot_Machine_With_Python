import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={ #DICCIONARIO
    "7":2,
    "A":4,
    "9":6,
    "D":8
    
}

symbol_value={ 
    "7":5,
    "A":4,
    "9":3,
    "D":2
    
}

def check_winnings(columns,lines,bet, values):
    winnings = 0 
    winnings_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check= column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol]*bet
                winnings_lines.append(line + 1)
        return winnings, winnings_lines
                
    
    


def get_slot_machine_spin(rows,cols, symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns =[]
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value =random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns


def print_slot_machine(columns):
 for row in range(len(columns[0])):
     for i, column in enumerate(columns):
         if i != len(columns)-1:
            print(column[row], end=" | ") #el end es para q las filas salgan en la misma linea
         else:
             print(column[row], end="")
             print()
             

    
        
    
def deposit():
    while True:
        amount= input("Cuanto te gustaria depositar? $ ")
        if amount.isdigit():
            amount= int(amount)
            if amount >0:
                break
            else: print("El deposito debe ser mayor a $0.00")
        else:
            print("Por favor ingrese un monto valido")        
    return amount   

def get_numer_of_lines():
     while True:
        lines= input(f"Ingrese el número de líneas para apostar (1 - {MAX_LINES} ): ")
        if lines.isdigit():
            lines= int(lines)
            if  1<= lines<=MAX_LINES:
                break
            else: print(f"El numero debe ser mayor a 0 y hasta {MAX_LINES}")
        else:
            print("Por favor ingrese un numero valido")        
     return lines 
    
def get_bet():
     while True:
        bet= input(f"Ingrese cuanto quiere apostar por cada linea: $")
        if bet.isdigit():
            bet= int(bet)
            if  MIN_BET<= bet <=MAX_BET:
                break
            else: print(f"la apuesta minimas es de ${MIN_BET} y el maximo es de ${MAX_BET}")
        else:
            print("Por favor ingrese una apuesta valido")        
     return bet 
 
 
def spin(balance):
    lines =get_numer_of_lines()
    while True:    
        bet= get_bet()
        total_bet= bet *lines
   
        if total_bet > balance:
            print(f"No tenes ese dinero para apostar esa cantidad, vos tenes un monto de: ${balance} y quisiste apostar ${total_bet} (monto x linea)")
        else:
         break
   
    print(f"Estas apostando ${bet} en la linea {lines}. El total de apuesta es: ${total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnning, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Ganaste: ${winnning}")
    print(f"Ganaste en las lineas:", *winnings_lines)
    return winnning - total_bet