
# 비밀번호 생성기

  이 파이썬 프로그램은 주어진 단어 목록을 기반으로 비밀번호를 생성합니다. 선택적 접두사 및 접미사를 포함한 단어의 조합을 생성하며, 숫자, 문자, 특수 문자의 포함 여부를 선택할 수 있습니다.

## 기능

- 파일로부터 단어 목록을 불러옵니다.
- 각 단어에 문자, 숫자 및/또는 특수 문자를 앞이나 뒤에 추가하여 비밀번호를 생성합니다.
- 생성된 비밀번호를 `passwords.txt` 파일에 저장합니다.

## 사용 방법

- 프로그램을 단어 목록 파일을 인자로 하여 실행합니다.
- 비밀번호를 사용자 정의하기 위한 선택적 인자로 `--prefix_length`, `--suffix_length`, `--combinations`을 사용할 수 있습니다.

### 예시 명령어

```bash
python main.py word_list.txt --prefix_length 3 --suffix_length 2 --combinations ncs
```

## 인자

- `word_list_file`: 단어 목록이 포함된 파일.
- `--prefix_length`: 접두사 길이 (기본값은 0).
- `--suffix_length`: 접미사 길이 (기본값은 0).
- `--combinations`: 포함할 문자 조합 (n: 숫자, c: 문자, s: 특수 문자, 또는 이들의 조합).

## 출력

- 프로그램은 생성된 비밀번호를 포함하는 `passwords.txt` 파일을 출력합니다.
