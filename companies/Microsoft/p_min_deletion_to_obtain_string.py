# https://leetcode.com/discuss/interview-question/786237/Microsoft-or-OA-or-Min-Deletions-To-Obtain-String-in-Right-Format
# Microsoft | OA | Min Deletions To Obtain String in Right Format

s ="BAAABAB"

BA
delete B



def min_deletions(input):

    if not input:
        return

    input = list(input)
    i = input[0]

    count = 0
    p_a, p_b = 0, len(input)-1

    curr = 0

    while curr <=p_b:

        if input[curr] =='A':

            return 
        else:
            # swap
            count +=1
            input[p_a], input[p_b] = input[p_b],input[p_a]
            p_b -=1

# ABBB

# BBB