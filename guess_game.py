import random
#Random Number is Generated
def random_generator(max_number):
	number = random.randint(0,max_number)
	return number
#Give user chance to guess the number
def guess_number():
	max_number = int(input("Up to how many numbers can you guess?! :"))
	guess = random_generator(max_number)
	print("Please guess the number within 5 tries")
	tries = 0
	c = 0
	for x in range(1,6):
		print("Your {} guess".format(x))
		c = x
		y = int(input())
		if y==guess:
			tries = 1
			break
		else:
			print("Try Again")
	if tries == 1:
		print("You Won!!")
		print("The number of tries taken: {}".format(x))
	else:
		print("Better Luck Next Time =(")

if __name__ == "__main__":
	guess_number()

