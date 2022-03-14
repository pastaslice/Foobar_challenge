# Input:
# solution.solution("abcabcabcabc")
# Output:
#     4





def solutions(s) : # this version passed tests
    str = s
    divider = 0
    seq_len = 0
    true_seq1 = 0
    slicer = 0
    outp = 0
    while divider < len(str) :
        divider = divider + 1
        print(divider, '-divider', len(str), '-len(str)')
        if len(str) % divider == 0:
           seq_len = int(len(str) / divider)
           print(seq_len,'-seq_len')
        else:
            print('conitnue')
            continue
        while int((seq_len * 2) + slicer) < len(str) + 1 :
            print(slicer,'-slicer')
            if str[slicer:int(seq_len + slicer)] != str[int(seq_len + slicer):int((seq_len * 2) + slicer)] :
                outp = 1
                print('break')
                break
            slicer = slicer + 1
        slicer = 0
        if outp == 0 :
            true_seq1 = str[:seq_len]
            print(str[:seq_len], 'str[:seq_len]')
        else :
            outp = 0
    print(true_seq1,'-true_seq1')
    result = int(len(str) / len(true_seq1))
    return  result

print(solutions('aaabba'))

# first way to approach problem but it didnt work properly :/
def solution(s) :
    str = s
    seq1 = ''
    rank = -1
    true_se = ''
    for y in str :
        rank = rank + 1
        if seq1 == '' :
            seq1 = y
        elif y != seq1[0] :
            seq1 = seq1 + y
        elif y == seq1[0] :
            if seq1 == str[rank:rank * 2] :
                print(y, rank, seq1, '-seq1', true_se, '-true_se')
                if true_se == '':
                    true_se = seq1
                if len(seq1) % 2 == 0 :
                    if seq1[:int(len(seq1)/2)] != seq1[int(len(seq1)/2):] :
                        if true_se[len(true_se)-1] != seq1[len(seq1)-1] :
                            true_se = seq1
                else :
                    if true_se == '' :
                        true_se = seq1
                    elif true_se not in seq1 :
                        true_se = seq1
                    elif true_se in seq1 :
                        if true_se[len(true_se)-1] != seq1[len(seq1)-1] :
                            true_se = seq1
                        else :
                            if len(true_se) == 1 :
                                for x in seq1 :
                                    if true_se != x :
                                        true_se = seq1
                seq1 = seq1 + y
            else :
                seq1 = seq1 + y
    result = int(len(str) / len(true_se))
    print(true_se)
    return result

print(solution("abab"))

