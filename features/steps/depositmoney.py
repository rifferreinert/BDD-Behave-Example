from behave import given, when, then
from account import Account


@given("the account starts with ${starting_amount:d}")
def step_impl(context, starting_amount):
    context.account = Account(starting_amount)


@when("we deposit ${additional_amount:d}")
def step_impl(context, additional_amount):
    context.account.deposit(additional_amount)


@when("we withdraw ${withdrawal_amount:d}")
def step_impl(context, withdrawal_amount):
    context.account.withdraw(withdrawal_amount)


@then("the account value is ${new_amount:d}")
def step_impl(context, new_amount):
    assert context.account.current_value == new_amount
