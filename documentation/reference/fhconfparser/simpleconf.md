# SimpleConf

[Fhconfparser Index](../README.md#fhconfparser-index) /
[Fhconfparser](./index.md#fhconfparser) /
SimpleConf

> Auto-generated documentation for [fhconfparser.simpleconf](../../../fhconfparser/simpleconf.py) module.

- [SimpleConf](#simpleconf)
  - [SimpleConf](#simpleconf-1)
    - [SimpleConf().get](#simpleconf()get)

## SimpleConf

[Show source in simpleconf.py:51](../../../fhconfparser/simpleconf.py#L51)

SimpleConf works to combine some dictionary of options (likely from argparse)...

with the get method from FHConfParser to provide a very simple solution to enable
a user to extend the capabilities of FHConfParser such that command-line arguments
can be used to override config options

#### Arguments

- `configParser` *FHConfParser* - config parser
- `section` *str* - section to use
args (dict[str, Any]): some dictionary of commandline args.
eg. vars(parser.parse_args())

Example use:

```python
import argparse
from fhconfparser import FHConfParser, SimpleConf

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument(
 "--file",
 "-o",
 help="Filename to write to (omit for stdout)",
)
...
parser.add_argument(
 "--zero",
 "-0",
 help="Return non zero exit code if an incompatible license is found",
 action="store_true",
)
args = vars(parser.parse_args())

# ConfigParser (Parses in the following order: `pyproject.toml`, `setup.cfg`
configparser = FHConfParser()
configparser.parseConfigList(
 [("pyproject.toml", "toml"), ("setup.cfg", "ini")],
 ["tool"],
 ["tool"],
)

sc = SimpleConf(configparser, "licensecheck", args)

sc.get("zero", False) # Provide the actual default here (used if not provided
       # from the command line or through a config file)
```

#### Signature

```python
class SimpleConf:
    ...
```

### SimpleConf().get

[Show source in simpleconf.py:103](../../../fhconfparser/simpleconf.py#L103)

Get an option from the commandline/ the config.

#### Arguments

- `option` *str* - option name
- `fallback` *Optional[Any]* - value to fallback to. Default=None

#### Returns

- `Any` - command-line option or config option

#### Signature

```python
def get(self, option: str, fallback: Any | None = None) -> Any:
    ...
```


