class Atm:

    def __init__(self,cardNumber,PinNumber,balance,name):
        self.cardNumber=cardNumber
        self.PinNumber=PinNumber
        self.balance=balance
        self.name=name

        


    def cashWithdraw(self,amount):
        if self.balance-amount > 0:
            self.balance=self.balance-amount
            print("$",amount," withdrawn. Current Balance: $",self.balance)
        else:
            print("You don't have enough money")

    def cashDeposit (self,Money):
        Money = input("How much money would you like to deposit: ")
        self.balance=self.balance+Money
        print ("Yay you deposited $" + Money + "your current balance is $" + self.balance)

    def balanceEnquiry (self):
         print ("Welcome to the Online Atm")
         CardNo = input ("Please enter your card number: ")
         PinNo = input ("please enter your pin number: ")
         BalanceEnquiring = input ("Would like to know how much money you have currently? type YES or NO: ")
         if BalanceEnquiring == "YES":
            print ("Your current balance is: $" + self.balance)

manasvi=Atm("1234","9056","0","Manasvi")
print(manasvi.balanceEnquiry())





