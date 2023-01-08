'''
Write a program that:
• asks the user to input a sentence
• asks the user to input:
• the word they want to replace
• the word they want to replace it with
• outputs the new sentence

"".replace("old string", "new string") -> how to replace a string
"hello world".replace("hello", "Hello") -> output "Hello world"

Variables
String Manipulation
'''
sentence = input("What is the sentence?")
replacement = input("word you'd like to replace?")
placement = input("what word to replace with")
print(f"{sentence.replace(replacement, placement)}")