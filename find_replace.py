# Regex search and replace

import editor
import console
import re


text = editor.get_text()
selection = editor.get_selection()

search = console.input_alert('Find', 'Enter RegEx search string.')
replace = console.input_alert('Replace', 'Enter RegEx replacement string.')

# if no text is selected, get all text
if selection[0] == selection[1]:
    selection = (0, len(text))
    selected_text = text
else:
    selected_text = text[selection[0]:selection[1]]

replacement_text, replacements_made = re.subn(search, replace, selected_text)

editor.replace_text(selection[0], selection[1], replacement_text)
editor.set_selection(selection[0], selection[0] + len(replacement_text) - 1)
console.hud_alert('{} replacements were made.'.format(replacements_made))

