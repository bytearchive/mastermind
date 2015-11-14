# Proxy Switch

Test [mitmproxy](https://mitmproxy.org) via rewriting their [mitmwrapper.py example](https://github.com/mitmproxy/mitmproxy/blob/master/examples/mitmproxywrapper.py)

## Install

```sh
pip install "git+https://github.com/ustwo/proxyswitch.git@v0.4.3#egg=proxyswitch"
```

## Proxyswitch

Check the help:

```sh
proxyswitch --help
```


## Mastermind

Mastermind combines `mitmdump` and `proxyswitch` making sure the proxy settings
are enabled when the mitmproxy starts and disabling them when the proxy stops.

There are two forms you can use, "Simple" and "Script".  The first expects a
response body and a URL.  It will use the response body everytime it intercepts
the given URL.


```sh
sudo mastermind --response-body $(pwd)/test/records/fake.json" \
                https://api.github.com/users/octocat/orgs
```

The former expects a mitmproxy Python script. So you can do:

```sh
sudo mastermind --script $(pwd)/myscript.py
```

Or pass parameters to your script the same way mitmproxy does:

```sh
sudo mastermind --script "$(pwd)/myscript.py param1 param2"
```

If you go for the `--script` approach, you have to explicitly manage proxyswitch
yourself. Adding the following will do the trick:

```python
import proxyswitch as pswitch

def start(context, argv):
    enable()

def done(context):
    disable()

def enable():
    settings = ('127.0.0.1', '8080')
    pswitch.enable(*settings)

def disable():
    pswitch.disable()
```


Check the help for more.

```sh
mastermind --help
```


## Maintainers

* [Arnau Siches](mailto:arnau@ustwo.com)
