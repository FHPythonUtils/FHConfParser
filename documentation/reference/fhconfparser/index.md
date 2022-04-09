# Fhconfparser

> Auto-generated documentation for [fhconfparser](../../../fhconfparser/__init__.py) module.

Provides a config language independent way to read a config file.

- [Fhconfparser](../README.md#fhconfparser-index) / [Modules](../MODULES.md#fhconfparser-modules) / Fhconfparser
    - [Currently supports](#currently-supports)
    - Modules
        - [FHConfParser](fhconfparser.md#fhconfparser)
        - [SimpleConf](simpleconf.md#simpleconf)

## Rationale for project
For instance toml and ini syntax is very similar but not identical. Currently, tools such as
pylint must implement custom ways to deal with this. Hopefully this code
streamlines that a bit.

## Currently supports

- Ini
- Toml
- Json
