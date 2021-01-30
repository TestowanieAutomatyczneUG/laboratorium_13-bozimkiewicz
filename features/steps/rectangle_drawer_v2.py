from behave import *
from src.RectangleDrawerV2 import rectangle_v2

use_step_matcher('parse')


@given('we have a rectangle drawer')
def step_impl(context):
    context.rectangle = rectangle_v2


@step(u'we want to use {sign}')
def step_impl(context, sign):
    context.sign = sign


@step(u'we want our length to be {length}')
def step_impl(context, length):
    context.length = length


@step(u'we want our width to be {width}')
def step_impl(context, width):
    context.width = width


@when('we want to draw a rectangle using given attributes')
def step_impl(context):
    context.result = context.rectangle(context.length, context.width, context.sign)


@then(u'the result is a rectangle {length}x{width} using {sign} sign')
def step_impl(context, length, width, sign):
    assert context.result == f"{sign}" * int(width) + "\n" + (f"{sign}" + " " * (int(width) - 2) + f"{sign}\n") * (int(length) - 2) + f"{sign}" * int(width)


@then(u'the result is a vertical line with a length {length} using {sign} sign')
def step_impl(context, length, sign):
    assert context.result == f"{sign}\n" * int(length)


@then(u'the result is a horizontal line with a length {width} using {sign} sign')
def step_impl(context, width, sign):
    assert context.result == f"{sign}" * int(width)


@then('the program should return wrong input error')
def step_impl(context):
    assert context.result == 'Wrong input'


