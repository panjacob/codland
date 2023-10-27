vowels_letters = ['a', 'i', 'e', 'o', 'u']

num_lines = int(input("How many lines will there be? "))

poem = []
for i in range(num_lines):
    line = input("Enter line {} of the poem: ".format(i + 1))
    poem.append(line.lower())

vowels_count = 0
consonants_count = 0
for line in poem:
    for letter in line:
        if not letter.isalnum():
            continue

        if letter in vowels_letters:
            vowels_count += 1
        else:
            consonants_count += 1

print("Number of vowels: {}".format(vowels_count))
print("Number of consonants: {}".format(consonants_count))
