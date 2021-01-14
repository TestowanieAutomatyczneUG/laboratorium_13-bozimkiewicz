from behave import *
from src.RectangleDrawer import RectangleDrawer


@given('there is a rectangle drawer')
def step_impl(context):
    context.rectangle = RectangleDrawer()


@when('we draw a rectangle using length = 3 width = 4')
def step_impl(context):
    context.result = context.rectangle.rectangle(3, 4)


@then('the result is a rectangle 3x4')
def step_impl(context):
    assert context.result == '****\n*  *\n****'


@when('we draw a rectangle using length = 3 width = -3')
def step_impl(context):
    context.result = context.rectangle.rectangle(3, -3)


@then('the result is Wrong input')
def step_impl(context):
    assert context.result == 'Wrong input'


@when('we draw a rectangle using length = -5 width = -2')
def step_impl(context):
    context.result = context.rectangle.rectangle(-5, -2)


@when('we draw a rectangle using length = 3 width = 3')
def step_impl(context):
    context.result = context.rectangle.rectangle(3, 3)


@then('the result is a rectangle 3x3')
def step_impl(context):
    assert context.result == '***\n* *\n***'


@when('we draw a rectangle using length = 0 width = 0')
def step_impl(context):
    context.result = context.rectangle.rectangle(0, 0)
