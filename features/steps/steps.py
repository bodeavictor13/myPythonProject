from behave import *
# from twentyone import *
# backgound
@given(u'a global administrator named "Greg"')
def step_impl(context):
    1+1


@given(u'a blog named "Greg\'s anti-tax rants"')
def step_impl(context):
    1+1


@given(u'a customer named "Wilson"')
def step_impl(context):
    1+1

# table comming
@given(u'the following people exist:')
def step_impl(context):
    1+1
#        for row in context.table:
#            a = row


@given(u'some precondition 1')
def step_impl(context):
    1+1


@when(u'some action by the actor')
def step_impl(context):
    1+1


@when(u'some other action')
def step_impl(context):
    1+1


@then(u'some testable outcome is achieved')
def step_impl(context):
    # print('STEP: Then some testable outcome is achieved')
    assert(1==0)


@then(u'something else we can check happens too')
def step_impl(context):
    # print('STEP: Then something else we can check happens too')
    assert(1==0)

@given(u'something else we can check happens too')
def step_impl(context):
    1+1


# scenario 2
@given(u'some precondition')
def step_impl(context):
    1+1
#    context.scenario.skip(reason="skip scenario 2")


@given(u'some other precondition with doc string')
def step_impl(context):
    1+1


@when(u'yet another action')
def step_impl(context):
    1+1

# # *
# @given('something else we can check happens too')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given something else we can check happens too')


@given(u'I don\'t see something else')
def step_impl(context):
    1+1


# scenario 3
@given(u'the cow weighs {weight} kg')
def step_impl(context, weight):
    1+1
    # print('STEP: Given the cow weighs kg: ' + weight)


@when(u'we calculate the feeding requirements')
def step_impl(context):
    1+1


@then(u'the energy should be {energy} MJ')
def step_impl(context, energy):
    # print('STEP: Then the energy should be MJ: ' + energy)
    assert(1==0)


# @given(u'a blog named "Greg\'s anti-tax rants"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given a blog named "Greg\'s anti-tax rants"')


# @given(u'the cow weighs 500 kg')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given the cow weighs 500 kg')
#
#
# @then(u'the energy should be 29500 MJ')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the energy should be 29500 MJ')
