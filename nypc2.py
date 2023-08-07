import sys
input = sys.stdin.readline

# num_lines, max_column = map(int, input().split())

# l = []

# for i in range(0, n) :
#     a = a.replace(' ', '-')
#     l.append(a)
    
# dic =   {
#             '<CENtER>' : 'C', 
#             '<RIGHT>' : 'R',
#             '</CENTER>' : 'L',
#             '</RIGHT>' : 'L'
#         }   
# for i in range(0, n) :
#     tag = dic[l[i]]

#     if l[i] != '<CENTER>' and l[i] != '<RIGHT>' and l[i] != '</CENTER>' and l[i] != '</RIGHT>' :
#         if tag == 'C' :
#             s = ('-'*((m-len(l[i]))//2))+l[i]+('-'*(((m-len(l[i]))//2)+1))
#         elif tag == 'R' :
#             s = l[i]+('-'*(m-len(l[i])))
#         elif tag == 'L' :
#             s = ('-'*(m-len(l[i])))+l[i]
#         if len(s) > m :
#             ss = s.split('-')
            
#         print(s)


num_lines, max_column = map(int, input().split())

lines = []

for i in range(num_lines) :
    lines.append(input().split())

align = 'left'

output = ''

dic =   {
            '<CENTER>' : 'C', 
            '<RIGHT>' : 'R',
            '</CENTER>' : 'L',
            '</RIGHT>' : 'L'
        }   

def get_align(line):
    if line[0] == '<CENTER>':
        return 'center'
    elif line[0] == '<RIGHT>':
        return 'right'
    elif line[0] == '</CENTER>':
        return 'left'
    elif line[0] == '</RIGHT>':
        return 'left'
    
    return None

def align_print(text):
    text = text.replace(' ', '-')
    padding = max_column - len(text)
    if align == 'left':
        text = text + '-' * padding
    elif align == 'right':
        text = '-' * padding + text
    else:
        half_padding = padding // 2
        remain_padding = padding % 2
        text = '-' * half_padding + text + '-' * (half_padding + remain_padding)

    print(text)

for line in lines:
    if len(output) > 0:
        align_print(output)
        output = ''

    # if line[0] == '</RIGHT>':
    #     print('bingo')

    check_align = get_align(line)
    if check_align != None:
        align = check_align
        continue

    for word in line:
        test_line = ''
        if len(output) == 0:
            test_line = word
        else:
            test_line = output + ' ' + word
        
        if len(test_line) > max_column:
            align_print(output)
            output = word
        else:
            output = test_line

if len(output) > 0:
    align_print(output)




 