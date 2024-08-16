#starting commands
summon = "Jarvis"
investments = "Investments"
go_back = "return"
cancel = "cancel"
home_screen = "exit"

#stock information
AMZN="Amazon: \nCurrently $153 \n+13% ROI" #assign info to variable/ticker
AAPL="Apple: \nCurrently $192 \n-5% ROI"


def stock_info(ticker):
  if ticker == "AMZN":
    print(AMZN)
  if ticker == "AAPL":
    print(AAPL)
  if ticker not in ["AMZN", "AAPL"]:
    print("Invalid ticker")
    stock_info(input("Enter a valid ticker: "))

def market_info():
  print("Market info:")
  print("Market is down 3 points")

def stock_invest(ticker):
  if ticker == "AMZN":
    share = int(input("How many shares do you want to buy? "))
    print("Right away, sir.")
    print("You invested in "+str(share)+ " shares of "+ticker+", for $"+str(share*153)+".")
  if ticker == "AAPL":
    share = int(input("How many shares do you want to buy? " ))
    print("You invested in "+str(share)+ " shares of "+ticker+", for $"+str(share*192)+".")
  if ticker not in ["AMZN", "AAPL"]:
    print("Stock not found")
    stock_invest(input("Enter a valid ticker: "))

    
  
command = input("Enter a command: ")

while command != summon:
  print("invalid command")
  command = input("Enter a command: ")

print("Greetings, I am Jarvis.")
print("")
print("Menu:")
print("Portfolio, Invest")
print("*Use 'dismiss' to end program*")
print("")
command = input("What can I do for you? ")

while command not in ["Portfolio", "Invest", "dismiss"]:
  print("Invalid command")
  command = input("What can I do for you? ")
while command in ["Portfolio", "Invest", "dismiss"]:
  


  if command == "Portfolio":
    stock_or_market = input("Would you like to see your stock investments or the market? ")
    while command == "Portfolio":

      while stock_or_market not in ["stocks", "market", "return", "exit"]:
        print("invalid command")
        stock_or_market = input("Would you like to see your stock investments or the market? ")


      if stock_or_market == "stocks": 
        while stock_or_market == "stocks":
          stock_info(input("Which stock would you like to see? (enter ticker in ALL CAPS) ")) #asks user to input stock ticker
          print('')
          stock_or_market = input("Would you like to see another stock investment or return? (enter stocks or return) ")
          if stock_or_market == "return":
            stock_or_market = input("Would you like to see your stock investments or the market? ")
      if stock_or_market == "market":
        print('')
        market_info()
        print('')
        stock_or_market = input("Return to stocks or exit? (enter return or exit) ")


      if stock_or_market == "return":
        stock_or_market = input("Would you like to see your stock investments or the market? ")

      if stock_or_market == "exit":
        command = input("What can I do for you? ")




  if command == "Invest":
    ___ = input("Would you like to invest in stocks? (enter yes or no) ")
    while command == "Invest":
      while ___ not in ["yes", "no", "cancel"]:
        print("Invalid command")
        ___ = input("Enter appropiate response: ")

      if ___ == "yes":
        print('')
        stock_invest(input("Which stock would you like to invest in? (enter ticker in ALL CAPS) "))
        print('')
        ___ = input("Would you like to invest in another stock? (enter yes or no) ")
      if ___ == "no" or ___ == "cancel":
        print('')
        command = input("What can I do for you? ")

      if ___ == "exit":
        print('')
        command = input("What can I do for you? ")

  

  
  if command == "dismiss":
    print("As you wish")
    print("Goodbye")
    break

  while command not in ["Portfolio", "Invest", "dismiss"]:
    print("Invalid command")
    command = input("What can I do for you? ")