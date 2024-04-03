import argparse
import json


def run_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='see format of output')
    # args = parser.parse_args() # So linter does not argue.
    parser.parse_args()


def generate_diff(file1, file2):

    # Calculate difference
    diff = {}
    for key in sorted(file1.keys())+sorted(file2.keys()):
        if key not in file2:
            diff[f'- {key}'] = file1[key]
        elif key not in file1:
            diff[f'+ {key}'] = file2[key]
        else:
            if file1[key] != file2[key]:
                diff[f'- {key}'] = file1[key]
                diff[f'+ {key}'] = file2[key]
            else:
                diff[key] = file1[key]

    # Print the {diff} in a readable format in the console
    printable_result = []
    for key, value in diff.items():
        printable_result.append(f"{key}: {value}")
    for i in printable_result:
        print(i)

    # Return result
    return diff


def main():
    print('')
    print("Hello, %username%! Be assured, the Gendiff script is running!")
    # file1 = json.load(open('file1.json'))
    # file2 = json.load(open('file2.json'))
    # generate_diff(file1, file2)
    run_parser()


if __name__ == '__main__':
    main()
