from behave import given, when, then
from account import Account


@given("the account starts with $0")
def step_impl(context):
    context.account = Account(0)


@when("we deposit $10")
def step_impl2(context):
    context.account.deposit(10)


@then("the account value is $10")
def step_impl3(context):
    assert context.account.current_value == 10