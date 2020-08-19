# Minimum number of deletions and insertions to transform one string into another
# Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
# Input : str1 = "heap", str2 = "pea" 
# Output : Minimum Deletion = 2 and
#          Minimum Insertion = 1
# p and h deleted from heap
# Then, p is inserted at the beginning
# One thing to note, though p was required yet
# it was removed/deleted first from its position and
# then it is inserted to some other position.
# Thus, p contributes one to the deletion_count
# and one to the insertion_count.

# Input : str1 = "geeksforgeeks", str2 = "geeks"
# Output : Minimum Deletion = 8
#          Minimum Insertion = 0


# https://www.geeksforgeeks.org/minimum-number-deletions-insertions-transform-one-string-another/


def dp_longest_common_substring(x,y, n, m):
    r,c = n+1, m+1

    dp_arr = [[ -1 for x in range(c)] for x in range(r)]
    result = 0
    for i in range(r):
        for j in range(c):

            if i == 0 or j ==0:
                dp_arr[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
                result = max(result, dp_arr[i][j]) 
            else:
                dp_arr[i][j] = 0

    # print(dp_arr)
    return result

def dp_p4_min_noof_del_insertion_to_transform_one_str_into_another(x,y, n, m):
    
    num_of_deletes, num_of_insertions = 0, 0

    dp_len = dp_longest_common_substring(s1, s2, len(s1), len(s2))
    num_of_deletes = len(s1) - dp_len
    num_of_insertions = len(s2) - dp_len
    return (num_of_deletes, num_of_insertions)

s1 = "heap"
s2 = "pea"
print(dp_p4_min_noof_del_insertion_to_transform_one_str_into_another(s1, s2, len(s1), len(s2)))

s1 = "geeksforgeeks"
s2 = "geeks"

print(dp_p4_min_noof_del_insertion_to_transform_one_str_into_another(s1, s2, len(s1), len(s2)))



