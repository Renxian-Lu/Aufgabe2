import sys

try:

    file_name = sys.argv[1]
    # print(file_name)

    with open(file_name) as file_obj:

        fileContent = file_obj.read()
        print(fileContent)
except FileNotFoundError:
    print('File does not exists: '+file_name)
    sys.exit(-1)