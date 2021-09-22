import re

def checkpassport():
    valid = 0
    required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    with open('input.txt') as f:
        input1 = f.read()
    blank_line_regex = r"(?:\r?\n){2,}"
    all_pass = []
    all_pass = re.split(blank_line_regex, input1.strip())
    for passport in all_pass:
        passport = passport.replace('\n', ' ')
        passport = passport.split(' ')
        count_fields = 0
        for field in required_fields:
            if any(field in s for s in passport):
                count_fields += 1
        if count_fields == 7:
            valid += 1
    print('Valid passports:', valid)

checkpassport()
