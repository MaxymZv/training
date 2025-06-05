import pickle
import datetime
import decimal
from functools import wraps




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
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, args



@input_error
def calculate_amount(num) -> float:
    try:
        if not [int(num) or float(num)]:
            raise ValueError("Input must be a number.")
    except ValueError:
        return "Input must be a number."
    else:
        a = decimal.Decimal(num)
        b = decimal.Decimal(1.5)
        c = decimal.Decimal(0.4)
        d = (a * b) * c
        d = round(d, 2)  # Round to 2 decimal places
        d = float(d)  # Convert Decimal to float for consistency
        return d


def add_payment(amount, filename='payments.pickle'):
    amount = calculate_amount(amount)
    data = load_data(filename)
    current_month = datetime.datetime.now().strftime('%Y-%m-%d')
    
    if current_month not in data:
        data[current_month] = []
    
    payment_entry = {'Amount': amount}
    data[current_month].append(payment_entry)
    
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    
    return f"Payment of {amount} added for {current_month}."


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

    

@input_error
def main():
    load_data()
    print("Welcome to the Payment Tracker!")
    while True:
        user_input = input("Enter command (add, view, exit): ")
        cmd, args = parse_input(user_input)

        if cmd in ['exit', 'quit']:
            print("Exiting the program.")
            break
        elif cmd == 'add':
            add_payment(float(args[0]))
            
            print(f"Payment added: {args[0]}")

        elif cmd == 'view':
            print(f"Payments:{load_data()}")
        elif cmd == 'del':
            delete_data()
            print("All payment data deleted.")


if __name__ == "__main__":
    main()
        


        
        
        

        





