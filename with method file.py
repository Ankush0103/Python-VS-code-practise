with open('Hello Ankush.txt', 'r') as f:
    a = f.read()
    print(a) # We don't need to write fclose() when we are using with function.