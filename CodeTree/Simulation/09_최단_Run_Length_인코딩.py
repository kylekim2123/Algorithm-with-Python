word = input()
cases = set(word[-i:] + word[:-i] for i in range(len(word)))
min_length = 999999999

for case in cases:
    encoded_word = ""
    base = case[0]
    counts = 1

    for i in range(1, len(case)):
        if base == case[i]:
            counts += 1
            continue

        encoded_word += base + str(counts)
        base = case[i]
        counts = 1

    encoded_word += base + str(counts)
    min_length = min(min_length, len(encoded_word))

print(min_length)
