# Define a class to represent a bank account. Include the following details like name of the depositor, account number, type of account, balance amount in the account. Write methods to assign initial values, to deposit an amount, withdraw an amount after checking the balance, to display name, account number , account type and balance  
class bank:
  def geti(self):
    self.name=input("Name: ")
    self.acno=input("Account no:")
    self.tyac=input("Account type: ")
    self.bal=0
    
  def dep(self):
    print("")
    self.depo=int(input("Amount to deposite:"))
    self.bal=self.bal+self.depo
    print("Balance: ",self.bal)
  
  def wid(self):
    print("")
    self.widr=int(input("Amount to withdarw:"))
    self.bal=self.bal-self.widr
    print("Balance: ",self.bal)
  
  def dis(self):
    print("")
    print( "Name: ",self.name)
    print( "AC no : ",self.acno)
    print( "AC type: ",self.tyac)
    print("Balance: ",self.bal)


b1=bank()
b1.geti()
b1.dep()
b1.wid()
b1.dis()