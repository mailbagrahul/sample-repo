import pandas as pd
import re


found_case = ""
found_end = ""
sameline_case = ""
case_count = 0
total_case_Stat = 0


def write_text(joined_str):

    outfile.write(joined_str)


def process_line(line):
    # if 'save the world' in line.lower():
    #      superman.save_the_world()
    global found_case, found_end, sameline_case, case_count, total_case_Stat

    if 'case' in line.lower():
        total_case_Stat += 1
        if found_case == "Y":
            case_count = case_count + 1
        else:
            case_count = 1

        words = line.split()
        # print(words)
        for word in words:
            if 'case' in word.lower():
                case_index = words.index(word)
                found_case = 'Y'
            else:
                if 'end' in word.lower():
                    end_index = words.index(word)
                    found_end = 'Y'
                    if found_case == "Y":  # if case found case in same line - set sameline_case to Y
                        sameline_case = "Y"

        if sameline_case == "Y":
            case_string = " ".join(words[case_index: end_index + 5])
            # reset to default
            sameline_case = ""
            found_case = ""
            found_end = ""
        else:
            case_string = " ".join(words[case_index:])

        write_text(case_string)
        write_text("\n")

    elif found_case == "Y":  # found CASE in previous lines
        if 'end' in line.lower():
            case_count = case_count - 1
            write_text(line)
            write_text("\n")

            if case_count == 0:
                found_case = "N"

        else:
            # write until it finds END
            write_text(line)
            write_text("\n")


with open(r'C:\Users\N0207022\Desktop\NGRT\Tharani_eg.txt') as f:
    outfile = open(r'C:\Users\N0207022\Desktop\NGRT\Tharani_out.txt', 'w')
    for line in f:
        if line.strip().startswith('--'):
            pass
        else:
            process_line(line)
    else:
        print("Total case Statements found:{}".format(total_case_Stat))
        outfile.close()
