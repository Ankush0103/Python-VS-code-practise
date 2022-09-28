myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are", myDict.keys())
a = input("Enter the Hindi word: \n")
# print("The meaning of your word is: \n", myDict[a]) # This progrram can show error if key is not in dictionary.

# Below line will not throw an error if the key is not present in the dictionary.
print("The meaning of your word is:", myDict.get(a))