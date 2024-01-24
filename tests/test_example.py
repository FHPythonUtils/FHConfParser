from __future__ import annotations

import configparser
import sys
from pathlib import Path

import pytest

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import fhconfparser


def test_ini() -> None:
	ini = fhconfparser.FHConfParser()
	ini.parseConfigList([(f"{THISDIR}/data/example.ini", "ini")])
	assert ini.data == {"section": {"a": "b", "b": True, "c": True, "d": ["list", "of", "things"]}}
	assert ini.defaults() == {}
	assert ini.sections() == ["section"]
	assert ini.options("section") == ["a", "b", "c", "d"]
	assert ini.get("section", "a") == "b"


def test_json() -> None:
	json = fhconfparser.FHConfParser()
	json.parseConfigList([(f"{THISDIR}/data/example.json", "json")])
	assert json.data == {
		"a": "b",
		"b": 1,
		"c": True,
		"d": ["list", "of", "things"],
		"section": {"a": "b", "b": 1, "c": True, "d": ["list", "of", "things"]},
	}
	assert json.defaults() == {"a": "b", "b": 1, "c": True, "d": ["list", "of", "things"]}
	assert json.sections() == ["section"]
	assert json.options("section") == ["a", "b", "c", "d"]
	assert json.get("section", "a") == "b"


def test_toml() -> None:
	toml = fhconfparser.FHConfParser()
	toml.parseConfigList([(f"{THISDIR}/data/example.toml", "toml")])
	assert toml.data == {
		"a": "b",
		"b": 1,
		"c": True,
		"d": ["list", "of", "things"],
		"section": {"a": "b", "b": 1, "c": True, "d": ["list", "of", "things"]},
	}
	assert toml.defaults() == {"a": "b", "b": 1, "c": True, "d": ["list", "of", "things"]}
	assert toml.sections() == ["section"]
	assert toml.options("section") == ["a", "b", "c", "d"]
	assert toml.get("section", "a") == "b"
	assert toml.get(None, "a") == "b"


def test_toml_no_section() -> None:
	toml = fhconfparser.FHConfParser()
	namespace = ["section"]
	toml.parseConfigList(
		[(f"{THISDIR}/data/example_no_section.toml", "toml")],
		namespace,
		namespace,
	)
	assert toml.data == {}


def test_not_exists_ini() -> None:
	ini = fhconfparser.FHConfParser()
	ini.parseConfigList([(f"{THISDIR}/data/not_exists.ini", "ini")])
	assert ini.data == {}


def test_not_exists_json() -> None:
	json = fhconfparser.FHConfParser()
	json.parseConfigList([(f"{THISDIR}/data/not_exists.json", "json")])
	assert json.data == {}


def test_not_exists_toml() -> None:
	toml = fhconfparser.FHConfParser()
	toml.parseConfigList([(f"{THISDIR}/data/not_exists.toml", "toml")])
	assert toml.data == {}


def test_broken_ini() -> None:
	ini = fhconfparser.FHConfParser()
	ini.parseConfigList([(f"{THISDIR}/data/broken.ini", "ini")])
	assert ini.data == {}


def test_broken_json() -> None:
	json = fhconfparser.FHConfParser()
	json.parseConfigList([(f"{THISDIR}/data/broken.json", "json")])
	assert json.data == {}


def test_broken_toml() -> None:
	toml = fhconfparser.FHConfParser()
	toml.parseConfigList([(f"{THISDIR}/data/broken.toml", "toml")])
	assert toml.data == {}


def test_broken_throws_ini() -> None:
	ini = fhconfparser.FHConfParser()
	with pytest.raises(configparser.MissingSectionHeaderError):
		ini.parseIni(f"{THISDIR}/data/broken.ini", throws=True)
	assert ini.data == {}


def test_broken_throws_json() -> None:
	json = fhconfparser.FHConfParser()
	with pytest.raises(ValueError):
		json.parseJson(f"{THISDIR}/data/broken.json", throws=True)
	assert json.data == {}


def test_broken_throws_toml() -> None:
	toml = fhconfparser.FHConfParser()
	with pytest.raises(ValueError):
		toml.parseToml(f"{THISDIR}/data/broken.toml", throws=True)
	assert toml.data == {}


def test_get() -> None:
	ini = fhconfparser.FHConfParser()
	ini.parseConfigList([(f"{THISDIR}/data/example.ini", "ini")])

	assert ini.getfloat("section", "a", strict=False) == "b"
	assert ini.getint("section", "a", strict=False) == "b"
	assert ini.getbool("section", "a", strict=False)
	assert ini.getstr("section", "a") == "b"


def test_strict_get() -> None:
	ini = fhconfparser.FHConfParser()
	ini.parseConfigList([(f"{THISDIR}/data/example.ini", "ini")])

	with pytest.raises(ValueError):
		ini.getfloat("section", "a", strict=True)

	with pytest.raises(ValueError):
		ini.getint("section", "a", strict=True)

	assert ini.getbool("section", "a", strict=True)
	assert ini.getstr("section", "a") == "b"
