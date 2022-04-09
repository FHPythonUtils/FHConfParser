# FHConfParser

> Auto-generated documentation for [fhconfparser.fhconfparser](../../../fhconfparser/fhconfparser.py) module.

Provides a config language independent way to read a config file.

- [Fhconfparser](../README.md#fhconfparser-index) / [Modules](../MODULES.md#fhconfparser-modules) / [Fhconfparser](index.md#fhconfparser) / FHConfParser
    - [Currently supports](#currently-supports)
    - [FHConfParser](#fhconfparser)
        - [FHConfParser().defaults](#fhconfparserdefaults)
        - [FHConfParser().get](#fhconfparserget)
        - [FHConfParser().getbool](#fhconfparsergetbool)
        - [FHConfParser().getfloat](#fhconfparsergetfloat)
        - [FHConfParser().getint](#fhconfparsergetint)
        - [FHConfParser().getstr](#fhconfparsergetstr)
        - [FHConfParser().hasOption](#fhconfparserhasoption)
        - [FHConfParser().hasSection](#fhconfparserhassection)
        - [FHConfParser().options](#fhconfparseroptions)
        - [FHConfParser().parseConfigList](#fhconfparserparseconfiglist)
        - [FHConfParser().parseIni](#fhconfparserparseini)
        - [FHConfParser().parseJson](#fhconfparserparsejson)
        - [FHConfParser().parseToml](#fhconfparserparsetoml)
        - [FHConfParser().sections](#fhconfparsersections)

## Rationale for project
For instance toml and ini syntax is very similar but not identical. Currently, tools such as
pylint must implement custom ways to deal with this. Hopefully this code
streamlines that a bit.

## Currently supports

- Ini
- Toml
- Json

## FHConfParser

[[find in source code]](../../../fhconfparser/fhconfparser.py#L28)

```python
attr.s(auto_attribs=True)
class FHConfParser():
```

FHConfParser.

#### Returns

- `FHConfParser` - parser object.
- Call `parseConfigList` to parse files
- Call `data` to access the internal rep

### FHConfParser().defaults

[[find in source code]](../../../fhconfparser/fhconfparser.py#L209)

```python
def defaults() -> dict[str, Any]:
```

Return a dictionary containing the defaults.

#### Returns

- `list[str]` - A dictionary containing the defaults

### FHConfParser().get

[[find in source code]](../../../fhconfparser/fhconfparser.py#L236)

```python
def get(section: str | None, option: str, fallback: Any = None) -> Any:
```

Get a value from section.option with some fallback for if it doesn't exist.

#### Arguments

- `section` *str* - the specified section
- `option` *str* - the specified key/ option
- `fallback` *Any, optional* - the fallback value for if it doesn't exist.
Defaults to None.

#### Returns

- `Any` - the value at section.option or fallback

### FHConfParser().getbool

[[find in source code]](../../../fhconfparser/fhconfparser.py#L290)

```python
def getbool(
    section: str | None,
    option: str,
    fallback: Any = None,
    strict: bool = True,
) -> bool:
```

Get a value from section.option with some fallback for if it doesn't exist as an bool.

#### Arguments

- `section` *str* - the specified section
- `option` *str* - the specified key/ option
- `fallback` *Any, optional* - the fallback value for if it doesn't exist.
Defaults to None.
- `strict` *bool* - raise an error if the cast fails when true, else return
the value uncasted. Defaults to True

#### Returns

- `bool` - the value at section.option or fallback (Any if strict=False)

### FHConfParser().getfloat

[[find in source code]](../../../fhconfparser/fhconfparser.py#L272)

```python
def getfloat(
    section: str | None,
    option: str,
    fallback: Any = None,
    strict: bool = True,
) -> float:
```

Get a value from section.option with some fallback for if it doesn't exist as an float.

#### Arguments

- `section` *str* - the specified section
- `option` *str* - the specified key/ option
- `fallback` *Any, optional* - the fallback value for if it doesn't exist.
Defaults to None.
- `strict` *bool* - raise an error if the cast fails when true, else return
the value uncasted. Defaults to True

#### Returns

- `float` - the value at section.option or fallback (Any if strict=False)

### FHConfParser().getint

[[find in source code]](../../../fhconfparser/fhconfparser.py#L254)

```python
def getint(
    section: str | None,
    option: str,
    fallback: Any = None,
    strict: bool = True,
) -> int:
```

Get a value from section.option with some fallback for if it doesn't exist as an int.

#### Arguments

- `section` *str* - the specified section
- `option` *str* - the specified key/ option
- `fallback` *Any, optional* - the fallback value for if it doesn't exist.
Defaults to None.
- `strict` *bool* - raise an error if the cast fails when true, else return
the value uncasted. Defaults to True

#### Returns

- `int` - the value at section.option or fallback (Any if strict=False)

### FHConfParser().getstr

[[find in source code]](../../../fhconfparser/fhconfparser.py#L308)

```python
def getstr(
    section: str | None,
    option: str,
    fallback: Any = None,
    strict: bool = True,
) -> str:
```

Get a value from section.option with some fallback for if it doesn't exist as an str.

#### Arguments

- `section` *str* - the specified section
- `option` *str* - the specified key/ option
- `fallback` *Any, optional* - the fallback value for if it doesn't exist.
Defaults to None.
- `strict` *bool* - raise an error if the cast fails when true, else return
the value uncasted. Defaults to True

#### Returns

- `str` - the value at section.option or fallback (Any if strict=False)

### FHConfParser().hasOption

[[find in source code]](../../../fhconfparser/fhconfparser.py#L197)

```python
def hasOption(section: str | None, option: str) -> bool:
```

Return True if the option present in the data rep (under a given section.

#### Arguments

- `section` *str* - section to get
- `option` *str* - ... and option to get

#### Returns

- `bool` - Return True if the option present in the data rep (under a given section

### FHConfParser().hasSection

[[find in source code]](../../../fhconfparser/fhconfparser.py#L186)

```python
def hasSection(section: str | None) -> bool:
```

Return True if the section present in the data rep.

#### Arguments

- `section` *str* - section to get

#### Returns

- `bool` - Return True if the section present in the data rep.

### FHConfParser().options

[[find in source code]](../../../fhconfparser/fhconfparser.py#L225)

```python
def options(section: str | None) -> list[str]:
```

Return a list of options available in the specified section.

#### Arguments

- `section` *str* - the specified section

#### Returns

- `list[str]` - list of options

### FHConfParser().parseConfigList

[[find in source code]](../../../fhconfparser/fhconfparser.py#L39)

```python
def parseConfigList(
    confList: list[tuple[str, str]],
    tomlNamespace: list[str] | None = None,
    jsonNamespace: list[str] | None = None,
) -> list[str]:
```

Parse a list of tuples containing paths to config files and the format.

...and update the internal rep with the new data.

e.g.

```python
>>> parseConfigList([("pyproject.toml", "toml"), (".config.ini", "ini")])
```

Note that data is not overwritten so if "pyproject.toml" and ".config.ini"
define some data at section.option then the value defined by "pyproject.toml"
takes precedent.

#### Arguments

confList (list[tuple[str, str]]): A list of tuples of config files
and format. e.g. [("pyproject.toml", "toml"), (".config.ini", "ini")]
- `tomlNamespace` *list[str], optional* - table to treat as root . Defaults to None.
- `jsonNamespace` *list[str], optional* - define root. Defaults to None.

#### Returns

- `list[str]` - list of successfully parsed files

### FHConfParser().parseIni

[[find in source code]](../../../fhconfparser/fhconfparser.py#L81)

```python
def parseIni(file: str, throws: bool = False, **kwargs) -> list[str]:
```

Parse a single ini file and update the internal rep with the new data.

#### Arguments

- `file` *str* - config file to parse
- `throws` *bool* - Throw an exception if there is a parsing failure.
Defaults to False.
- `kwargs` - ignored

#### Raises

- `ParsingError` - if throws = True

#### Returns

- `list[str]` - list of successfully parsed files

### FHConfParser().parseJson

[[find in source code]](../../../fhconfparser/fhconfparser.py#L157)

```python
def parseJson(
    file: str,
    jsonNamespace: list[str] | None = None,
    throws: bool = False,
    **kwargs,
) -> list[str]:
```

Parse a single json file and update the internal rep with the new data.

#### Arguments

- `file` *str* - config file to parse
- `jsonNamespace` *list[str], optional* - define root. Defaults to None.
- `throws` *bool* - Throw an exception if there is a parsing failure.
Defaults to False.
- `kwargs` - ignored

#### Raises

- `JSONDecodeError` - if throws = True

#### Returns

- `list[str]` - list of successfully parsed files

### FHConfParser().parseToml

[[find in source code]](../../../fhconfparser/fhconfparser.py#L128)

```python
def parseToml(
    file: str,
    tomlNamespace: list[str] | None = None,
    throws: bool = False,
    **kwargs,
) -> list[str]:
```

Parse a single toml file and update the internal rep with the new data.

#### Arguments

- `file` *str* - config file to parse
- `tomlNamespace` *list[str], optional* - table to treat as root . Defaults to None.
- `throws` *bool* - Throw an exception if there is a parsing failure.
Defaults to False.
- `kwargs` - ignored

#### Raises

- `ParseError` - if throws = True

#### Returns

- `list[str]` - list of successfully parsed files

### FHConfParser().sections

[[find in source code]](../../../fhconfparser/fhconfparser.py#L217)

```python
def sections() -> list[str]:
```

Return a list of the sections available.

#### Returns

- `list[str]` - A list of sections
