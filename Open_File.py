# Old method
    #f = open('secret.txt')
    #text = f.read()
    #f.close()

    #print(text)


# New better method
with open("secret.txt") as f:       # Automatically closes the file!
    text = f.read()
    print(text)