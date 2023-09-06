from sqlalchemy import create_engine, ForeignKey, Column, Integer, UniqueConstraint, String, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        UniqueConstraint(
            'phone_number',
            name='phone_number'),
    )

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    phone_number = Column(Integer())
    created_at = Column(DateTime, default=func.now())
    accounts = relationship('Accounts', back_populates='customer')

    def __repr__(self):
        return f'Customer(ID={self.id}, Name={self.name})'


class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column(Integer(), primary_key=True)
    balance = Column(Integer())  
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    transactions = relationship('Transactions', back_populates='account')  

    def __repr__(self):
        return f"Accounts(ID={self.id}, Balance={self.balance})"


class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer(), primary_key=True)
    account_id = Column(Integer(), ForeignKey('accounts.id'))
    amount = Column(Integer())
    timestamp = Column(DateTime, default=func.now()) 
    type = Column(String())  

    def __repr__(self):
        return f"Transactions(ID={self.id}, Type={self.type}, Amount={self.amount})"


if __name__ == "__main__":
    engine = create_engine("sqlite:///BANK.db")
    Base.metadata.create_all(engine)