single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line-string"""
text = "Python Programming"
name = " bob the builder"

name1 = "John Doe"
age = 30

message_1 = f"My name is {name1} and I am {age} years old."  # f-strings
message_2 = "My name is {} and I am {} years old.".format(name1, age)  # str.format()
message_3 = "My name is %s and I am %.1f years old." % (name1, age)  # %-formatting

print(message_1)
print(message_2)
print(message_3)

print(single_quote)
print(double_quote)
print(triple_quote)
print(text)
print(len(text))
print(text[0])
print(text[-1])
print(text[0:6])
print(text[:6])
print(text[7:])

print(len(name))
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("bob", "jane"))