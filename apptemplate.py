import apptemplate

AppYamlFormat = """application: %s
version: 1
runtime: python
api_version: 1

handlers:
- url: /.*
  script: index.py
"""

