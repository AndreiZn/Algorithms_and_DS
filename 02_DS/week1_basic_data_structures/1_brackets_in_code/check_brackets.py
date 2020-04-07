# python3

from collections import namedtuple
import os
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = [0]*len(text)
    stack_num_elements = 0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            next_bracket = Bracket(next, i+1)
            #print(len(opening_brackets_stack))
            opening_brackets_stack[stack_num_elements] = next_bracket
            stack_num_elements += 1
        if next in ")]}":
            # Process closing bracket, write your code here
            if stack_num_elements > 0:
                stack_pop = opening_brackets_stack[stack_num_elements-1]
                if not are_matching(stack_pop.char,  next):
                    return i + 1
                else:
                    stack_num_elements -= 1
            else:
                return i + 1

    if stack_num_elements == 0:
        return "Success"
    else:
        return opening_brackets_stack[stack_num_elements-1].position

def main(from_file=False):
    if from_file:
        test_files = sorted(os.listdir(test_dir))
        print(test_files)
        for file_id in range(0,len(test_files),2):
            test_filename = test_dir + test_files[file_id]
            #print(test_filename)
            f = open(test_filename, "r")
            text = f.read()

            #print(text)

            correct_ans_filename = test_dir + test_files[file_id+1]
            f = open(correct_ans_filename, "r")
            correct_ans = f.read()

            #print(correct_ans)

            mismatch = find_mismatch(text)
            if mismatch == correct_ans:
                print('True')
            else:
                print(text)
                print(correct_ans)
                print(mismatch)
    else:
        text = input()
        mismatch = find_mismatch(text)
        # Printing answer, write your code here
        print(mismatch)

if __name__ == "__main__":
    #test_dir = '/Users/andreizn/Desktop/Algorithms_and_DS/02_DS/week1_basic_data_structures/1_brackets_in_code/tests/'
    main()
