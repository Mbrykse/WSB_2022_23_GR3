from behave import given, when, then, step 

@given("there were {start:d} cucumbers")
def step_cucumber(context, start):
    pass 
@when("I eat {eat:d} cucumbers")
def step_eating(context, eat):
    pass 
@then("I should have {left:d} cucumbers") 
def step_
after(context, left):
    pass 