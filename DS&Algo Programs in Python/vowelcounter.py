def countVowels(S):
    t= len(S)
    v= 0
    for char in S:
        if char in 'aeiouAEIOU':
            v=v+1
    c=t-v
    if v>c:
        print('There are more vowels than consonants in the string ' + S)
    elif v==c:
        print('Both vowels and consonants are equal in the string ' + S)
    else:
        print('There are more consonants than vowels in the string ' + S)
countVowels('hello')
countVowels('hi')
countVowels('aeiocc')
