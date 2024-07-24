def is_title_easy(text):
    return text.istitle()

def is_title_with_split(text):
    words = text.split(" ")
    for word in words:
        if (word[0].isupper() or not word[0].isalpha()) and not word[1:].isupper():
            continue
        else:
            return False
    return True
        


test_list = [
             "Potatoes ARE Nice",
             "Apples + Oranges",
             "My Dog Is Cute",
             "Yes she is",
             "9999 Lollypops",
             "A Mind Boggling Achievement",
             "A Simple Python Program!",
             "Water is transparent",
             "YEEEHAAAWW"
             ]


for text in test_list:
    print(is_title_with_split(text))
