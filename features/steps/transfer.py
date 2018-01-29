from behave import given, when, then
from account import Account

@given('a checking account with ${first_balance_start:d}')
def step_impl(context, first_balance_start):
    context.checking = Account(first_balance_start)

@given('a savings account with ${second_balance_start:d}')
def step_impl(context, second_balance_start):
    context.savings = Account(second_balance_start)

@when('we transfer ${transfer_amount:d} from checking to savings')
def step_impl(context, transfer_amount):
    context.checking.transfer_to(context.savings, transfer_amount)

@then('the checking account has a balance of ${first_balance_end:d}')
def step_impl(context, first_balance_end):
    assert context.checking.current_value == first_balance_end

@then('the savings account has a balance of ${second_balance_end:d}')
def step_impl(context, second_balance_end):
    assert context.savings.current_value == second_balance_end
    