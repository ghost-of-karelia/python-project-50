import argparse

def run_parser():

    parser = argparse.ArgumentParser(
        prog='gendiff', usage='%(prog)s [-h] first_file second_file',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', nargs='+', help='')
    parser.add_argument('second_file', nargs='+', help='')

    parser.print_help()


parser = argparse.ArgumentParser(
    prog='gendiff', usage='%(prog)s [-h] first_file second_file',
    description='Compares two configuration files and shows a difference.'
)

parser.add_argument('first_file', nargs='+', help='')
parser.add_argument('second_file', nargs='+', help='')

args = parser.parse_args()
print(args.accumulate(args.integers))



def main():
    print('')
    #run_parser() TODO delete the function run_parser if works without it
    print('')
    print("Hello, %username%!\nBe assured, the Gendiff script is running!")


if __name__ == '__main__':
    main()