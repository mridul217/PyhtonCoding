# s = "kedisdeetexyuuuu"
s = "aeiou"

k=2
c_vowel = 0
max_vowel = 0
vowel = {'a', 'e','i', 'o', 'u'}

for i in range(k):
    if s[i] in vowel:
        c_vowel += 1

max_vowel = c_vowel

for i in range (k, len(s)):
    if s[i-k] in vowel:
        c_vowel -= 1
    if s[i] in vowel:
        c_vowel +=1

    max_vowel = max(max_vowel, c_vowel)

print(max_vowel)