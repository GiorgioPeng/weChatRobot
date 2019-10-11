from wxpy import *
if __name__ == '__main__':
	b = Bot(cache_path=True)
	for i in range(len(b.user_details(b.friends()))):
		print(b.user_details(b.friends())[i])