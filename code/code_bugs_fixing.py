#for i in range(1, 4):
 #   j = i * 2
#   print(f"i is {i} and j is {j}")
    
    
#just buggy code...
def add_underscores(word):
    new_word = "_"
    for letter in word:
        new_word = new_word + letter + "_"
        print(f"i = {i}; new_word = {new_word}")
    return new_word
    
phrase = "hello"
print(add_underscores(phrase))