# a demo to count the common words
def count_common_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"Sorry, {filename} is not found")
    else:
        text_string = ''

        for content in contents:
            text_string += content.strip()

        print(f"{filename} have {len(text_string)} words")
        print(f"\nThe word for 'the' in {filename} is {contents.lower().count('the ')}")
        print(f"\nThe word for 'there' in {filename} is {contents.lower().count('there ')}")
        print(f"\nThe word for 'rule' in {filename} is {contents.lower().count('rule ')}")

filename = '/Users/nerve2009/Desktop/python_projects/python_crash_course/diy_app/words_count_automated/wings_and_stings.txt'
count_common_words(filename)