def vowel(str):
    count = 0
    vowel = "aeiouAEIOU"

    for alphabet in str:
        if alphabet in vowel:
           count = count +1

    return count

print(vowel("kashish"))