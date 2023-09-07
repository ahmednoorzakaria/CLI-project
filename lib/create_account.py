import click
from Database import session  # Make sure the import path is correct
from models import Customer, Accounts, Transactions

@click.group()
def cli():
    pass

@cli.command()
def create_account():
    # ...
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")

    existing_customer = session.query(Customer).filter_by(phone_number=phone_number).first()

    if existing_customer:
        print("Customer with this phone number already exists.")
    else:
        # Create a new customer and an associated account with a zero balance
        new_customer = Customer(name=name, phone_number=phone_number)
        new_account = Accounts(balance=0)
        new_customer.accounts.append(new_account)
        
        # Add the new customer and account to the database
        session.add(new_customer)
        session.commit()
        
        print(f"Customer '{name}' has been created with an account and a zero balance.")
