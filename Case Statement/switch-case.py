def switch_case(lines):
    last_code = []
    switch_index = None
    for i in range (len(lines)):
        each_line = lines[i]
        br=0
        if 'switch' in each_line:
            switch_index = i
            curr_index = i
            sw_start = switch_index
            no_of_cases = switch_index
            cnt=0
            for j in lines:
                if 'case' in j:
                    cnt+=1
            # print(cnt)
            start_index = each_line.index('(')  # stores the index of '(' as start_index 
            end_index = each_line.index(')')  # stores the index of ')' as end_index
            input_switch = ''.join(each_line[start_index+1:end_index]) 
            # print(input_switch)
            for j in range(cnt):
                no_of_cases+=1
                temp='avi'
                last_code.append('if {} ={} goto({})'.format(input_switch,None,temp))  
            curr_index=cnt
            # print(last_code)
        elif 'case' in each_line:
            no_of_stat = 0
            case_index=i

            for j in range(case_index,lines.index('break')):
                no_of_stat+=1
            # print(no_of_stat) 
            start_index = 4   
            end_index = each_line.index(':')  
            cases=[]
            cases.append(each_line[start_index:end_index])
            
            last_code[sw_start] = last_code[sw_start].replace('None',str(cases[0]))
            last_code[sw_start] = last_code[sw_start].replace('avi',str(curr_index+2))
            sw_start+=1
            curr_index+=no_of_stat
            # print(last_code)
       
        elif 'break' in each_line:
            break_index=i
            tmp ='END'
            last_code.append('goto({})'.format(tmp))
            # last_code[sw_start] = last_code[sw_start].replace('None',str())
        elif '}' in each_line:
            continue
        else:
            last_code.append(each_line)
    return last_code

with open('switch.txt') as f:
    code = f.readlines()
    # print(code)
print('The Statement is:')
print(''.join(code))

removed_newline = [] # storing the values after removing the newline below
for i in range(len(code)):
    if code[i] != '\n': # Neglecting the "\n" i.e. totally empty line
        if code[i][-1] == '\n': # check if last element is newline 
            # don't include the \n at the end of each line
            removed_newline.append(code[i][:-1].strip()) # last element is '\n' then append the string till second last element
            # print(removed_newline) # strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
        else:
            removed_newline.append(code[i].strip()) # last element is not '\n' then append the whole string

removed_newline.remove('{')
# for i in removed_newline:

add3_code = switch_case(removed_newline)
add3_code.append('END')

# print(add3_code)
index=1
for i in add3_code:
    print(index ,i)
    index+=1
