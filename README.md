# Banking CLI Application

## Overview

The Banking CLI Application is a command-line tool for managing bank accounts. It provides functionalities for creating new accounts, logging in, depositing and withdrawing money, and checking account balances. The application is built using Python and leverages the Click library for creating the command-line interface and SQLAlchemy for interacting with the database.

## Features

- **User Account Creation**: Users can create new bank accounts by providing their name and phone number.

- **Account Login**: Registered users can log in to their accounts using their phone number.

- **Deposit**: Users can deposit money into their accounts.

- **Withdrawal**: Users can withdraw money from their accounts.

- **Check Balance**: Users can check their account balance.

- **Database Integration**: The application uses SQLAlchemy for database operations, allowing for persistent data storage.

## Prerequisites

Before running the Banking CLI Application, ensure you have the following dependencies installed:

- Python (version 3.9 or higher)
- SQLAlchemy
- Click

You can install the required dependencies using pip:

`bash
pip install sqlalchemy click



## Usage
To run the Banking CLI Application, follow these steps:

- Clone the project repository to your local machine:
git clone https://github.com/ahmednoorzakaria/CLI-project
- Navigate to the project directory:
  - cd banking-cli
  - Run the CLI application:
     - python cli.py
- Follow the on-screen prompts to create an account, log in, and perform banking operations.
## Database Configuration
The application uses an SQLite database named "BANK.db" by default. You can modify the database configuration in the cli.py file by changing the database URL in the following line:

- engine = create_engine("sqlite:///BANK.db")
## Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

  - git checkout -b feature/my-feature
  - Make your changes, commit them, and push to your forked repository:
     - git commit -m "Add my feature"
     - git push origin feature/my-feature
 - Create a pull request to the main project repository, describing your changes.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or suggestions, please feel free to contact us at zakariaahmednoor5@email.com.



