# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mingshe', 'mingshe._vendor.pegen']

package_data = \
{'': ['*'], 'mingshe': ['_vendor/*'], 'mingshe._vendor.pegen': ['templates/*']}

entry_points = \
{'console_scripts': ['mingshe = mingshe.commands:main']}

setup_kwargs = {
    'name': 'mingshe',
    'version': '0.7.0',
    'description': '',
    'long_description': "# MíngShé\n\nA better [Python](https://www.python.org/) superset language. Use [Pegen](https://github.com/we-like-parsers/pegen) to compile the code.\n\n> “鲜山多金玉，无草木，鲜水出焉，而北流注于伊水。其中多鸣蛇，其状如蛇而四翼，其音如磬，见则其邑大旱”——《山海经》\n\n## Install\n\n```\npip install mingshe\n```\n\n## Usage\n\n### As a script\n\nWrite some code in `main.she`, then run `mingshe ./main.she` to execute code.\n\n```python\n10 |> range |> map(pow(?, 2), ?) |> list |> print\n```\n\n### Compile to python\n\nYou can use `mingshe --compile ./main.she` to generate python file.\n\n### As a module\n\nYou can directly import MíngShé script as a module, as long as the script name ends with `.she`.\n\nExample:\n\n```python\n# lib.she\ndef digit_sum(s: str) -> int:\n    return s |> map(int, ?) |> sum\n```\n\n```python\n# main.py\nfrom lib import digit_sum\nprint(digit_sum('123456'))\n```\n\n## Extended syntax\n\n### Pipe\n\nExample:\n\n```\nrange(10) |> sum |> print\n```\n\nCompile to:\n\n```python\nprint(sum(range(10)))\n```\n\n#### Priority\n\nThe priority of `|>` is lower than `|` and higher than comparison operations (`in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`).\n\n### Conditional\n\nExample:\n\n```\na ? b : c\n```\n\nCompile to:\n\n```python\nb if a else c\n```\n\n#### Priority\n\n`a ? b: c` has the same priority as `b if a else c`.\n\n### Partial\n\nExample:\n\n```\nsquare = pow(?, 2)\n```\n\nCompile to:\n\n```python\n(lambda pow: lambda _0: pow(_0, 2))(pow)\n```\n\n### Nullish coalescing\n\nExample:\n\n```\na ?? b\n```\n\nCompile to:\n\n```python\na if a is not None else b\n```\n\n#### Priority\n\n`??` has the same priority as `or`.\n\n#### Note\n\nWhen you need to use `??` with `or`, you need to use parentheses in the outer layer, otherwise it will cause a syntax error.\n\n```\na or b ?? c    # syntax error\n(a or b) ?? c  # OK\na or (b ?? c)  # OK\n```\n\n### Optional chaining\n\nExample:\n\n```\na?.b\n```\n\nCompile to:\n\n```python\na if a is None else a.b\n```\n\nExample:\n\n```\na?[b]\n```\n\nCompile to:\n\n```python\na if a is None else a[b]\n```\n\nExample:\n\n```\na?.b()\n```\n\nCompile to:\n\n```python\na if a is None else a.b()\n```\n\n## Change log\n\nRead [releases](https://github.com/abersheeran/mingshe/releases) to see the change log.\n",
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/mingshe',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

