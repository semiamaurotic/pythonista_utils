# coding: utf-8

import appex
from html2text import html2text
import console
import re
import clipboard


def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    text = appex.get_text()
    if not text:
        print('No text input found.')
        return

    selection = console.alert('Transform Text',
                              'Select Transformation',
                              'Title Case',
                              'lower case',
                              'Sentance case',
                              hide_cancel_button=True)
    if selection == 1:
        text = text.title()
    elif selection == 2:
        text = text.lower()
    elif selection == 3:
        sentences = [x.capitalize() for x in re.split(r'([\.?!] |\n)', text)]
        print(sentences)
        text = ''.join(sentences)
    elif selection == 4:
        # console.alert() only supports 3 buttons,
        # so this option is superfluous for now.
        text = text.upper()
    else:
        pass
        
    try:
        clipboard.set(text)
        console.hud_alert('Copied to Clipboard')
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()

