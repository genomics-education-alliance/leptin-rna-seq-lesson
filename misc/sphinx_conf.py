# -*- coding: utf-8 -*-

import sys
import os
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
import sphinx_fontawesome


extensions = [
    'sphinx.ext.autodoc',
    'sphinx_fontawesome'
]

project = 'RNA-Seq analysis of Mouse Leptin Gene'
copyright = '2019, Genomics Education Alliance'
author = 'Genomics Education Alliance'
version = '1.0'
release = '1.0'

language = None
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst']

common_static_path = os.path.join(os.path.dirname(__file__), 'static')

templates_path = ['_templates']
html_static_path = ['_static', common_static_path]
exclude_patterns = ['_build']
master_doc = 'index'
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'

htmlhelp_basename = 'GEA_lesson'

latex_elements = {}
latex_documents = [
    (master_doc, 'GEA_lesson.tex', 'GEA Lesson',
     'GEA', 'lesson'),
]

man_pages = [
    (master_doc, 'GEA Lesson', 'GEA Lesson',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'GEA Lesson', 'GEA Lesson',
     author, 'GEA', 'GEA',
     'Miscellaneous'),
]

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']


def setup(app):
    app.add_config_value(
        'recommonmark_config',
        {
            'enable_auto_toc_tree': True,
            'enable_eval_rst': True,
            'auto_toc_tree_section': 'Contents',
        },
        True
    )
    app.add_transform(AutoStructify)
    app.add_stylesheet('gea.css')
    #uncomment to enable table sorting app.add_javascript('jquery.tablesorter.min.js')
    app.add_javascript('gea.js')
    # enable inline question and answer
    app.add_javascript('question-answer.js')
