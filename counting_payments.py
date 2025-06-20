import pickle
import json
import datetime
import decimal
from functools import wraps



class Accumulator:
    def __init__(self, initial_value=0):
        self.total = initial_value
        self.history = []
    

    def add_input(self, *args):
        for arg in args:
            if isinstance(arg, (int, float)):
                self.total += arg
                self.history.append(arg)
                return f'Added {arg}, now total is {self.total}'
    
    def calculate(self):
        if self.total == 0:
            return 'Accumulator is empty.'
        a = decimal.Decimal(self.total)
        b = decimal.Decimal(1.5)
        c = decimal.Decimal(0.4)
        d = (a * b) * c
        d = round(d, 2)
        d = float(d)
        return d
    

    def get_total(self):
        return float(self.total)
    def get_history(self):
        return self.history
    

    def reset(self):
        self.total = 0
        self.history = []
        return 'Accumulator reset to zero.'


class PrettyView:
    pass


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs) 
        except IndexError:                             
            return 'Incorrect input!'
        except KeyError:                               
            return 'Incorrect input!'
        except ValueError:                             
            return 'Incorrect input!'
    return inner
    




payments = ('payments.json')



def parse_input(user_input):
    if not user_input.strip():  # checking if input is empty
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, args


#this was a first version of this function
# @input_error
# def calculate_amount(num) -> float:
#     try:
#         if not [int(num) or float(num)]:
#             raise ValueError("Input must be a number.")
#     except ValueError:
#         return "Input must be a number."
#     else:
#         a = decimal.Decimal(num)
#         b = decimal.Decimal(1.5)
#         c = decimal.Decimal(0.4)
#         d = (a * b) * c
#         d = round(d, 2)  # Round to 2 decimal places
#         d = float(d)  # Convert Decimal to float for consistency
#         return d
    

def calculate_chat_payment(value):
    try:
        if not [int(value) or float(value)]:
            raise ValueError("Input must be a number.")
    except ValueError:
        return "Input must be a number."
    else:
        minutes = decimal.Decimal(value)
        cost = decimal.Decimal(0.14)
        percentage = decimal.Decimal(0.4)
        payment = (minutes * cost) * percentage
        payment = round(payment, 2)
        payment = float(payment)
        return payment   


def add_chat_payment(amount, filename='payments.pickle'):
    amount = calculate_chat_payment(amount)
    data = load_data(filename)
    current_month = datetime.datetime.now().strftime('%Y-%m-%d')
    
    if current_month not in data:
        data[current_month] = []
    
    payment_entry = {'Chat Payment': amount}
    data[current_month].append(payment_entry)
    
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    
    return f"Chat payment of {amount} added for {current_month}."


def add_payment(amount, filename='payments.pickle'):
    amount = Accumulator(amount)
    data = load_data(filename)
    current_month = datetime.datetime.now().strftime('%Y-%m-%d')
    
    if current_month not in data:
        data[current_month] = []
    
    payment_entry = {'Amount': amount.get_total()}
    data[current_month].append(payment_entry)
    
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    
    return f"Payment of {amount.get_total()} added for {current_month}."


def load_data(filename='payments.pickle'):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
            data = {}
    return data


def delete_data(filename='payments.pickle'):
    try:
        with open(filename, 'wb') as f:
            pickle.dump({}, f)
    except FileNotFoundError:
        return "File not found, nothing to delete."

    


def main():
    load_data()
    acc = Accumulator()
    print("Welcome to the Payment Tracker!")
    while True:
        user_input = input("Enter command (for all cmd type help): ")
        cmd, args = parse_input(user_input)
        if cmd == '':
            print("No command entered. Type 'help' for available commands.")
            continue
        elif cmd in ['exit', 'quit']:
            print("Exiting the program.")
            break
        elif cmd == 'add':
            add_payment(acc.calculate())
            print(f"Payment added: {acc.calculate()}")
        elif cmd == 'add-chat':
            if not args:
                print("Please provide the number of minutes.")
                continue
            if not args[0].isdigit():
                print("Please provide a valid number of minutes.")
                continue
            add_chat_payment(float(args[0]))
            print(f"Chat payment added: {args[0]}")
        elif cmd == 'add-acc':
            if not args:
                print("Please provide an amount to add.")
                continue
            if not args[0].isdigit():
                print("Please provide a valid number.")
                continue
            amount = int(args[0])
            result = acc.add_input(amount)
            print(result)
        elif cmd == 'history':
            history = acc.get_history()
            if history:
                print("Payment history:")
                for entry in history:
                    print(entry)
            else:
                print("No payment history available.")
        elif cmd == 'total':
            total = acc.get_total()
            print(f"Total amount received: {total}")
        elif cmd == 'reset':
            acc.reset()
            print("Accumulator reset to zero.")    
        elif cmd == 'view':
            print(f"Payments:{load_data()}")
        elif cmd == 'del':
            delete_data()
            print("All payment data deleted.")
        elif cmd == 'reset':
            acc.reset()
            print("Accumulator reset to zero.")
        elif cmd == 'help':
            print('Available commands:\nadd - adding amount from accumulator of received money via letter\nadd-chat <minutes> - adding amount of received money via chat\n' \
            'view - view all payments\nexit - exit the program\ndel - delete all payment data\nhistory - view payment history\nadd-acc adding acc counting\n' \
            'reset - reset accumulator to zero\ntotal - view total amount received\nhelp - show this help message'
            )
        else:
            print("Unknown command. Type 'help' for available commands.")


if __name__ == "__main__":
    main()
        


        
        
        

        





