def get_total_spent(transactions):

    total = 0
    for transaction in transactions:
        total += transaction["price"]

    print(f"TOTAL SPENT: {total}")


def list_bank_card_transaction(transactions):

    # first solution to filter
    # for index in range(0, len(transactions) - 1):
    #     if transactions[index]["payment_method"] == "BANK_CARD":
    #         del transactions[index]

    # second solution to filter
    # transactions = list(filter(lambda t: t["payment_method"] == "BANK_CARD", transactions))

    print(transactions)


if __name__ == "__main__":
    transactions = [
        {
            "description": "IKEA",
            "price": 10.99,
            "payment_method": "BANK_CARD"
        },
        {
            "description": "ASOS",
            "price": 56.40,
            "payment_method": "BANK_CARD"
        },
        {
            "description": "McDonald",
            "price": 11.23,
            "payment_method": "CASH"
        }
    ]

    list_bank_card_transaction(transactions)
    get_total_spent(transactions)