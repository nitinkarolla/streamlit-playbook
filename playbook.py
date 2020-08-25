# -*- coding: utf-8 -*-
"""Streamlit playbook for learning

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:

"""

import streamlit as st
import numpy as np
import pandas as pd
import time
from pages import overview, get_started


st.title("Streamlit Playbook")

PAGES = {
    "Overview": overview,
    "Getting Started": get_started,
    "Widgets": None,
    "Commands": None,
    "References": None,
}


"""Main function of the App"""
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]


with st.spinner(f"Loading {selection} ..."):
    page.main()
