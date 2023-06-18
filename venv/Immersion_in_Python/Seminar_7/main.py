from Task_1S import feel_numbers
from Task_2S import gen_name
from Task_3S import gen_new_file
from Task_4S import gen_file
from Task_5S import gen_file_2
from Task_1HW import group_rename

if __name__ == '__main__':
    feel_numbers(5, 'Task_1.txt')
    gen_name(5, 'Task_2.txt')
    gen_new_file('Task_1.txt', 'Task_2.txt', 'Task_3.txt')
    gen_file('bin', 5, 10, 256, 1024, 2)
    gen_file_2(['txt', 'byte'], [2, 2])
    group_rename(3, 'bin', 'txt', [2, 3], "file_new")
