[![License](https://img.shields.io/badge/License-AGPL-green.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![Latest Version](https://img.shields.io/pypi/v/httpd-pyparser.svg)](https://pypi.python.org/pypi/httpd-pyparser)

# httpd_pyparser

Welcome to the `httpd_pyparser` documentation.

The parser runs under Python 3.7+ on Linux, Windows and Mac.

Licensing
=========

**httpd_pyparser** is dual licensed under the following licenses. You can use the software according to the terms of your chosen license.

* [GNU Affero General Public License (AGPL) v3 with additional terms](https://www.gnu.org/licenses/agpl-3.0.html)
* Our Own Proprietary License - please contact with us

This means, we can apply any pull requests from any contributor after the agreement of our CLA. For mor information, please check our [contrbuting reference](CONTRIBUTING.md)

Installation
============

The parser relies on *Ply* as its underlying parsing library.

Therefore, to run it you will need:

* a **Python 3** interpreter
* **Ply** - the Python Ley Yacc library
* **YAML** and/or **JSON** it you want your output to be either of those

### Debian install

You can install these packages on Debian with this command:

```bash
sudo apt install python3-ply python3-yaml python3-simplejson
```

Try to keep the module updated, because it is under heavy development now.

Module Contents
===============

`httpd_pyparser` contains two main submodules:

* apache
* nginx

Both main submodules have three classes:

* Lexer
* Parser
* Writer

## Module version

Before you start to work with any classplease check the version to make sure you have the current one (`0.3`):

```python
$ python3
...
>>> import httpd_pyparser
>>> import httpd_pyparser.apache
>>> import httpd_pyparser.nginx
>>> httpd_pyparser.__version__
'0.3'
>>> httpd_pyparser.apache.__version__
'0.3'
>>> httpd_pyparser.nginx.__version__
'0.3'

```
Lexer classes
=============

The `Lexer` classes are wrappers for Ply's `lexer` object. You can use it independently, to **check** and **see** what tokens are in your `Apache` or `Nginx` configuration.

Here is a simple example:

```python
$ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import httpd_pyparser
>>> import httpd_pyparser.nginx
>>> import httpd_pyparser.apache
>>> 
>>> config = """<VirtualHost *:80>
...     ServerName www.yourdomain.com
...     Redirect / https://www.yourdomain.com
... </VirtualHost>
... """
>>> 
>>> mlexer = httpd_pyparser.apache.Lexer()
>>> mlexer.lexer.input(config)
>>> while True:
...     tok = mlexer.lexer.token()
...     if not tok:
...         break
...     print(tok)
... 
LexToken(T_CONFIG_DIRECTIVE_TAG,'<VirtualHost *:80>',1,0)
LexToken(T_CONFIG_DIRECTIVE,'ServerName',2,23)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'www.yourdomain.com',2,34)
LexToken(T_CONFIG_DIRECTIVE,'Redirect',3,57)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'/',3,66)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'https://www.yourdomain.com',3,68)
LexToken(T_CONFIG_DIRECTIVE_TAG_CLOSE,'</VirtualHost>',4,95)
>>>
>>> config = """server {
...     listen 80;
...     server_name www.yourhost.com;
... 
...     location / {
...         proxy_set_header X-Real-IP $remote_addr;
...         proxy_set_header X-Forwarded-For $remote_addr;
...         proxy_set_header Host $host;
...         proxy_pass http://vm-lxc1;
...     }
... }
... """
>>> mlexer = httpd_pyparser.nginx.Lexer()
>>> mlexer.lexer.input(config)
>>> while True:
...     tok = mlexer.lexer.token()
...     if not tok:
...         break
...     print(tok)
... 
LexToken(T_CONFIG_DIRECTIVE,'server',1,0)
LexToken(T_BRACE_OPEN,'{',1,7)
LexToken(T_CONFIG_DIRECTIVE,'listen',2,13)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'80',2,20)
LexToken(T_SEMICOLON,';',2,22)
LexToken(T_CONFIG_DIRECTIVE,'server_name',3,28)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'www.yourhost.com',3,40)
LexToken(T_SEMICOLON,';',3,56)
LexToken(T_CONFIG_DIRECTIVE,'location',5,63)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'/',5,72)
LexToken(T_BRACE_OPEN,'{',5,74)
LexToken(T_CONFIG_DIRECTIVE,'proxy_set_header',6,84)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'X-Real-IP',6,101)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'$remote_addr',6,111)
LexToken(T_SEMICOLON,';',6,123)
LexToken(T_CONFIG_DIRECTIVE,'proxy_set_header',7,133)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'X-Forwarded-For',7,150)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'$remote_addr',7,166)
LexToken(T_SEMICOLON,';',7,178)
LexToken(T_CONFIG_DIRECTIVE,'proxy_set_header',8,188)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'Host',8,205)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'$host',8,210)
LexToken(T_SEMICOLON,';',8,215)
LexToken(T_CONFIG_DIRECTIVE,'proxy_pass',9,225)
LexToken(T_CONFIG_DIRECTIVE_ARGUMENT,'http://vm-lxc1',9,236)
LexToken(T_SEMICOLON,';',9,250)
LexToken(T_BRACE_CLOSE,'}',10,256)
LexToken(T_BRACE_CLOSE,'}',11,258)
```

Parser classes
==============

The `Parser` classes are wrappers for Ply's `parser` object. The parser object needs a lexer class, but both `Parser` classes invoke the required `Lexer` and sets it up.

Here is a simple example:

```python
>>> mparser = httpd_pyparser.nginx.Parser()
>>> mparser.parser.parse(config)
>>> print(mparser.configlines)
[{'type': 'directive', 'value': 'server', 'lineno': 1, 'arguments': [], 'blocks': [[{'type': 'directive', 'value': 'listen', 'lineno': 2, 'arguments': [{'value': '80', 'lineno': 2, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'server_name', 'lineno': 3, 'arguments': [{'value': 'www.yourhost.com', 'lineno': 3, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'location', 'lineno': 5, 'arguments': [{'value': '/', 'lineno': 5, 'quote_type': 'no_quote'}], 'blocks': [[{'type': 'directive', 'value': 'proxy_set_header', 'lineno': 6, 'arguments': [{'value': 'X-Real-IP', 'lineno': 6, 'quote_type': 'no_quote'}, {'value': '$remote_addr', 'lineno': 6, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'proxy_set_header', 'lineno': 7, 'arguments': [{'value': 'X-Forwarded-For', 'lineno': 7, 'quote_type': 'no_quote'}, {'value': '$remote_addr', 'lineno': 7, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'proxy_set_header', 'lineno': 8, 'arguments': [{'value': 'Host', 'lineno': 8, 'quote_type': 'no_quote'}, {'value': '$host', 'lineno': 8, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'proxy_pass', 'lineno': 9, 'arguments': [{'value': 'http://vm-lxc1', 'lineno': 9, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}]]}]]}]
>>>
>>> 
>>> config = """<VirtualHost *:80>
...     ServerName www.yourdomain.com
...     Redirect / https://www.yourdomain.com
... </VirtualHost>
... """
>>> mparser = httpd_pyparser.apache.Parser()
>>> mparser.parser.parse(config)
>>> print(mparser.configlines)
[{'type': 'directive_tag', 'value': 'VirtualHost', 'lineno': 1, 'arguments': [{'value': '*:80', 'quote_type': 'no_quote', 'lineno': 1}], 'blocks': [[{'type': 'directive', 'value': 'ServerName', 'lineno': 2, 'arguments': [{'value': 'www.yourdomain.com', 'lineno': 2, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'Redirect', 'lineno': 3, 'arguments': [{'value': '/', 'lineno': 3, 'quote_type': 'no_quote'}, {'value': 'https://www.yourdomain.com', 'lineno': 3, 'quote_type': 'no_quote'}], 'blocks': []}]]}, {'type': 'directive_tag_close', 'value': 'VirtualHost', 'lineno': 4, 'arguments': [], 'blocks': []}]
```

### Writer

These classes transforms the inside structure to the string. You can save the result to a file. This class converts YAML, JSON, etc, to a config file. See the example file `test_writer.py` for how it works.

Here is a simple example:

```python
struct = [{'type': 'directive_tag', 'value': 'VirtualHost', 'lineno': 1, 'arguments': [{'value': '*:80', 'quote_type': 'no_quote', 'lineno': 1}], 'blocks': [[{'type': 'directive', 'value': 'ServerName', 'lineno': 2, 'arguments': [{'value': 'www.yourdomain.com', 'lineno': 2, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'Redirect', 'lineno': 3, 'arguments': [{'value': '/', 'lineno': 3, 'quote_type': 'no_quote'}, {'value': 'https://www.yourdomain.com', 'lineno': 3, 'quote_type': 'no_quote'}], 'blocks': []}]]}, {'type': 'directive_tag_close', 'value': 'VirtualHost', 'lineno': 4, 'arguments': [], 'blocks': []}]
>>> mwriter = httpd_pyparser.apache.Writer(struct, "        ")
>>> mwriter.generate()
>>> print("\n".join(mwriter.output))
<VirtualHost *:80>
        ServerName www.yourdomain.com
        Redirect / https://www.yourdomain.com
</VirtualHost>
>>>
>>> struct = [{'type': 'directive', 'value': 'server', 'lineno': 1, 'arguments': [], 'blocks': [[{'type': 'directive', 'value': 'listen', 'lineno': 2, 'arguments': [{'value': '80', 'lineno': 2, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'server_name', 'lineno': 3, 'arguments': [{'value': 'www.yourhost.com', 'lineno': 3, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'location', 'lineno': 5, 'arguments': [{'value': '/', 'lineno': 5, 'quote_type': 'no_quote'}], 'blocks': [[{'type': 'directive', 'value': 'proxy_set_header', 'lineno': 6, 'arguments': [{'value': 'X-Real-IP', 'lineno': 6, 'quote_type': 'no_quote'}, {'value': '$remote_addr', 'lineno': 6, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'proxy_set_header', 'lineno': 7, 'arguments': [{'value': 'X-Forwarded-For', 'lineno': 7, 'quote_type': 'no_quote'}, {'value': '$remote_addr', 'lineno': 7, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'proxy_set_header', 'lineno': 8, 'arguments': [{'value': 'Host', 'lineno': 8, 'quote_type': 'no_quote'}, {'value': '$host', 'lineno': 8, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}, {'type': 'directive', 'value': 'proxy_pass', 'lineno': 9, 'arguments': [{'value': 'http://vm-lxc1', 'lineno': 9, 'quote_type': 'no_quote'}, {'value': None, 'quote_type': 'no_quote'}], 'blocks': []}]]}]]}]
>>> mwriter = httpd_pyparser.nginx.Writer(struct, "        ")
>>> mwriter.generate()
>>> print("\n".join(mwriter.output))
server {
        listen 80;
        server_name www.yourhost.com;

        location / {
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $remote_addr;
                proxy_set_header Host $host;
                proxy_pass http://vm-lxc1;
        }
}
```

Inside of structure
===================

The `Parser` classes reads the configuration files, and transforms them into a Python `list`. Every item in this list is a `dictionary`. Every dictionary item has the keys `type` and `lineno`. Depending on the `type` there might be additional keys.

These are the supported types:

* Comment
* Directive

There are four types of dictionary objects for types above:

#### Apache

```python
{
  'type': 'comment',
  'value': <class 'str'>,
  'lineno': <class 'int'>
}

{
  'type': 'directive',
  'value': <class 'str'>,
  'lineno': <class 'int'>,
  'arguments': <class 'list' of 'arg'>,
  'blocks': <class 'list' of 'directive' or 'directive_tag'>
}

{
  'type': 'directive_tag',
  'value': <class 'str'>,
  'lineno': <class 'int'>,
  'arguments': <class 'list' of 'arg'>,
  'blocks': <class 'list' of 'directive' or 'directive_tag'>
}

{
  'type': 'directive_tag_close',
  'value': <class 'str'>,
  'lineno': <class 'int'>,
  'arguments': None,
  'blocks': None
}

# arg type:
{
  'value': <class 'str'>,
  'quote_type': QUOTE_TYPE,
  'lineno': <class 'int'>
}
```

#### Nginx

```python
{
  'type': 'comment',
  'value': <class 'str'>,
  'lineno': <class 'int'>
}

{
  'type': 'directive',
  'value': <class 'str'>,
  'lineno': <class 'int'>,
  'arguments': <class 'list' of 'arg'>,
  'blocks':  <class 'list' of 'directive'>
}

# arg type:
{
  'value': <class 'str'>,
  'lineno': <class 'int'>,
  'quote_type': QUOTE_TYPE
}
```

Quote type:
```python
'QUOTE_TYPE' could be item from set('no_quote', 'quotes', 'quoted')
```

where
* `no_quote` - there isn't any quote mark
* `quotes` - means **S**ingle quote (`'`)
* `quoted` - means **D**double quote (`"`)

type
----
**Description:** type of the configuration directive

**Used at:** Comment, Directive, DirectiveTag

**Syntax:** `'type': <class 'str'>`

**Example Usage:** `'type': "DirectiveTag"`

**Default Value:** no default value

**Possible value:** `Comment`, or any possible directive in ModSecurity (except `DirectiveTag` and `Directive`)

**Scope:** Comment, Directive or DirectiveTag dictionary

**Added Version:** 0.1

lineno
------
**Description**: line number in the original file

**Syntax:** `'lineno': <class 'int'>`

**Example Usage:** `'lineno': 10`

**Default Value:** no default value

**Possible value:** a positive integer

**Scope:** every item in the list

**Added Version:** 0.1


argument
--------
**Description**: the dictionary next to the directive

**Syntax:** `{'argument': <class 'str'>, 'quote_type': QUOTE_TYPE}`

**Example Usage:** `{'argument': '# this is a comment', 'quote_type': 'no_quote'}`

**Default Value:** no default value

**Possible value:** no restrictions

**Scope:** Comment or Directive dictionary

**Added Version:** 0.1

**Changd in:** 1.0


quoted
------
**Description**: indicates if the argument was quoted or not

**Syntax:** `'quoted': <class 'str'>`

**Example Usage:** `'quoted': quotes`

**Default Value:** `no_quoted`

**Possible value:** `no_quoted`, `quoted` (quoted with DOUBLE quotes `"`), `quotes` (quoted with SINGLE quotes `'`)

**Scope:** Dictionary key in Comment, Directive types, and used list: variables, actions and arguments.

**Added Version:** 0.1


Examples
========

There is the `examples/` subdirectory with some examples, data, and descriptions in the code. There are three scripts:

```bash
examples/test_lexer.py
examples/test_parser.py
examples/test_writer.py
```

All of them demonstrates how the classes work. There are two more scripts in root directory of source tree, which converts Apache2 or Nginx configuration files (without recursion) into YAML or JSON files.

Let's see more details with help of examples.

Consider a very simple configuration file for Apache2 web server:

```
<VirtualHost *:80>
    ServerName www.yourdomain.com
</VirtualHost>
```

The parser will generate this structure:
```
[
    {
        "type": "directive_tag",
        "value": "VirtualHost",
        "lineno": 1,
        "arguments": [
            {
                "lineno": 1,
                "quote_type": "no_quote",
                "value": "*:80"
            }
        ],
        "blocks": [
            [
                {
                    "type": "directive",
                    "value": "ServerName",
                    "lineno": 2,
                    "arguments": [
                        {
                            "lineno": 2,
                            "quote_type": "no_quote",
                            "value": "www.yourdomain.com"
                        }
                    ],
                    "blocks": []
                }
            ]
        ]
    },
    {
        "type": "directive_tag_close",
        "value": "VirtualHost",
        "lineno": 3,
        "arguments": [],
        "blocks": []
    }
]
```

This is a list with two items. First item is a `directive_tag` type, the value is the `VirtualHost`. This is in the first line. The tag has an argument: `*:80`. The second item is a `directive_tag_close`, which indicates this is the end of the block. The first item has a `blocks` key, which contains the blocks. Every block item can be a `comment`, `directive` or `directive_tag`. The `blocks` list has one item, generated from the `ServerName www.yourdomain.com`. This is a `directive` (not `directive_tag`), value is the `ServerName` in 2nd line, and it has one argument: `www.yourdomain.com`.

Now take a look to Nginx config:

```
server {
    server_name www.yourhost.com;

    location / {
        proxy_pass http://vm-lxc1;
    }
}
```
This will generates a structure like this:
```
[
    {
        "type": "directive",
        "value": "server",
        "lineno": 1,
        "arguments": [],
        "blocks": [
            [
                {
                    "type": "directive",
                    "value": "server_name",
                    "lineno": 2,
                    "arguments": [
                        {
                            "lineno": 2,
                            "quote_type": "no_quote",
                            "value": "www.yourhost.com"
                        },
                        {
                            "quote_type": "no_quote",
                            "value": null
                        }
                    ],
                    "blocks": []
                },
                {
                    "type": "directive",
                    "value": "location",
                    "lineno": 4,
                    "arguments": [
                        {
                            "lineno": 4,
                            "quote_type": "no_quote",
                            "value": "/"
                        }
                    ],
                    "blocks": [
                        [
                            {
                                "type": "directive",
                                "value": "proxy_pass",
                                "lineno": 5,
                                "arguments": [
                                    {
                                        "lineno": 5,
                                        "quote_type": "no_quote",
                                        "value": "http://vm-lxc1"
                                    },
                                    {
                                        "quote_type": "no_quote",
                                        "value": null
                                    }
                                ],
                                "blocks": []
                            }
                        ]
                    ]
                }
            ]
        ]
    }
]

```

Reporting issues
================

If you run into unexpected behavior, found a bug, or have a feature request, just [create a new issue](https://github.com/digitalwave/httpd_pyparser/issues/new), or drop an e-mail to us: **modsecurity** at **digitalwave** dot **hu**.

Known bugs
==========

Actually, there isn't any know bug.

