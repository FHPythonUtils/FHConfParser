# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2023 - 2023/12/01

- fix: crash when a namespace doesn't exist https://github.com/FHPythonUtils/LicenseCheck/issues/65

## 2022 - 2022/01/27

- Update deps
- Add formal tests
- Use tomli in place of tomlkit (for parse speed improvements)
- Bugfixes

## 2021.1.2 - 2021/10/14

- Use pre-commit to enforce reasonable standards + consistency
- Update readme with improved docs on installing and running python (fairly generic)
- Remove classifiers for license + python versions and rely on poetry to generate these
- Update tooling config (pyproject.toml)

## 2021.1 - 2021/09/07

- Add `SimpleConf` to enable a user to extend the capabilities of FHConfParser
	such that command-line arguments can be used to override config options.

## 2021 - 2021/08/21

- First release
