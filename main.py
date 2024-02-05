import argparse

from Classes.PasswordGenerator import PasswordGenerator


def main():
    # How to Use
    # python main.py word_list.txt --prefix_length 3 --suffix_length 2 --combinations ncs

    parser = argparse.ArgumentParser(description='Generate passwords from a word list.')
    parser.add_argument('word_list_file', help='The file containing the word list.')
    parser.add_argument('--prefix_length', type=int, default=0, help='The length of the prefix to add to each word.')
    parser.add_argument('--suffix_length', type=int, default=0, help='The length of the suffix to add to each word.')
    parser.add_argument('--combinations', choices=['n', 'c', 's', 'nc', 'ns', 'cs', 'ncs'], default='n',
                        help='Character combinations: n (numbers), c (characters), s (special characters).')
    return parser.parse_args()


if __name__ == '__main__':
    args = main()
    generator = PasswordGenerator(args.word_list_file, args.combinations, args.prefix_length, args.suffix_length)
    generator.create_pw_file()
