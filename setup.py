#!/usr/bin/env python3

# +------------------------+			   
# | Created with Sailboat  |
# |                        |
# | Do not edit this file  |
# | directly. Instead  	   |			   
# | you should edit the	   |			   
# | `sailboat.toml` file.  |			   
# +------------------------+	

import setuptools

try:
	with open("README.md", "r") as fh:
		long_description = fh.read()
except FileNotFoundError:
	long_description = """
	# Test_Project
	A demo of Sailboat's capabilities
	### Contributors
	- Cole Wilson
	### Contact
	<cole@colewilson.xyz>
	"""

options = {
	"name": "test_project_pycon2021",
	"version": "0.0.3",
	"scripts": ['bin/hello'],
	"entry_points": {'console_scripts': []},
	"author": "Cole Wilson",
	"author_email": "cole@colewilson.xyz",
	"description": "A demo of Sailboat's capabilities",
	"long_description": long_description,
	"long_description_content_type": "text/markdown",
	"url": "https://github.com",
	"packages": setuptools.find_packages(),
	"install_requires": [],
	"classifiers": ["Programming Language :: Python :: 3"],
	"python_requires": '>=3.6',
	"package_data": {"": [], },
	"license": "none",
	"keywords": 'kw1 kw2 kw3',
	"setup_requires": ['wheel'],
}

custom_options = {}

if __name__ == "__main__":
	setuptools.setup(**custom_options, **options)
