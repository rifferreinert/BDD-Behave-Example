Feature: Deposit and Withdraw Money
    The user can deposit funds, increasing the
    balance on an account

    Scenario Outline: Valid deposits
        Given the account starts with $<starting_amount>
        When we deposit $<additional_amount>
        Then the account value is $<new_amount>

        Examples: Different amount combinations
            |starting_amount |additional_amount |new_amount |
            |0               |10                |10         |
            |100             |20                |120        |

    Scenario Outline: Valid withdrawls
        Given the account starts with $<starting_amount>
        When we withdraw $<withdrawal_amount>
        Then the account value is $<new_amount>

        Examples: Different amount combinations
            |starting_amount |withdrawal_amount |new_amount |
            |100             |50                |50         |
            |100             |20                |80         |
    

        

        