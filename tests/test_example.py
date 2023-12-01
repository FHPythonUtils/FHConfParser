from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import fhconfparser


def test_ini():
	ini = fhconfparser.FHConfParser()
	ini.parseConfigList([(f"{THISDIR}/data/example.ini", "ini")])
	assert ini.data == {"section": {"a": "b", "b": True, "c": True, "d": ["list", "of", "things"]}}
	assert ini.defaults() == {}
	assert ini.sections() == ["section"]
	assert ini.options("section") == ["a", "b", "c", "d"]
	assert ini.get("section", "a") == "b"


def test_json():
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


def test_toml():
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


def test_toml_no_section():
	toml = fhconfparser.FHConfParser()
	namespace = ["section"]
	toml.parseConfigList(
		[(f"{THISDIR}/data/example_no_section.toml", "toml")],
		namespace,
		namespace,
	)
	assert toml.data == {}
