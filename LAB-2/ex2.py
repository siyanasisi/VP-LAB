text = input("Enter a string: ")
word = input("Enter a word to search for: ")

text = text.lower()
word = word.lower()

if word in text: 
    count = text.count(word)
    index = text.index(word)
    print(f" the word '{word}' was found {count} times in the text")
    print(f"the first occurrence of the word '{word}' is at index {index} ")

else: 
    print(f"the word '{word}' was not found in the text ")