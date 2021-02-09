# search-python-client
This library provides an easy to use library for searching DNAstacks covidcloud database.

# Dependencies
Written in python 3.7.4

# Install
```
pip install search-python-client --no-cache-dir
```

# Tests
There are many ways to test, but this is the easiest way
```
git clone https://github.com/DNAstack/search-python-client
cd search-python-client
python setup.py test
```

# Config File
To protect your DRS Server variables I have allowed for the user to submit their server variables through a config.ini file.

Your file should be structured in one of two ways depending on if you want auth or wallet support. Please note that only one of these ways must be used. You cannot use both! 

Also you cannot pass the `config_file` parameter with another parameter (`auth` or `wallet`). This will cause `config_file` to overwrite the values of the other variables.

For auth:
```
[drs-auth]
username = user
password = pass
```

For wallet:
```
[drs-wallet]
token = 123
```