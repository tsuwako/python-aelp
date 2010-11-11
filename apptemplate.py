import apptemplate

AppYaml = """application: %s
version: 1
runtime: python
api_version: 1

handlers:
- url: /.*
  script: index.py
"""

PyFile = """
print 'Content-Type: text/plain'
print ''
print 'Hello, world!'
"""
