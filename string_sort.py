def get_only_letters(elem):
    if not elem.isalpha():
        return "".join((char for char in elem if char.isalpha()))
    return elem

def sort_by_letter(arr):
    return sorted(arr, key=get_only_letters)

l = ["99a", "78b", "c2345", "11d"]

h = []

print(sort_by_letter(l))
