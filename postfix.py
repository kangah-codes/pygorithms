# author = "Joshua Akangah"
# evaluate postfix in python


def postfix_eval(expression):
	stack = []

	for i in expression:
		try:
			current = int(i)
			stack.append(current)
		except ValueError:
			if i == '+':
				first = stack.pop()
				second = stack.pop()
				stack.append(first+second)
			elif i == '-':
				first = stack.pop()
				second = stack.pop()
				stack.append(second-first)
			elif i == '*':
				first = stack.pop()
				second = stack.pop()
				stack.append(first*second)
			elif i == '/':
				first = stack.pop()
				second = stack.pop()
				stack.append(second/first)

	return stack[0]

exp = input("Enter your expression: ")

print(postfix_eval(exp))