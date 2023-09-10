import random


MAX_LINES = 3
MAX_BET=100
MIN_BET=1

ROWS = 3
COLS = 3

#symbols        -A,B,C,D
#symbol_counts  -2,4,6,8
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns,lines ,bet , values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol in symbol_to_check:
                break

        else:
            winnings +=values[symbol]*bet
            winning_lines.append(line + 1)

    return winnings,winning_lines


#machine_spain_loop
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for  symbol, symbol_count in symbols.items():
        for simbol_count in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] # copy of all_symbols list

        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns 
#results displaier
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns) :
            if i != len(columns) - 1:
                print(column[row] , end=" | ")
            else:
                print(column[row] , end=" ")

        print()
            


def deposit():
    while True:
        amount = input("what woud you like to deposit? $")
        if amount.isdigit():
            amount = int(amount) 
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter number.")    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES ) + ") ?") 
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES :
                break
            else:
                print("Enter a valid number of lines. ")
        else:
            print("Please enter number.")    
    return lines

def get_bet():
    while True:
        amount = input("what woud you like to bet in Each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter number.")    
    return amount

def spin(balance):
    lines =get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"your balance is not enough,your currunt balance is ${balance} and total bet is {total_bet}")
        else:
            break

    
    
    print(f"you are betting on ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    Winnings , winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"you want ${Winnings}.")
    print(f"you won on lines:",* winning_lines)
    return Winnings - total_bet 


def main():
    balance=deposit()
    while True:
        print(f"currunt balance is ${balance}" )
        answer = input("press enter to spin( q to quit)")
        if spin == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")


main()