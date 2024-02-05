import copy
import os
import re
import string


class PasswordGenerator:
    def __init__(self, file_path, mode, prefix_len=0, suffix_len=0):
        self.word_list = []
        self.pw_list = []

        # 단어 목록을 불러옵니다.
        with open(file_path, 'r') as f:
            self.word_list = f.read().splitlines()

        #  추가할 문자 set 설정합니다.
        self.word_count = len(self.word_list)
        punctuation = "!@#$%_-~"
        match mode:     # 추가할 문자 set 모드(숫자, 영문자, 특수문자)
            case 'n':
                self.char_set = string.digits
            case 'c':
                self.char_set = string.ascii_letters
            case 's':
                # self.char_set = string.punctuation
                self.char_set = punctuation
            case 'nc':
                self.char_set = string.digits + string.ascii_letters
            case 'ns':
                # self.char_set = string.digits + string.punctuation
                self.char_set = string.digits + punctuation
            case 'cs':
                # self.char_set = string.ascii_letters + string.punctuation
                self.char_set = string.ascii_letters + punctuation
            case 'ncs':
                # self.char_set = string.digits + string.ascii_letters + string.punctuation
                self.char_set = string.digits + string.ascii_letters + punctuation
            case _:
                raise ValueError(f"Invalid mode: {mode}")

        self.prefix_len = prefix_len  # 앞에 추가할 문자 길이
        self.suffix_len = suffix_len  # 뒤에 추가할 문자 길이

        print("------------------------------")
        print("설정 정보: ")
        print(f"- 단어 목록: {file_path} (단어 수: {self.word_count})")
        self.word_count = self.word_count * 2  # 단어 수 * 2 (알파벳 첫 글자 대문자 치환)
        print(f"- 앞에 추가할 문자 길이: {self.prefix_len}")
        print(f"- 뒤에 추가할 문자 길이: {self.suffix_len}")
        print(f"- 추가할 문자 set(mode {mode}): {self.char_set}")
        print("------------------------------")

    def gen_password_list(self, word):
        password_list = [word]

        # 앞에 추가할 문자 길이만큼 반복합니다.
        temp_list = [word]
        for _ in range(self.prefix_len):
            created_list = []
            for w in temp_list:
                for c in self.char_set:
                    created_list.append(c + w)
            password_list.extend(created_list)
            temp_list = created_list

        # 뒤에 추가할 문자 길이만큼 반복합니다.
        temp_list = copy.deepcopy(password_list)
        for _ in range(self.suffix_len):
            created_list = []
            for w in temp_list:
                for c in self.char_set:
                    created_list.append(w + c)
            password_list.extend(created_list)
            temp_list = created_list

        return password_list

    def create_pw_file(self):
        # 패스워드를 생성합니다.
        for i, word in enumerate(self.word_list):
            print(f"{word}에 대한 패스워드 생성 중....{i*2+1}/{self.word_count}")
            # 앞/뒤에 문자를 추가합니다.
            self.pw_list.extend(self.gen_password_list(word))

            # 첫 번째 알파벳을 대문자로 변경합니다.
            caped_word = self.capitalize_first_letter(word)
            if caped_word:
                print(f"{caped_word}에 대한 패스워드 생성 중....{i*2+2}/{self.word_count}")
                self.pw_list.extend(self.gen_password_list(caped_word))

        # 파일 저장
        with open('passwords.txt', 'w') as f:
            for pw in self.pw_list:
                f.write(pw + '\n')

        print("------------------------------")
        print("파일 저장 완료!")
        print(f"생성된 패스워드 수: {len(self.pw_list):,}")
        print(f"패스워드 파일 크기: {os.path.getsize('passwords.txt') / 1048576:.2f} MB")
        print(f"초당 시도 시 예상 시간: {len(self.pw_list)/86400:.2f} 일")
        print("------------------------------")

    def capitalize_first_letter(self, word):
        """
        첫 번째 알파벳 찾아 대문자로 변경합니다.
        만약, 숫자나 특수문자라면 변경하지 않습니다.

        :param word:
        :return:
        """
        match = re.search(r'[a-zA-Z]', word)

        if match:
            return word[:match.start()] + match.group().upper() + word[match.end():]
        else:
            return None
