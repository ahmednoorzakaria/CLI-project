import click
from Database import session  # Make sure the import path is correct
from models import Customer, Accounts, Transactions

def deposit(customer, amount):
    account = customer.accounts[0]  # Assuming one account per customer
    account.balance += int(amount)
    transactions = Transactions(account=account, amount=int(amount), type="deposit")
    session.add(transactions)
    session.commit()
    click.echo(f"Deposited ${amount} successfully. New balance: ${account.balance}")

def withdraw(customer, amount):
    account = customer.accounts[0]  # Assuming one account per customer

    if account.balance < int(amount):
        click.echo("Insufficient funds.")
    else:
        account.balance -= int(amount)
        transactions = Transactions(account=account, amount=int(amount), type="withdraw")
        session.add(transactions)
        session.commit()
        click.echo(f"Withdrew ${amount} successfully. New balance: ${account.balance}")

def check_balance(customer):
    account = customer.accounts[0]  # Assuming one account per customer
    click.echo(f"Your account balance: ${account.balance}")