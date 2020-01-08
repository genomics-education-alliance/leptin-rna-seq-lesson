#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# General information about the project.

import sys
import os
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
import sphinx_fontawesome
sys.path.insert(0, os.path.dirname(__file__))


rst_prolog = sphinx_fontawesome.prolog

from misc.sphinx_conf import *  # noqa

project = 'RNA-Seq analysis of Mouse Leptin Gene'
copyright = '2019, Genomics Education Alliance'
author = 'your_name'
version = '1.0'
release = '1.0'

html_logo = './img/GEA_logo.png'
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
