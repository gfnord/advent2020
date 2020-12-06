import re

def check_answers():
    input = open('input.txt', 'r').read()
    blank_line_regex = r"(?:\r?\n){2,}"
    answer_count = 0
    persons_per_group = 0
    all_groups = []
    all_groups = re.split(blank_line_regex, input.strip())
    for answers in all_groups:
        per_answer = answers.splitlines()
        persons_per_group = len(per_answer)
        #print(per_answer)
        if persons_per_group == 1:
            per_answer_lst = list(per_answer[0])
            answer_count += len(per_answer_lst)
            #print('- ', len(per_answer_lst), per_answer_lst)
        if persons_per_group == 2:
            person1 = list(per_answer[0])
            person2 = list(per_answer[1])
            answer_count += len(set(person1).intersection(person2))
            #print('- ', len(set(person1).intersection(person2)), set(person1).intersection(person2))
        if persons_per_group == 3:
            person1 = list(per_answer[0])
            person2 = list(per_answer[1])
            person3 = list(per_answer[2])
            answer_count += len(set(person1).intersection(person2, person3))
            #print('- ', len(set(person1).intersection(person2, person3)), set(person1).intersection(person2, person3))
        if persons_per_group == 4:
            person1 = list(per_answer[0])
            person2 = list(per_answer[1])
            person3 = list(per_answer[2])
            person4 = list(per_answer[3])
            answer_count += len(set(person1).intersection(person2, person3, person4))
            #print('- ', len(set(person1).intersection(person2, person3, person4)), set(person1).intersection(person2, person3, person4))
        if persons_per_group == 5:
            person1 = list(per_answer[0])
            person2 = list(per_answer[1])
            person3 = list(per_answer[2])
            person4 = list(per_answer[3])
            person5 = list(per_answer[4])
            answer_count += len(set(person1).intersection(person2, person3, person4, person5))
            #print('- ', len(set(person1).intersection(person2, person3, person4, person5)), set(person1).intersection(person2, person3, person4, person5))
    print('Answers count:', answer_count)
            
check_answers()
