#!/usr/bin/env python3

import os
import posixpath
from urllib.parse import quote
import re


def regexReplace(string, search, replacement):
    return re.compile(search).sub(replacement, string)


languageCount = 0
languagesText = ""

# List the available languages
for directory in sorted(os.listdir('.')):
    if not (directory == '.' or directory == '..' or directory[0] == '.' or os.path.isfile(directory)):
        for filename in sorted(os.listdir(directory), key=lambda s: s.lower()):
            if os.path.isfile(os.path.join(directory, filename)):
                language = os.path.splitext(filename)[0].replace(
                    '-', ' ').replace('_', ' ').title()
                languagesText += f'* [{language}]({posixpath.join(quote(directory), quote(filename))})\n'
                languageCount += 1

result = f"""<!--Languages start-->
## Languages ({languageCount} total)

{languagesText}<!--Languages end-->"""

<<<<<<< HEAD
readmeContents = open('readme.md', 'r', encoding="utf-8").read()

open('readme.md', 'w', encoding="utf-8").write(regexReplace(
=======
readmeContents = open('README.md', 'r', encoding="utf-8").read()

open('README.md', 'w', encoding="utf-8").write(regexReplace(
>>>>>>> 650e43f2adbb7558d5367e8865662ffaba528374
    readmeContents, r"<!--Languages start-->(.|\n)*<!--Languages end-->", result))
