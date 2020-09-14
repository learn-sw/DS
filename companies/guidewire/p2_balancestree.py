    # https://www.onooks.com/a-string-is-considered-balanced-when-every-letter-in-the-string-appears-both-in-uppercase-and-lowercase/#comments    
    # dict_charFreq = {}
    
    # for char in S:
    #     char = char.lower()
    #     if char in dict_charFreq:
    #         dict_charFreq[char] +=1
    #     else:
    #         dict_charFreq[char] = 1
    
    # # this loop will return -1 if the values in the dict_charFreq equals 1
    # for key, value in dict_charFreq.items():
    #     # print(key)
    #     # print(value)
    #     if value == 1:
    #         return -1
            
            
    # dict_uppercase = {}
    # l_index = -1
    # prev_char = ''
    # result = len(S)
    # for r_index in range(len(S)):
    #     if S[r_index].isupper():
    #         dict_uppercase[ S[r_index]] = True
    #         prev_char = S[r_index].lower()
            
    #         if(l_index == -1):
    #             l_index = r_index
        
    #     if S[r_index] in dict_uppercase and prev_char == S[r_index]:
    #         result = min(result, r_index-l_index+1)    
    
    # return result

def balancedString(S):
    upperCaseChars = {}
    charFrequency = {}
    for char in S:
        char = char.lower();
        if char in charFrequency.keys():
            charFrequency[char] = charFrequency[char] + 1
        else:
            charFrequency[char] = 0

    # for value in charFrequency.values():
    #     if value == 1:
    #         return -1


    count = 0
    for value in charFrequency.values():
        if value == 1:
            count += 1

    if count == len(charFrequency.keys()):
        return  -1

    l_index = ""
    result = len(S);
    lastChar = ""

    for index in range(len(S)):
        letter = S[index];

        if letter.upper() == letter:
            upperCaseChars[letter.lower()] = True;
            lastChar = letter.lower()

            if not l_index:
                l_index = index;

        if letter in upperCaseChars and  lastChar == letter:
            result = min(result, index - l_index + 1);

    return result

print("ans is ", balancedString('azABaabza'))