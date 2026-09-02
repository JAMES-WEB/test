text = """Python is a powerful programming language. It's easy to learn and versatile."""

characters = len(text)
words = len(text.split())
sentences = text.count(".")

print("Characters:", characters)
print("Words:", words)
print("Sentences:", sentences)