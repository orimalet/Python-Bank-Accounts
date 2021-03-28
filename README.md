# Python-Bank-Accounts
A program that implements Basic Account and Premium Account types of Bank Accounts in Python.

You are to design an implement two classes in Python: BasicAccount and PremiumAccount.

The classes are to be adherent to the following UML Class diagram, though you may add extra methods and variables if you wish (essentially, the class diagram is a minimum, and it shows you what will be tested against):

![image](https://user-images.githubusercontent.com/56177227/112739315-4eb9bc80-8f6b-11eb-8a3d-45f40a1e7a35.png)





To read the UML diagram, a line of <varName> : <dataType> means that varName is an object of that data type.

A line of <methodSignature> : <dataType> means that the method will return a particular data type.

The variables of the classes are described as follows:

name – the account holders name

acNum – the number of the account. This should be “serial”, as in the first account to be created should be number 1, the second account to be created should be 2, and so on...

balance – The balance (in pounds) of the account.

CardNum – The card number should be a string of a 16 digit number (you should use the random module for this)

cardExp - a tuple where the first element is an int of the month and the second element is 2-digit year. Eg: 03/23 represents March 2023   (You should use the datetime module for this)

overdraft – True if the account has an overdraft, and false if not

overdraftLimit – The amount that the account can go overdrawn by

 

The method behaviours are as follows:

__init__(self, str, float)

Initialiser giving the account name and opening balance

__init__(self, str, float, float)
initialiser giving the account name, opening balance, and overdraft limit (0 or above)

deposit(self, float)
Deposits the stated amount into the account, and adjusts the balance appropriately.
Deposits must be a positive amount.

withdraw(self, float)
Withdraws the stated amount from the account, prints a message of “<Name> has withdrew £<amount>. New balance is £<amount>”.
If an invalid amount is requested, then the following message should be printed, and the method should then terminate: “Can not withdraw £<amount>”

getAvailableBalance(self)
Returns the total balance that is available in the account as a float. It should also take into account any overdraft that is available.

getBalance(self)
returns the balance of the account as a float. If the account is overdrawn, then it should return a negative value.

printBalance(self)
Should print to screen in a sensible way the balance of the account. If an overdraft is available, then this should also be printed and it should show how much overdraft is remaining.
getName(self)
Returns the name of the account holder as a string

getAcNum(self)
Returns the account number as a string

issueNewCard(self)
Creates a new card number, with the expiry being 3 years to the month from now. (eg: if today is 3/12/20, then the expiry date would be (12/23))

closeAccount(self)
To be called before deleting of the object instance. Returns any balance to the customer (via the withdraw method) and returns True.
Returns False if the customer is in debt to the bank, and prints message “Can not close account due to customer being overdrawn by £<amount>”
Clarification: You shouldnt actually delete the account instance.... this function will simply do the relevant house keeping in the account, and return a boolean

setOverdraftLimit(self, float)
Sets the overdraft limit to the stated amount

 

In addition to the above, you must also define suitable string representations that give the account name, available balance, and overdraft details (that is: you need to also implement the __str__ methods for each class).

 

You must keep both classes in a single file: BankAccounts.py

You may write some test code in the main body, but this must not run if your file is imported into another module.

You should not use any libraries, other than those specified, and a penalty will be imposed if extra unneeded libraries are used.
