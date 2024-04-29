s = input()
alphabet = [0] * 26

for i in s:
    alphabet[ord(i) - 97] += 1

for t in alphabet:
    print(t, end=" ")
