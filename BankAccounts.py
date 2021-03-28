# Name: Orion Assefaw ,COMP517 Assignment 4(CA4)

from random import *
import datetime


class BasicAccount():
    """
    Basic Account allows the general management of the bank account objects
    such us creating account, depositing, withdrawing and etc.
    """
    __serialNo = 1
    def __init__(self, acName, openingBalance):
        """
        Basic Account constructor function.
        Parameters:
            acName: string - The Account holders Name
            openingBalance: float - The account opening balance
        
        Returns:
            Nothing
        """
        
        self.name = acName
        self.startBalance = openingBalance
        self.balance = float(openingBalance)
        
        self.acNum = BasicAccount.__serialNo 
        BasicAccount.__serialNo += 1

        self.cardNum = ""
        for i in range(16):
            self.cardNum += str(randint(0,9))

        today = datetime.date.today()
        threeYrs = datetime.timedelta(days=1095.75)
        after3Yrs = today + threeYrs
        expiryDate = after3Yrs.strftime('%m/%y')
        self.cardExp = expiryDate
        

    def __str__(self):
        """
        A function that returns a string representation of the bank account object. It includes Account Holder's Name, Account Number and balance.

        Parameters:
            Nothing

        Returns:
            Nothing
        """
        
        return 'Account Name: {self.name}, Account Number: {self.acNum}\nAccount Type: Basic Account\nAccount Balance: £{self.balance}'.format(self=self)

    def deposit(self, amount):
        """
        Deposits a fixed amount into the Basic Account instance.

        Parameters:
            amount: float - the amount that is to be deposited or added to the account
        Returns:
            Nothing
        """
        self.balance += float(amount)   

    def getAvailableBalance(self):
        """
        Returns the total balance that is available in the account. 
        It also takes into account any overdraft that is available.

        Parameters:
            nothing
        Returns:
            balance: float
        """     
        return float(self.balance)
        
        

    def getBalance(self):
        """
        Returns the account balance. If the account is overdrawn, it returns negative balance values.

        Parameters:
            nothing
        Returns:
            balance: float
        """
        return float(self.balance)

    def printBalance(self):
        """
        Prints and displays the account holder's name and account balace.

        Parameters:
            nothing
        Returns:
            nothing
        """
        print(self.name+"'s account balance is: £"+str(self.balance))     

    def withdraw(self, amount):
        """
        Withdraws a fixed amount from the Basic Account instance, provided the amount is not more than the account balance.

        Parameters:
            amount: float - the amount that is to be withdrawn
        Returns:
            Nothing
        """
        if (amount <= self.getAvailableBalance()):
            self.balance -= float(amount)
            print(self.name, "has withdrew £"+str(amount)+". New balance is £"+str(self.balance))
        else:
            print("Can not withdraw £"+str(amount))
            raise SystemExit
    
    

    def getName(self):
        """
        Returns the name of the account holder.

        Parameters:
            nothing

        Returns:
            name: string
        """
        return self.name
    
    def getAcNum(self):
        """
        Returns the account number, based on a serial number.

        Parameters:
            nothing

        Returns:
            acNum: string
        """
        return str(self.acNum)
    
       
    def issueNewCard(self):
        """
        Creates a new card having a unique 16 digit long number and expiry date (set to 3 years after creation time).

        Parameters:
            nothing

        Returns:
            nothing
        """
        self.cardNum = ""
        for i in range(16):
            self.cardNum += str(randint(0,9))

    def closeAccount(self):
        """
        This function does house keeping in the account, before the account gets deleted. 
        It returns any balance to the customer and if customer account is overdrawn, notifies that the
        account can not be closed, displaying the amount the customer is owed.

        Parameters:
            nothing

        Returns:
            True/False: boolean (depending on wether or not account can be closed)
        
        """
        if (self.balance >= 0):
            amount = self.balance
            self.withdraw(amount)
            return True
        else:
            print("Can not close account due to customer being overdrawn by £"+str(-1*(self.balance)))
            return False
                

class PremiumAccount(BasicAccount):
    """
    Premium Account allows the general management of the premium type of bank account objects
    for all the basic functionalities as well as the added overdraft management functionalities. 
    """

    def __init__(self,acName, openingBalance,initialOverdraft):
        """
        Premium Account constructor function.
        Parameters:
            acName: string - The Account holders Name
            openingBalance: float - The account opening balance
            initialOverdraft: float - The allowed overdraft amount in the account
        
        Returns:
            Nothing
        """
        super().__init__(acName, openingBalance)
        self.overdraftLimit = float(initialOverdraft)
        if(self.overdraftLimit > 0):
            self.overdraft = True
        else:
            self.overdraft = False 

    def __str__(self):
        
        """
        A function that returns a string representation of the Premium account object. It includes Account Holder's Name, Account Number, balance and overdraft details.

        Parameters:
            Nothing

        Returns:
            Nothing
        """      
        return 'Account Holders Name: {self.name}\nAccount Type: Premium Account\nAccount Balance: £{self.balance}\nAgreed Overdraft in the account is: £{self.overdraftLimit}'.format(self=self)


    def setOverdraftLimit(self, thenewlimit):
        """
        setOverdraftLimit will update the overdraft limit of a Premium bank account instance if the account is allowed to have overdraft.

        Parameters:
            thenewlimit: float - The new overdraft limit

        Returns:
            nothing
        """
        if((self.overdraft == True) and (thenewlimit != 0)):
            self.overdraftLimit = float(thenewlimit)
        elif((self.overdraft == True) and (thenewlimit == 0)):
            self.overdraftLimit = float(thenewlimit)
            self.overdraft = False
        else:
            #self.overdraft == False
            raise SystemExit
            

  
    def getAvailableBalance(self):
        """
        Returns the total balance that is available in the account. 
        It also takes into account any overdraft that is available.

        Parameters:
            nothing
        Returns:
            balance: float
        """ 
        
        return float(self.balance + self.overdraftLimit)

    def printBalance(self):
        """
        Prints and displays the account holder's name , account balace, overdraft and remaining overdraft.

        Parameters:
            nothing
        Returns:
            nothing
        """
        if(self.balance >= 0):
            remaining = self.overdraftLimit
        else:
            remaining = self.overdraftLimit + self.balance

        print(self.name+"'s account balance is: £"+str(self.balance))
        print("The overdraft in this account is: £"+str(self.overdraftLimit)+".\n"+"Of this overdraft, £"+str(remaining)+" is remaining.")
    