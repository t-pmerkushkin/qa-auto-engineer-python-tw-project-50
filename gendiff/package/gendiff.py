import argparse

def main():
    gendiff = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and shows a difference.',usage='first_file second_file', epilog='set format of output')
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')
    gendiff.add_argument('-f', '--format')
    gendiff.print_help()

if __name__ == '__main__':
    main()