text = "apple banana apple apple orange banana orange"

#Words = strings
#count
#sentence
#how many times = repeat

count_apple = 0
count_orange = 0
count_banana = 0

for word in text.split():
    if word == "apple":
        count_apple += 1
    elif word == "orange":
        count_orange += 1
    else:
        count_banana += 1

print(f'apple: {count_apple}')
print(f'orange: {count_orange}')
print(f'banana: {count_banana}')