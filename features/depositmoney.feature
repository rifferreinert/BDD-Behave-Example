Feature: Deposit Money
    The user can deposit funds, increasing the
    balance on an account

    Scenario: The account is empty
        Given the account starts with $0
        When we deposit $10
        Then the account value is $10
        

        