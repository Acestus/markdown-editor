
formats = ["plain", "bold", "italic", "inline-code", "link", "header", "new-line"]
full_text = ""
def set_plain():
    return (get_text())
def set_bold():
    return (f"**{get_text()}**")

def set_italic():
    return (f"*{get_text()}*")

def set_inline_code():
    return (f"`{get_text()}`")

def set_link():
    label = input("Label: ")
    url = input("URL: ")
    return (f"[{label}]({url})")

def set_header():
    while True:
        level = int(input("Level: "))
        if level in range(1, 7):
            return (f"{'#' * level} {get_text()}\n")
            break
        else:
            print("The level should be within the range of 1 to 6")

def set_ordered_list():
    return (f"1. {get_text()}")

def set_unordered_list():
    return (f"* {get_text()}")

def set_new_line():
    return "\n"

def check_prompt(prompt):
    if prompt not in formats:
        print("Unknown formatting type or command")

def get_text():
    text = input("Text: ")
    return text

def format_text(prompt):
    if prompt == "plain":
        return set_plain()
    elif prompt == "bold":
        return set_bold()
    elif prompt == "italic":
        return set_italic()
    elif prompt == "inline-code":
        return set_inline_code()
    elif prompt == "link":
        return set_link()
    elif prompt == "header":
        return set_header()
    elif prompt == "ordered-list":
        return set_ordered_list()
    elif prompt == "unordered-list":
        return set_unordered_list()
    elif prompt == "new-line":
        return set_new_line()
    elif prompt == "!help":
        print("Available formatters: plain bold italic inline-code link header unordered-list ordered-list new-line")
        print("Special commands: !help !done")
    else:
        print("Unknown formatting type or command")


while True:
    prompt = input("Choose a formatter: ")
    prompt = prompt.replace(" ", "")
    check_prompt(prompt)
    if prompt == "!done":
        break
    full_text += format_text(prompt)
    print(full_text)

