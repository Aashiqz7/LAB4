# This list has a nested list element.
# ... It cannot be summed with sum.
values = [10, [20, 30]]

# This will cause a TypeError.
result = sum(values)
print(result)

