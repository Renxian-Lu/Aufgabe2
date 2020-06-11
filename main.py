import sys

try:

    file_name = sys.argv[1]
    # print(file_name)

    with open(file_name, 'r') as file_obj:

        lines = file_obj.readlines()[1:]  # skip the first line
        list1 = []
        for line in lines:
            list1.append(line)

        for i in list1:
            i.strip()

except FileNotFoundError:
    print('File does not exists: '+file_name)
    sys.exit(-1)