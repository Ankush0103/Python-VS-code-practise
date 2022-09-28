def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()
    
this = "      Ankur is Good     "
# print(this)
# print(this.strip()) # Strip removes spaces between "  "
n = remove_and_split(this, "Harry")
print(n)