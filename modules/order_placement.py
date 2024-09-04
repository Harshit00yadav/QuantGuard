from dhanhq import dhanhq


class DhanHQ:
    def __init__(self, client_id, access_token):
        self.broker = dhanhq(client_id, access_token)

    def get_funds(self):
        funds = self.broker.get_fund_limits()
        return funds["data"]["availabelBalance"]

if __name__ == "__main__":
    broker = DhanHQ()
    print(broker.get_funds())
