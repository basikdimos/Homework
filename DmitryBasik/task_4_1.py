# Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.

def replace_sym(in_str):
	""" replaces all `"` or `'` symbols on `'` or `"` """
	out_str = ''
	for i in in_str:
		if i == '"':
			out_str += "'"
		elif i == "'":
			out_str += '"'
		else:
			out_str += i
	return out_str

some_str = '"Hi Amy! Your mum sent me a \'text\'. You forgot your inhaler. Why don’t you turn your phone on?" Amy didn’t like technology'
print(f'{some_str}')
print(f'{replace_sym(some_str)}')
