def is_title_easy(text):
    return text.istitle()


test_list = [
             "Potatoes ARE Nice",
             "My Dog Is Cute",
             "Yes she is",
             "9999 Lollypops",
             "A Mind Boggling Achievement",
             "A Simple Python Program!",
             "Water is transparent",
             ]


for text in test_list:
    print(is_title_easy(text))
