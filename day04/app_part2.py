import re

def checkpassport():
    valid = 0
    required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    with open('input.txt') as f:
        input1 = f.read()
    blank_line_regex = r"(?:\r?\n){2,}"
    all_pass = []
    all_pass = re.split(blank_line_regex, input1.strip())
    for passport in all_pass:
        passport = passport.replace('\n', ' ')
        passport = passport.split(' ')
        # reset all field checks
        count_fields = 0
        byr_ok = 0
        iyr_ok = 0
        eyr_ok = 0
        hgt_ok = 0
        hcl_ok = 0
        ecl_ok = 0
        pid_ok = 0
        for field in required_fields:
            if any(field in s for s in passport): # check for all required fields
                count_fields += 1
        for field in passport:
            field = field.split(':')
            if field[0] == 'byr' and 1920 <= int(field[1]) <= 2002:
                byr_ok = 1
            if field[0] == 'iyr' and 2010 <= int(field[1]) <= 2020:
                iyr_ok = 1
            if field[0] == 'eyr' and 2020 <= int(field[1]) <= 2030:
                eyr_ok = 1
            if field[0] == 'hgt':
                if 'cm' in field[1]:
                    field[1] = field[1].replace('cm', '')
                    if 150 <= int(field[1]) <= 193:
                        hgt_ok = 1
                if 'in' in field[1]:
                    field[1] = field[1].replace('in', '')
                    if 59 <= int(field[1]) <= 76:
                        hgt_ok = 1
            if field[0] == 'hcl':
                if len(field[1]) == 7:
                    char = []
                    char[:] = field[1]
                    if char[0] == '#':
                        for index in range(1, len(field[1])):
                            i = char[index]
                            if i.isalpha() or i.isdigit():
                                hcl_ok = 1
            if field[0] == 'ecl':
                if any(field[1] in s for s in valid_eye_colors):
                    ecl_ok = 1
            if field[0] == 'pid':
                if len(field[1]) == 9 and field[1].isdigit():
                    pid_ok = 1

        # check all rules to check if it's valid
        if count_fields == 7 and byr_ok == 1 and iyr_ok == 1 and eyr_ok == 1\
            and hgt_ok == 1 and hcl_ok == 1 and ecl_ok == 1 and pid_ok == 1:
            valid += 1

    print('Valid passports:', valid)

checkpassport()
