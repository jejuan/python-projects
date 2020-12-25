def mortgageAmount():
    amount = input("What is the price of the home? ")
    return int(amount)


def downPayment():
    downpayment = input("How much is your down-payment? ")
    return int(downpayment)


def loanTerm():
    term = input("How long will you be financing you home in years? ")
    return int(term)


def main():
    amount = mortgageAmount()
    downpayment = downPayment()
    term = loanTerm()
    loanAmount = amount - downpayment
    print(loanAmount / (term * 12), " /month")


main()
