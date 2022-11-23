while True:
    prompt = input("Choose a formatter: ")
    prompt = prompt.replace(" ", "")
    if prompt == "plain":
        print("Text without formatting")
    elif prompt == "bold":
        print("**Text**")
    elif prompt == "italic":
        print("*Text*")
    elif prompt == "inline-code":
        print("`Text`")
    elif prompt == "link":
        print("[Text](link)")
    elif prompt == "header":
        print("Text")
    elif prompt == "ordered-list":
        print("1. Text")
    elif prompt == "unordered-list":
        print("* Text")
    elif prompt == "new-line":
        print("")
    elif prompt == "!help":
        print("Available formatters: plain bold italic inline-code link header unordered-list ordered-list new-line")
        print("Special commands: !help !done")
    elif prompt == "!done":
        break
    else:
        print("Unknown formatting type or command")
