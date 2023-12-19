ter_cases = {'0': ('1', '2'), '1': ('0', '2'), '2': ('0', '1')}

def is_same(bi_num, ter):
    for j in range(len(ter)):
        for case in ter_cases[ter[j]]:
            if not j and case == '0':
                continue
            changed = ter[:j] + case + ter[j+1:]
            if bi_num == int(changed, 3):
                return True
    return False

def check_all_case(bi, ter):
    for i in range(1, len(bi)):
        case = '1' if bi[i] == '0' else '0'
        changed = bi[:i] + case + bi[i+1:]
        bi_num = int(changed, 2)
        if is_same(bi_num, ter):
            return bi_num

for t in range(1, int(input())+1):
    print('#%s %s' % (t, check_all_case(input(), input())))