from sys import argv
script, input_encoding, error = argv

def main(language_file_object, encoding, errors):
    content = language_file_object.readline()

    if content:
        print_line(content, encoding, errors)
        return main(language_file_object, encoding, errors)

def print_line(content, encoding, errors):
    next_lang = content.strip()
    raw_bytes = next_lang.encode(encoding, errors)
    cooked_string = raw_bytes.decode(encoding, errors)

    print(raw_bytes, "<====>", cooked_string)


languages = open("testdata\\languages.txt", encoding="utf-8")

main(languages, input_encoding, error)