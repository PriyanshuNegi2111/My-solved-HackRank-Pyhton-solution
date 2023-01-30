def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        a = i
        for j in range(0, len(sub_string)):
            if string[a] == sub_string[j]:
                a +=1
                if j == len(sub_string)-1:
                    count = count + 1
                else:
                    continue
            else:
                break
    return count
