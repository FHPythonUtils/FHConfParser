import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import fhconfparser

print("INI")
ini = fhconfparser.FHConfParser()
ini.parseConfigList([(f"{THISDIR}/example.ini", "ini")])
print(ini.data)
print(ini.defaults())
print(ini.sections())
print(ini.options("section"))
print(ini.get("section", "a"))


print("JSON")
json = fhconfparser.FHConfParser()
json.parseConfigList([(f"{THISDIR}/example.json", "json")])
print(json.data)
print(json.defaults())
print(json.sections())
print(json.options("section"))
print(json.get("section", "a"))

print("TOML")
toml = fhconfparser.FHConfParser()
toml.parseConfigList([(f"{THISDIR}/example.toml", "toml")])
print(toml.data)
print(toml.defaults())
print(toml.sections())
print(toml.options("section"))
print(toml.get("section", "a"))
