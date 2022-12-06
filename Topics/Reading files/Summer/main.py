#  write your code here 

my_file = open("./data/dataset/input.txt",  "r")
amount_of_summers = 0
for line in my_file:
    if "summer\n" in line:
        amount_of_summers += 1
print(amount_of_summers)
