import re

def check_answers():
    with open('input.txt') as f:
        input1 = f.read()
    blank_line_regex = r"(?:\r?\n){2,}"
    answer_count = 0
    all_groups = []
    all_groups = re.split(blank_line_regex, input1.strip())
    for answers in all_groups:
        answers = answers.replace('\n', '') # remove new lines
        answers = list(answers) # create a list
        #convert the list to dict to remove duplicates and convert back to list
        answers_clean = list(dict.fromkeys(answers))
        answer_count += len(answers_clean)
    print('Answers count:', answer_count)

check_answers()
