def main(capital):
    risk_per_day = 5
    trade_frequency = 3
    RR = 2.5
    max_risk = capital*risk_per_day/100
    risk_per_trade = max_risk/trade_frequency
    
    diff = len(str(int(max_risk))) - len(str(int(risk_per_trade)))
    rpdstr = f"│ risk per day    : {int(max_risk)} ₹ │"
    rptstr = f"│ risk per trade  : {int(risk_per_trade)} ₹ "+" "*diff+"│"
    diff = len(rpdstr) - len(str(capital)) - 16
    move_up_clear = u"\r\033[A\033[2K"
    resetcolor = u"\033[0m"
    blackonwhite = u"\033[47;30m"
    print(move_up_clear+"╭"+blackonwhite+f" capital : {capital} ₹ "+resetcolor+"─"*diff+"╮")
    
    print(rpdstr)
    print(rptstr)
    print(f"╰{'─'*(len(rpdstr)-2)}╯")
    print("\nQuantity = Not defined")
    while True:
        SL_pips = float(input("enter pips of stop loss : "))
        if SL_pips == 0:
            break
        quantity = risk_per_trade / SL_pips
        print(u"\r\033[2A\033[2k"+f"Quantity = {quantity}")
