# write your code here
# write your code here
FORMATTER_OPTIONS = ["plain", "bold", "italic", "inline-code",
                     "link", "header", "unordered-list", "ordered-list", "new-line"]
phrase = list()


def header(header):
    while True:
        level = int(input("Level: "))
        if level in range(1, 7):
            break  # correct header [1-6]
        else:
            print("The level should be within the range of 1 to 6")
    while True:
        header = input("Text: ")
        if level == 1:
            phrase.append(f"# {header}\n")
            break
        elif level == 2:
            phrase.append(f"## {header}\n")
            break
        elif level == 3:
            phrase.append(f"### {header}\n")
            break
        elif level == 4:
            phrase.append(f"#### {header}\n")
            break
        elif level == 5:
            phrase.append(f"##### {header}\n")
            break
        else:
            phrase.append(f"######{header}\n")
            break


def list_(phrase, ordered):
    output_list = ""
    while True:
        number_of_rows = input("Number of rows: ")
        number_of_rows = int(number_of_rows)
        if int(number_of_rows) > 0:
            break
        else:
            print("The number of rows should be greater than zero")
    for index in range(1, number_of_rows + 1):
        row = input(f'Row #{index}: ')
        if ordered:
            output_list += f'{index}. {row}\n'
        else:
            output_list += f'* {row}\n'
    phrase.append(output_list)

def done(phrase):
    file = open("output.md", "w")
    for line in phrase:
        file.write(line)
    file.close()

def bold(phrase):
    text = input("Text: ")
    phrase.append(f"**{text}**")


def italic(phrase):
    text = input("Text: ")
    phrase.append(f"*{text}*")


def inline_code(phrase):
    text = input("Text: ")
    phrase.append(f"`{text}`")


def plain(phrase):
    text = input("Text: ")
    phrase.append(text)


def new_line(phrase):
    phrase.append("\n")


def link(phrase):
    label = input("Label: ")
    url = input("URL: ")
    link_ = f"[{label}]({url})"
    phrase.append(link_)


def print_phrase(phrase):
    output_text = ""
    for text in phrase:
        output_text += text
    print(output_text)


def choose_formatter():
    while True:
        formatter = input("Choose a formatter: ")
        if formatter == "!help":
            help_command()  # prints help command
        elif formatter == "!done":
            done(phrase)
            break  # quits the program
        elif formatter not in FORMATTER_OPTIONS:
            print("Unknown formatting type or command")
        elif formatter == 'bold':
            bold(phrase)
        elif formatter == 'italic':
            italic(phrase)
        elif formatter == 'inline-code':
            inline_code(phrase)
        elif formatter == 'plain':
            plain(phrase)
        elif formatter == 'new-line':
            new_line(phrase)
        elif formatter == 'link':
            link(phrase)
        elif formatter == 'header':
            header(phrase)
        elif formatter == 'ordered-list':
            list_(phrase, True)
        elif formatter == 'unordered-list':
            list_(phrase, False)
        if phrase:
            print_phrase(phrase)


def help_command():
    formatter_message = ("Available formatters: plain bold italic header"
                         " link inline-code ordered-list unordered-list "
                         "new-line")
    special_commands_message = "Special commands: !help !done"
    print(formatter_message)
    print(special_commands_message)


formatter = choose_formatter()
