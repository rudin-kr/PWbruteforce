
# Password Generator

This Python program generates passwords based on a given word list. It creates combinations of words with optional prefixes and suffixes, along with the choice of including numbers, characters, and special characters.

## Features

- Load a word list from a file.
- Generate passwords by appending or prepending characters, digits, and/or special characters to each word.
- Save the generated passwords to `passwords.txt`.

## How to Use

- Run the program with the word list file as an argument.
- Optional arguments include `--prefix_length`, `--suffix_length`, and `--combinations` for customizing the passwords.

### Example Command

```bash
python main.py word_list.txt --prefix_length 3 --suffix_length 2 --combinations ncs
```

## Arguments

- `word_list_file`: The file containing the word list.
- `--prefix_length`: Length of the prefix (default is 0).
- `--suffix_length`: Length of the suffix (default is 0).
- `--combinations`: Character combinations to include (n: numbers, c: characters, s: special characters, or any combination thereof).

## Output

- The program outputs a file named `passwords.txt` containing the generated passwords.
