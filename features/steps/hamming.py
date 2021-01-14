from behave import *
from src.Hamming import Hamming


@given('there is a hamming class')
def step_impl(context):
    context.hamming = Hamming()


@when('we calculate distance between two empty strands')
def steps_impl(context):
    context.result = context.hamming.distance('', '')


@then('the result is 0')
def steps_impl(context):
    assert context.result == 0


@when('we calculate distance between two identical single letter strands')
def steps_impl(context):
    context.result = context.hamming.distance('A', 'A')


@when('we calculate distance between two different single letter strands')
def steps_impl(context):
    context.result = context.hamming.distance('G', 'T')


@then('the result is 1')
def steps_impl(context):
    assert context.result == 1


@when('we calculate distance between two different long strands')
def steps_impl(context):
    context.result = context.hamming.distance("GGACGGATTCTG", "AGGACGGATTCT")


@then('the result is 9')
def steps_impl(context):
    assert context.result == 9


@when('we calculate distance between two identical long strands')
def steps_impl(context):
    context.result = context.hamming.distance("GGACGGATTCTG", "GGACGGATTCTG")


@then('the result is Values cannot be of different length')
def steps_impl(context):
    assert context.result == 'Values cannot be of different length'


@when('we calculate distance between two strands and first is longer')
def steps_impl(context):
    context.result = context.hamming.distance('AATG', 'AAA')


@when('we calculate distance between two strands and second is longer')
def steps_impl(context):
    context.result = context.hamming.distance('AAA', 'AATG')


@when('we calculate distance between two strands and first is empty')
def steps_impl(context):
    context.result = context.hamming.distance('', 'AATG')
