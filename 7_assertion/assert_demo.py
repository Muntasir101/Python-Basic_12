user_name = 'mr. smith'
age = 20

try:
    assert 20 in age
    print("Assertion Passed")
except AssertionError:
    print(AssertionError)
    print("Assertion Failed")

print("After Assertion")