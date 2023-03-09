from os import environ

def main():
    TEST = environ['REFRESH_TOKENS']
    for i in TEST:
        print(i)

if __name__ == "__main__":
    main()
