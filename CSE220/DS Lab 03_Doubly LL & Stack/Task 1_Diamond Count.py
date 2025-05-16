from Stack_Implement import *
import fhm_unittest as unittest


def diamond_count(stack, string):
    count = 0
    for i in range(len(string)):
        if string[i] == "<":
            stack.push("<")
        elif string[i] == ">" and stack.peek() == "<":
            stack.pop()
            count += 1
    return count


print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack, string)
print(f'Number of Diamonds: {returned_value}')  # This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack, string)
print(f'Number of Diamonds: {returned_value}')  # This should print 1
unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack, string)
print(f'Number of Diamonds: {returned_value}')  # This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')
