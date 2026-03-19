languages = {"Python", "Java", "C++", "Go"}

user_input = input("Enter a language: ")

if user_input in languages:
    print("Language exists in the set")
else:
    print("Language not found")