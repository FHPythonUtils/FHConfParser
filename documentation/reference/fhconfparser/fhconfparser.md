# FHConfParser

[Fhconfparser Index](../README.md#fhconfparser-index) / [Fhconfparser](./index.md#fhconfparser) / FHConfParser

> Auto-generated documentation for [fhconfparser.fhconfparser](../../../fhconfparser/fhconfparser.py) module.

- [FHConfParser](#fhconfparser)
  - [FHConfParser](#fhconfparser-1)
    - [FHConfParser().defaults](#fhconfparser()defaults)
    - [FHConfParser().get](#fhconfparser()get)
    - [FHConfParser().getbool](#fhconfparser()getbool)
    - [FHConfParser().getfloat](#fhconfparser()getfloat)
    - [FHConfParser().getint](#fhconfparser()getint)
    - [FHConfParser().getstr](#fhconfparser()getstr)
    - [FHConfParser().hasOption](#fhconfparser()hasoption)
    - [FHConfParser().hasSection](#fhconfparser()hassection)
    - [FHConfParser().options](#fhconfparser()options)
    - [FHConfParser().parseConfigList](#fhconfparser()parseconfiglist)
    - [FHConfParser().parseIni](#fhconfparser()parseini)
    - [FHConfParser().parseJson](#fhconfparser()parsejson)
    - [FHConfParser().parseToml](#fhconfparser()parsetoml)
    - [FHConfParser().sections](#fhconfparser()sections)
  - [_cast](#_cast)
  - [_resolveNamespace](#_resolvenamespace)

## FHConfParser

[Show source in fhconfparser.py:27](../../../fhconfparser/fhconfparser.py#L27)

FHConfParser.

Returns
-------
 FHConfParser: parser object.
 - Call `parseConfigList` to parse files
 - Call `data` to access the internal rep

#### Signature

```python
class FHConfParser: ...
```

### FHConfParser().defaults

[Show source in fhconfparser.py:237](../../../fhconfparser/fhconfparser.py#L237)

Return a dictionary containing the defaults.

Returns
-------
 list[str]: A dictionary containing the defaults

#### Signature

```python
def defaults(self) -> dict[str, Any]: ...
```

### FHConfParser().get

[Show source in fhconfparser.py:268](../../../fhconfparser/fhconfparser.py#L268)

Get a value from section.option with some fallback for if it doesn't exist.

#### Arguments

----
 - `section` *str* - the specified section
 - `option` *str* - the specified key/ option
 - `fallback` *Any, optional* - the fallback value for if it doesn't exist.
 Defaults to None.

#### Returns

-------
 - `Any` - the value at section.option or fallback

#### Signature

```python
def get(self, section: str | None, option: str, fallback: Any = None) -> Any: ...
```

### FHConfParser().getbool

[Show source in fhconfparser.py:328](../../../fhconfparser/fhconfparser.py#L328)

Get a value from section.option with some fallback for if it doesn't exist as an bool.

#### Arguments

----
 - `section` *str* - the specified section
 - `option` *str* - the specified key/ option
 - `fallback` *Any, optional* - the fallback value for if it doesn't exist.
 Defaults to None.
 - `strict` *bool* - raise an error if the cast fails when true, else return
 the value un-casted. Defaults to True

#### Returns

-------
 - `bool` - the value at section.option or fallback (Any if strict=False)

#### Signature

```python
def getbool(
    self, section: str | None, option: str, fallback: Any = None, strict: bool = True
) -> bool: ...
```

### FHConfParser().getfloat

[Show source in fhconfparser.py:308](../../../fhconfparser/fhconfparser.py#L308)

Get a value from section.option with some fallback for if it doesn't exist as an float.

#### Arguments

----
 - `section` *str* - the specified section
 - `option` *str* - the specified key/ option
 - `fallback` *Any, optional* - the fallback value for if it doesn't exist.
 Defaults to None.
 - `strict` *bool* - raise an error if the cast fails when true, else return
 the value un-casted. Defaults to True

#### Returns

-------
 - `float` - the value at section.option or fallback (Any if strict=False)

#### Signature

```python
def getfloat(
    self, section: str | None, option: str, fallback: Any = None, strict: bool = True
) -> float: ...
```

### FHConfParser().getint

[Show source in fhconfparser.py:288](../../../fhconfparser/fhconfparser.py#L288)

Get a value from section.option with some fallback for if it doesn't exist as an int.

#### Arguments

----
 - `section` *str* - the specified section
 - `option` *str* - the specified key/ option
 - `fallback` *Any, optional* - the fallback value for if it doesn't exist.
 Defaults to None.
 - `strict` *bool* - raise an error if the cast fails when true, else return
 the value un-casted. Defaults to True

#### Returns

-------
 - `int` - the value at section.option or fallback (Any if strict=False)

#### Signature

```python
def getint(
    self, section: str | None, option: str, fallback: Any = None, strict: bool = True
) -> int: ...
```

### FHConfParser().getstr

[Show source in fhconfparser.py:348](../../../fhconfparser/fhconfparser.py#L348)

Get a value from section.option with some fallback for if it doesn't exist as an str.

#### Arguments

----
 - `section` *str* - the specified section
 - `option` *str* - the specified key/ option
 - `fallback` *Any, optional* - the fallback value for if it doesn't exist.
 Defaults to None.
 - `strict` *bool* - raise an error if the cast fails when true, else return
 the value un-casted. Defaults to True

#### Returns

-------
 - `str` - the value at section.option or fallback (Any if strict=False)

#### Signature

```python
def getstr(
    self, section: str | None, option: str, fallback: Any = None, strict: bool = True
) -> str: ...
```

### FHConfParser().hasOption

[Show source in fhconfparser.py:223](../../../fhconfparser/fhconfparser.py#L223)

Return True if the option present in the data rep (under a given section.

#### Arguments

----
 - `section` *str* - section to get
 - `option` *str* - ... and option to get

#### Returns

-------
 - `bool` - Return True if the option present in the data rep (under a given section

#### Signature

```python
def hasOption(self, section: str | None, option: str) -> bool: ...
```

### FHConfParser().hasSection

[Show source in fhconfparser.py:210](../../../fhconfparser/fhconfparser.py#L210)

Return True if the section present in the data rep.

#### Arguments

----
 - `section` *str* - section to get

#### Returns

-------
 - `bool` - Return True if the section present in the data rep.

#### Signature

```python
def hasSection(self, section: str | None) -> bool: ...
```

### FHConfParser().options

[Show source in fhconfparser.py:255](../../../fhconfparser/fhconfparser.py#L255)

Return a list of options available in the specified section.

#### Arguments

----
 - `section` *str* - the specified section

#### Returns

-------
 - `list[str]` - list of options

#### Signature

```python
def options(self, section: str | None) -> list[str]: ...
```

### FHConfParser().parseConfigList

[Show source in fhconfparser.py:39](../../../fhconfparser/fhconfparser.py#L39)

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

----
 confList (list[tuple[str, str]]): A list of tuples of config files
 and format. e.g. [("pyproject.toml", "toml"), (".config.ini", "ini")]
 - `tomlNamespace` *list[str], optional* - table to treat as root . Defaults to None.
 - `jsonNamespace` *list[str], optional* - define root. Defaults to None.

#### Returns

-------
 - `list[str]` - list of successfully parsed files

#### Signature

```python
def parseConfigList(
    self,
    confList: list[tuple[str, str]],
    tomlNamespace: list[str] | None = None,
    jsonNamespace: list[str] | None = None,
) -> list[str]: ...
```

### FHConfParser().parseIni

[Show source in fhconfparser.py:84](../../../fhconfparser/fhconfparser.py#L84)

Parse a single ini file and update the internal rep with the new data.

#### Arguments

----
 file (str | Path): config file to parse
 - `throws` *bool* - Throw an exception if there is a parsing failure.
 Defaults to False.
 - `kwargs` - ignored

#### Raises

------
 - `ParsingError` - if throws = True

#### Returns

-------
 - `list[str]` - list of successfully parsed files

#### Signature

```python
def parseIni(
    self, file: str | Path, throws: bool = False, **kwargs: dict[str, Any]
) -> list[str]: ...
```

### FHConfParser().parseJson

[Show source in fhconfparser.py:173](../../../fhconfparser/fhconfparser.py#L173)

Parse a single json file and update the internal rep with the new data.

#### Arguments

----
 file (str | Path): config file to parse
 - `jsonNamespace` *list[str], optional* - define root. Defaults to None.
 - `throws` *bool* - Throw an exception if there is a parsing failure.
 Defaults to False.
 - `kwargs` - ignored

#### Raises

------
 - `JSONDecodeError` - if throws = True

#### Returns

-------
 - `list[str]` - list of successfully parsed files

#### Signature

```python
def parseJson(
    self,
    file: str | Path,
    jsonNamespace: list[str] | None = None,
    throws: bool = False,
    **kwargs: dict[str, Any]
) -> list[str]: ...
```

### FHConfParser().parseToml

[Show source in fhconfparser.py:136](../../../fhconfparser/fhconfparser.py#L136)

Parse a single toml file and update the internal rep with the new data.

#### Arguments

----
 file (str | Path): config file to parse
 - `tomlNamespace` *list[str], optional* - table to treat as root . Defaults to None.
 - `throws` *bool* - Throw an exception if there is a parsing failure.
 Defaults to False.
 - `kwargs` - ignored

#### Raises

------
 - `ParseError` - if throws = True

#### Returns

-------
 - `list[str]` - list of successfully parsed files

#### Signature

```python
def parseToml(
    self,
    file: str | Path,
    tomlNamespace: list[str] | None = None,
    throws: bool = False,
    **kwargs: dict[str, Any]
) -> list[str]: ...
```

### FHConfParser().sections

[Show source in fhconfparser.py:246](../../../fhconfparser/fhconfparser.py#L246)

Return a list of the sections available.

Returns
-------
 list[str]: A list of sections

#### Signature

```python
def sections(self) -> list[str]: ...
```



## _cast

[Show source in fhconfparser.py:389](../../../fhconfparser/fhconfparser.py#L389)

Handy cast function. Raises a ValueError if fails when strict=True else...

returns data unconverted.

#### Arguments

----
 - `payload` *Any* - data to convert
 castFunc (Callable[[Any], Any]): cast function eg int
 - `strict` *bool, optional* - throw error if true, otherwise return payload.
 Defaults to True.

#### Raises

------
 - `ValueError` - if the cast fails and strict=True

#### Returns

-------
 - `Any` - casted payload

#### Signature

```python
def _cast(payload: Any, castFunc: Callable[[Any], Any], strict: bool = True) -> Any: ...
```



## _resolveNamespace

[Show source in fhconfparser.py:369](../../../fhconfparser/fhconfparser.py#L369)

Take some document object and set the root to the namespace.

#### Arguments

----
 doc (dict[str, Any]): some document object dict[str, Any]
 - `namespace` *list[str], optional* - a list representing a namespace. e.g.
 ["tool", "poetry"]. Defaults to None.

#### Returns

-------
 - `dict[str,` *Any]* - resolved document

#### Signature

```python
def _resolveNamespace(
    doc: dict[str, Any], namespace: list[str] | None = None
) -> dict[str, Any]: ...
```