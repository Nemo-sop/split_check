class Friendship_conserver():
    def __init__(self):
        pass



    def divide_expensess(self, guest_expensess):
        total = 0
        for guest in guest_expensess:
            total += guest_expensess[guest]
        self.total_spent = total
        self.individual_spent = total/len(guest_expensess) 
        print(f'[INFO] Total spent: {self.total_spent}')
        print(f'[INFO] Individual spent: {self.individual_spent}')

    def balance(self, guest_expensess):
        self.debts = {}
        for guest in guest_expensess:
            self.debts[guest] = guest_expensess[guest] - self.individual_spent
        print(f'[INFO] Debts: {self.debts}')
        self.transfers = {}
    
    def calculate_transfers(self):
        debts = self.debts
        debtors = {name: abs(amount) for name, amount in debts.items() if amount < 0}
        creditors = {name: amount for name, amount in debts.items() if amount > 0}

        self.transfers = []
        
        while debtors and creditors:
            debtor, debt_amount = debtors.popitem()
            creditor, credit_amount = creditors.popitem()
            
            amount_to_transfer = min(debt_amount, credit_amount)
            amount_to_transfer_rounded = round(amount_to_transfer, 2)
            
            self.transfers.append(f"{debtor} transfers {amount_to_transfer_rounded} to {creditor}")
            #print(self.transfers)
            
            if debt_amount > credit_amount:
                debtors[debtor] = debt_amount - amount_to_transfer
                #creditors[creditor] = credit_amount
            elif debt_amount < credit_amount:
                creditors[creditor] = credit_amount - amount_to_transfer
                #debtors[debtor] = 0  # Debt is settled
            else:
                # Both debts are settled
                continue

        print(f'[INFO] Debts: {self.transfers}')

        
        return self.transfers
        
        
    def get_info(self):
        return

def main(guest_expensess: dict):
    # guest_expensess = {'nico':1000, 'tomas':2000}
    divider = Friendship_conserver()
    #print('[INFO] Friendship_conserver loaded')
    print(f'[INFO] Guest list: {guest_expensess}')
    divider.divide_expensess(guest_expensess)
    divider.balance(guest_expensess)
    divider.calculate_transfers()

guest_expensess = {'nico':3000, 'igna':5500, 'lucas':4700}
result = main(guest_expensess)
print(result)