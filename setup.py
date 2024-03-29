from setuptools import setup, find_packages

setup(name = "httpd_pyparser",
            description="HTTP daemons config files parser for Python 3",
            long_description = """
httpd_pyparser is a parser collection library, which uses PLY (Python Lex and Yacc). It
tokenizes the given text, and applies the language rules. If it's done, then
builds an own structure: a list of dictionary items.

The items contains the configuration directives from the original files, and
the number of lines where it founded. Also the items contains other datas about
the configuration line and structure.

Therefore, you can make many transformations on the structured data, and can
write back the modified config.
""",
            python_requires=">=3",
            license="""AGPLv3""",
            version = "0.3",
            author = "Ervin Hegedus",
            author_email = "airween@digitalwave.hu",
            maintainer = "Ervin Hegedus",
            maintainer_email = "airween@digitalwave.hu",
            url = "https://github.com/digitalwave/httpd_pyparser",
            packages = ['httpd_pyparser'],
            install_requires=[
              "ply >= 3.0"
            ],
            classifiers = [
              'Topic :: Text Processing'
            ],
            #data_files = [
            #  ('../../', ['apacheparsetab.py', 'nginxparsetab'])
            #],
            include_package_data = True,
            zip_safe = False
)
