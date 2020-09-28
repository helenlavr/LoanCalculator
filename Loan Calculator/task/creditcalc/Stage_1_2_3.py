import math

"""
Stage 1/4:
loan_principal = 'Loan principal: '
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(loan_principal, first_month, second_month, third_month, final_output, sep='\n')
"""

"""
Stage 2/4



def calculate_number_of_monthly_payments(principal, payment):
    months = math.ceil(principal / payment)
    if months > 1:
        print('It will take', months, 'months to repay the loan')
    else:
        print('It will take', months, 'month to repay the loan')


def calculate_monthly_payments(principal, months):
    payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * payment
    if last_payment < payment:
        print('You monthly payment =', payment, 'and the last payment =', last_payment)
    else:
        print('You monthly payment = ', payment)


def main():
    loan_principal = int(input('Enter the loan principal: '))
    calculation = input('What do you want to calculate? \ntype "m" - for number of monthly payments, \ntype "p" - for the monthly payment: \n')
    if calculation == 'm':
        monthly_payment = int(input('Enter the monthly payment:\n'))
        calculate_number_of_monthly_payments(loan_principal, monthly_payment)
    elif calculation == 'p':
        number_of_months = int(input('Enter the number of months:\n'))
        calculate_monthly_payments(loan_principal, number_of_months)


main()
"""
"""
Stage 3/4
"""


def interest_rate(i):
    i = i * 0.01 / 12
    new_i = round(i, 2)
    return i, new_i     # if input i = 10 -> (0.008333..., 0.01)


def annuity_payment(p, i, n):
    a = p * ((i * math.pow(1 + i, n)) / ((math.pow(1 + i, n)) - 1))
    return a


def loan_principal(a, n, i):
    p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    return p


def number_of_payments(a, i, p):    # number of months/number_of_periods
    n = math.ceil(math.log(a / (a - i * p), (1 + i)))
    return n


def convert_months(a, i, p):    # convert months to year(s) and months
    n = number_of_payments(a, i, p)
    years = math.floor(n / 12)
    months = n % 12
    return years, months       # (months if months != 0 else months)


def main():
    calculation = input('What do you want to calculate? \ntype "n" for number of monthly payments, \ntype "a" for annuity monthly payment amount , \ntype "p" for the monthly payment: \n')
    if calculation == 'n':
        p_loan_principal = int(input('Enter the loan principal: \n'))     # p
        monthly_payment = int(input('Enter the monthly payment:\n'))    # a
        loan_interest = float(input('Enter the loan interest: \n'))     # i
        i = interest_rate(loan_interest)[0]
        years_months = convert_months(monthly_payment, i, p_loan_principal)
        print('It will take', years_months[0], 'years and', years_months[1], 'months to repay this loan!')
        """
        IF its necessary to have the correct endings with month(s) and year(s)
        if years_months[0] == 0:
          print('It will take', years_months[1], 'months to repay this loan!')
        elif years_months[0] == 0 and years_months[1] == 1:
          print('It will take', years_months[1], 'month to repay this loan!')
        elif years_months[0] == 1 and year_months[1] == 1:
          print('It will take', years_months[0], 'year and', years_months[1], 'month to repay this loan!')
        elif years_months[0] == 1:
          print('It will take', years_months[0], 'year and', years_months[1], 'months to repay this loan!')
        else:
          print('It will take', years_months[0], 'years and', years_months[1], 'months to repay this loan!')
        """
    elif calculation == 'a':
        p_loan_principal = int(input('Enter the loan principal: \n'))         # p
        number_of_periods = int(input('Enter the number of periods: \n'))   # n
        loan_interest = float(input('Enter the loan interest: \n'))         # i
        i = interest_rate(loan_interest)[0]
        a = math.ceil(annuity_payment(p_loan_principal, i, number_of_periods))
        print('Your monthly payment = {}!'.format(a))
    elif calculation == 'p':
        a_annuity_payment = float(input('Enter the annuity payment: \n'))     # a
        number_of_periods = int(input('Enter the number of periods: \n'))     # n
        loan_interest = float(input('Enter the loan interest: \n'))           # i
        i = interest_rate(loan_interest)[0]
        p = math.floor(loan_principal(a_annuity_payment, number_of_periods, i))
        print('Your loan principal = {}!'.format(p))


main()

