Feature: Transfer Money
    The user can transfer money between accounts

    Scenario Outline: Transfering money between two accounts
        Given a checking account with $<first_balance_start>
        And a savings account with $<second_balance_start>
        When we transfer $<transfer_amount> from checking to savings
        Then the checking account has a balance of $<first_balance_end>
        And the savings account has a balance of $<second_balance_end>

        Examples:
        | first_balance_start | second_balance_start | transfer_amount | first_balance_end | second_balance_end |
        | 500                 | 1000                 | 200             | 300               | 1200               |