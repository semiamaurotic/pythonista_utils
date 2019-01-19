#Comment/Uncomment selected lines

import editor

def get_comment_level(text):
	# get the minimum indentation of the lines to be commented
	levels = [len(line[:len(line) - len(line.lstrip())]) 
		for line in text.splitlines(keepends=True) 
		if line.lstrip()]
	comment_level = min(levels)
	return comment_level


text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]

# by checking "is_comment" at the first line, the entire block is commented or
# uncommented together
is_comment = selected_text.lstrip().startswith('# ')
replacement = ''
comment_level = get_comment_level(selected_text)
for line in selected_text.splitlines(keepends=True):
	whitespace = line[:comment_level]
	if is_comment:
		if line.lstrip().startswith('# '):
			# replace only the first hash symbol so comments at deeper indent levels remain in place.
			replacement += line.replace('# ', '', 1)
		else:
			replacement += line
	else:
		replacement += whitespace + '# ' + line[comment_level:]
		
editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement))
