def replace_word():
    input_string = "Hi guys, I am John"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    
    replaced_string = input_string.replace(word_to_replace, word_replacement)
    print("Modified string:", replaced_string)

replace_word()
