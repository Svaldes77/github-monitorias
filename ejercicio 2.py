# INTEGRANTES:
# samuel alberto valdes Gomez
# santiago velasquez bedoya
# felipe calan

cards = [
    {"number": "1234567890", "pin": "1234", "balance": 10000},
    {"number": "0987654321", "pin": "4321", "balance": 5000},
    {"number": "5678901234", "pin": "5678", "balance": 20000}
]

def find_card(card_number):
    for card in cards:
        if card["number"] == card_number:
            return card
    return None

def perform_transaction(card):
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == card["pin"]:
        available_balance = card["balance"]
        withdrawal_amount = int(input("Enter the amount to withdraw: "))

        if withdrawal_amount <= available_balance:
            card["balance"] -= withdrawal_amount
            print(f"Withdrawal successful. Your remaining balance is: ${card['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Incorrect PIN.")


if __name__ == "__main__":
    while True:
        card_number = input("Enter your card number (or 'q' to quit): ")
        if card_number == 'q':
            break

        card = find_card(card_number)
        
        if card != None:
            print(f"Valid card. Current balance: ${card['balance']}")
            perform_transaction(card)
        else:
            print("Card not found. Please try again.")
    






