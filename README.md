sslcheck
========
Author : Jonas Björk <jonas.bjork@gmail.com><br />
Date   : 2014<br />
License: GNU GPLv2

Check if SSL certificates on list of sites are valid or not.

## Sample output

	>>> SSLcheck by Jonas Björk <jonas.bjork@gmail.com> 2014 <<<

	=== Testing SSL on 2 sites ===
	[CERT_OK  ] > Testing SSL on www.jonasbjork.net ... (www.jonasbjork.net)
	[CERT_OK  ] > Testing SSL on www.google.com ... (www.google.com)

	=== Result ===
	Certificates OK                      :  2
	Certificates OK, but wrong for domain:  0
	Certificates FAILED                  :  0

## Dependencies

The `AllCA.pem` file is the root certificates (CA) needed to test for
certificate validity. ([https://gist.github.com/caleb-vear/8274254#file-allca-pem|source] of file)

Python modules: `socket` and `ssl` which should be distributed with 
your Python version (>2.6).

## Function

You add a list of domains to check SSL on in the `sites`-list:

```python
sites = [
	'www.jonasbjork.net',
	'www.google.com'
]
```

Execute the script: `python sslcheck.py`. The script exits with `0` if 
everything is OK, else it exits with `1`.

