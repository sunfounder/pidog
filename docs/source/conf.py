# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import sphinx_rtd_theme
import time

project = 'SunFounder PiDog Kit'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'sunfounder'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton'
]

# Link to other projects' documentation with intersphinx. Use the intersphinx_mapping configuration to indicate the name and link of the projects you want to use
intersphinx_mapping = {
    'ezblock': ('https://docs.sunfounder.com/projects/ezblock3/en/latest/', None),
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_static_path = ['_static']
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
]
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

language = 'en'
locale_dirs = ['locale/'] 

gettext_compact = False

rst_epilog = """

.. |app_connect| image:: /python/img/app_connect.jpg
    :width: 20

"""

#links
rst_epilog += """

.. |link_microphone| raw:: html

    <a href="https://www.sunfounder.com/products/mini-usb-microphone?_pos=2&_sid=d05c80026&_ss=r" target="_blank">Microphone link</a>

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/api-keys" target="_blank">OpenAI API</a>

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/4arqbqG" target="_blank">here</a>

.. |link_code_10_balance| raw:: html

    <a href="https://github.com/sunfounder/pidog/blob/master/examples/10_balance.py" target="_blank">10_balance.py - Github</a>

.. |link_code_11_keyboard_control| raw:: html

    <a href="https://github.com/sunfounder/pidog/blob/master/examples/11_keyboard_control.py" target="_blank">11_keyboard_control.py - Github</a>

.. |link_robot_hat_v4| raw:: html

    <a href="https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/hardware_introduction.html" target="_blank">Robot HAT</a>

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pidog/de/latest/index.html" target="_blank">Deutsch Online-Kurs</a>

.. |link_jp_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pidog/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pidog/en/latest/" target="_blank">English Online-tutorials</a>

.. |link_PiDog| raw:: html

    <a href="https://www.sunfounder.com/products/sunfounder-pidog-robot-dog-kit-for-raspberry-pi?_pos=1&_sid=313a4c894&_ss=r&variant=44517213896939" target="_blank">Purchase Link for PiDog</a>

.. |link_Pi_Dog| raw:: html

    <a href="https://www.sunfounder.com/products/sunfounder-pidog-robot-dog-kit-for-raspberry-pi?_pos=1&_sid=313a4c894&_ss=r&variant=44517213896939" target="_blank">PiDog</a>

"""
