# 08 List Comprehension

numbers = [5, 10, 21, 70]
triples = [ number*3 for number in numbers] #  [expression for item in iterable]
print(triples)

celcius = [15.0, 88.75, 120.0, 37.0]
fahrenheit = [ 9/5 * c + 32 for c in celcius]
print(fahrenheit)

# Conditional in List Comprehension

numbers = [5, 10, 21, 70]
triples = [num * 3 for num in numbers if num % 2 == 0 ] # [expression for item in iterable if condition == True]
print(triples)

text = input()
print(sum([ch for ch in text if ch.lower() in "aeiou"]))
