from modules.startup_inti import Logo
from modules.moneymanagement import main
from modules.order_placement import DhanHQ

logo = Logo("assets/logo.txt")
logo.display()
C_ID, A_TOK = "", ""
with open("credentials/Harshit.txt", "r") as cred:
    C_ID = cred.readline().split(":")[1].replace("\n", "")
    A_TOK = cred.readline().split(":")[1].replace("\n", "")
try:
    broker = DhanHQ(C_ID, A_TOK)
    funds = float(broker.get_funds())
except:
    funds = float(input("Enter amount : "))
main(funds)
