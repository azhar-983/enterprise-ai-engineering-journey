name = "Azhar"
language = "Python"
greeting = "Hello, " + name + "!"

print(greeting)
print(f"{name} is learning {language}.")
print(f"The greeting has {len(greeting)} characters.")
print(f"The first character of {name} is {name[0]}.")
print(f"The first two characters of {language} are {language[:2]}.")
print(f"Uppercase: {greeting.upper()}")
print(f"Lowercase: {greeting.lower()}")
print(f"Title case: {greeting.title()}")
print(f"Contains 'Azhar': {'Azhar' in greeting}")
print(f"Starts with 'Hello': {greeting.startswith('Hello')}")
print(f"Position of '{name}': {greeting.find(name)}")
print(f"Number of 'l' characters: {greeting.count('l')}")

sentence = "  Strings are easy to learn.  "
clean_sentence = sentence.strip()
words = clean_sentence.split()
print(f"Trimmed text: '{clean_sentence}'")
print(f"Words: {words}")
print(f"Word count: {len(words)}")
print(f"Joined with hyphens: {'-'.join(words)}")
print(f"Replace 'easy' with 'fun': {clean_sentence.replace('easy', 'fun')}")
