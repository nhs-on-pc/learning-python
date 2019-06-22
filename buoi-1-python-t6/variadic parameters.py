def function(bob, sally, *args):
    print(bob, sally, args)

values = [1, 2, 3, 4]
function(bob="Hi bob", sally="Hello sally", *values)