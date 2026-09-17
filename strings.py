sentence = "  the Quick Brown Fox  "

cleaned = sentence.strip().title()
print(cleaned)

words = cleaned.split()
print(words)
print(len(words))

joined = "-".join(words)
print(joined)

print("Fox" in sentence)
print(sentence.strip().lower().startswith("the"))
