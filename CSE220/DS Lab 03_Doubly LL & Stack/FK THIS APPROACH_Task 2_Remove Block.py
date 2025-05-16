from Stack_Implement import *
def remove_block(stack, n):
    temp = Stack()
    count = 1
    flag = True
    while True:
        if count == n and flag:
            flag = False
            stack.pop()
            # print_stack(stack)
        elif not flag and count == n:
            if temp.isEmpty:
                break
            else:
                stack.push(temp.pop())
                # print_stack(stack)
                # print_stack(temp)
        else:
            count += 1
            temp.push(stack.pop())
            # print_stack(temp)


print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,3)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()