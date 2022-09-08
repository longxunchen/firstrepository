# -*- coding: utf-8 -*-
"""Sphinx configuration file."""
import time

author = "Jan Holthuis"
project = "sphinx-multiversion"
#release = "master"
#version = "master"
copyright = "{}, {}".format(time.strftime("%Y"), author)

html_theme = "alabaster"
html_theme_options = {
    "github_repo": "sphinx-multiversion",
    "github_user": "Holzhaus",
    "github_banner": True,
    "github_button": True,
    "travis_button": True,
    "show_relbar_bottom": True,
}
html_last_updated_fmt = "%c"
master_doc = "index"
pygments_style = "friendly"
templates_path = ["_templates"]
extensions = [
    "sphinx_multiversion",
]

templates_path = [
    "_templates",
]

html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "versioning.html",
    ],
}

#smv_remote_whitelist = r"^origin$"

#smv_branch_whitelist = r"^master$"

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = None

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
#smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
#smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
#smv_prefer_remote_refs = False
