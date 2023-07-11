import sys

def main():
    # 파일 경로를 명령줄 인수로 받음
    file_path = sys.argv[1]
    
    # 파일 열기
    with open(file_path, 'r') as file:
        # 파일 내용 출력
        print(file.read())

if __name__ == '__main__':
    main()
