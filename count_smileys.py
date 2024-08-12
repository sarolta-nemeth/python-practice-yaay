#counts the smiley facesin an array of strings
#valid: eye: :, ; nose(optional): -, ~ mouth: ), D

def count_smileys(arr):

    counter = 0
    options = [":;", "-~", ")D"]
    
    def is_smiley(string):
        for i in range(len(string)):
            if string[i] in options[i]:
                continue
            elif i == 1 and string[i] in options[i + 1]:
                continue
            else:
                return False
        return True
    
    if len(arr):
        for string in arr:
            if is_smiley(string):
                counter += 1
        return counter
    return counter
                    
test_arr = [[], [":)", ";(", ";}", ":-D"], [";D", ":-(", ":-)", ";~)"], [";]", ":[", ";*", ":$", ";-D"]]

for arr in test_arr:
    print(count_smileys(arr))
                
        
