para = "Ank is a good boy"
print(len(para)) # Output is 17 i.e. gaps between the words are also counted.
print(para.endswith("sjddaljd")) # output is False because para does not end with given quoted words.
print(para.endswith("boy")) # Output is True because para ends with boy.
print(para.count("o")) # Output is 3 i.e good has 2 o and boy has 1 o.
print(para.count("A")) # output is 1 Ank has A, a will not be counted because python is case sensitive language.
print(para.replace("Ank", "Ankur")) # Ouput replaces Ank with Ankur and gives Ankur is a good boy

story = "once upon a Time upon"
print(story.capitalize()) # Output converts small o To block O, capitalize converts first word of string to capital letter.
print(story.find("Time")) # output gives 12 i.e. finf function tells us at which index our word is.
print(story.find("Upon")) # output is -1 because there is no Upon in our string named  story.
print(story.find("upon")) # output is 5 because find function will only give index of first occurence of thde given word.
