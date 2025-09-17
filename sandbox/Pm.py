import yfinance as yf

# user_info = [username, password, cash_balance, ]

def main():
    login_input = input("Welcome to DC Portfolio Management System. Please enter a 1 to login or a 2 to make an account: ")
    
    def login_signup():
        if login_input == 1:
            input("Enter your username: ")
            password = input("Enter your password: ")
        elif login_input == 2:
            username = input("Enter the username you want: ")
            password = input("Enter the password you would like: ")
    
    print(f"Welcome to your profile. Your cash balance is {cash_balance}, and you own these stocks: {stocks}")
    main_choices = input("Enter a 1 to buy a stock, a 2 to sell sahres you own, a three to deposit cash, or a 4 to withdraw cash")
    
    def main_options():
        if main_choices == 1:
            stock_pick = input("Enter a stock's ticker you would like to buy: ")
            # print(stocks_info[stock_pick])
            purchase_amount = input("Enter a dollar amount you would like to buy: ")
            cash_balance = cash_balance - purchase_amount
            stocks_balance += stocks[stock_pick] / purchase_amount
            print(f"Congrats! You purchased {purchase_amount} of {stock_pick}")