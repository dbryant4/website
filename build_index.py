""" Quick and dirty script to auto populate the summary section in index.html
    with the summary field in resume.md
"""

import json

import markdown2
import CommonMark

from jinja2 import Template

parser = CommonMark.DocParser()

ast = parser.parse(file('resume.md', 'r').read())
summary = ast.children[3].strings[0]
summary_html = markdown2.markdown(summary)

with file('index.html.j2', 'r') as index_template:
    template = Template(index_template.read())

with file('index.html', 'w') as index_html:
    index_html.write((template.render(summary=summary_html)))
