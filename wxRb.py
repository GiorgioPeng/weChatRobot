from wxpy import *
if __name__ == '__main__':
    b = Bot(cache_path=True)
    for i in b.friends():
        print(i)
