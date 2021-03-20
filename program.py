from calculator import Calculator


if __name__ == "__main__":

    calculator = Calculator()
    
    print("Welcome to Calculator\n")

    while True:
        while True:
            try:
                calculator.first_number = float(input("Enter first Number: "))
            except ValueError:
                print("Choose only numbers")
                continue
            else:
                break
        while True:
            try:
                operation = int(input("Choose operation, enter numbers: 1)Sum 2)Sub 3)Multiply 4)Divide: "))
            except ValueError:
                print("Choose only numbers between 1 and 4")
                continue
            else:
                break
        while True:
            try:
                calculator.second_number = float(input("Enter second Number: "))  
            except ValueError:
                print("Choose only numbers")
                continue
            else:
                break
        if operation == 1:
            print(calculator.sum())
        elif operation == 2:
            print(calculator.sub())
        elif operation == 3:
            print(calculator.multiply())
        elif operation == 4:
            print(calculator.divide())
        
        exit_or_continue = input("Type 'exit' to exit or press any key to continue: ")
        if exit_or_continue.lower() == "exit":
            break
        else:
            continue

        