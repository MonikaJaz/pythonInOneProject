import random

MAX_LINES = 3  # WIELKIE LITERY JAKO ZMIENNA GLOBALNA
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {  # dzila podobnie jak haszmapa w javie ( klucz - wartosc )
    "A": 2,  # tyle razy bedzie wystepowal dana literka w maszynie
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {  # dzila podobnie jak haszmapa w javie ( klucz - wartosc )
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # symbol - pierwsza kolumna i pierwszy wiersz
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # jezeli poprzedni symbol w wierszu jest inny od nastepnegp
        else:
            winnings += values[symbol] * bet  # wygrana to wartosc symbolu (symbols_value) pomnozona przez zaklad
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  # tworzymy liste kolumn
    for _ in range(cols):  # tworzymy pętle ktora bedzie iterowac przez kazda kolumne w liscie kolumn
        column = []
        current_symbols = all_symbols[:]
        # dwukropek w nawiasie kwadratowym powoduje ze tworzy sie kopia current symbols w tym kodzie iterujemy przez
        # wzystkie wiersze znajdujace sie w danej kolumnie i losujemy wartosci ktore beda przypisane w kazdym miejscu
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # end sprawia ze jest nowa linia
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)  # castujemy int na stringa
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("Please enter a number!")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)  # castujemy int na stringa
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number!")
    return lines


def getBet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)  # castujemy int na stringa
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET - MAX_BET}.")  # trik na przedzial
        else:
            print("Please enter a number!")
    return amount
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = getBet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}. ")
    print(f"You won on lines: ", *winning_lines)  # gwiazdka oznacza unpack operator
    return winnings- total_bet

def main():
    balance = deposit()  # wywolanie funkcji
    while True:
        print(f"Current balance is ${balance}")
        answer10 = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


main()
