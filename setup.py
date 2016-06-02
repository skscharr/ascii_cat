#!/usr/bin/env python
"""
_setup.py_

Setup script for ascii_cat.
"""
import ConfigParser
import setuptools

#
# read the conf for this package
#
config = ConfigParser.RawConfigParser()
config.read("package.conf")

#
# get the entry point(s)
#
scripts = [
    "{0} = {1}".format(opt, config.get("console_scripts", opt))
    for opt in config.options("console_scripts")
]

#
# read requirements
#
requirements_file = open('requirements.txt')
requirements = requirements_file.read().strip().split('\n')

setup_args = {
    "name": config.get("package", "name"),
    "version": config.get("package", "version"),
    "description": config.get("package", "description"),
    "url": config.get("package", "url"),
    "author": config.get("package", "author"),
    "author_email": config.get("package", "author_email"),
    "include_package_data": True,
    "install_requires": requirements,
    "entry_points": {
        "console_scripts": scripts
    }
}

setuptools.setup(**setup_args)
