from __future__ import annotations

import argparse
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from fhconfparser import FHConfParser, SimpleConf

args = vars(argparse.Namespace(args=True))


def test_simpleconf():
	# ConfigParser (Parses in the following order: `pyproject.toml`, `setup.cfg`
	configparser = FHConfParser()
	assert (
		len(
			configparser.parseConfigList(
				confList=[
					(f"{THISDIR}/data/simpleconf.toml", "toml"),
					(f"{THISDIR}/data/simpleconf.cfg", "ini"),
				],
				tomlNamespace=["tool"],
				jsonNamespace=["tool"],
			)
		)
		== 2
	)

	sc = SimpleConf(configparser, "example", args)

	assert sc.get("args", False)  # Provide the actual default here (used if not provided
	# from the command line or through a config file)
	assert sc.get("toml", False)
	assert sc.get("cfg", False)
	assert sc.get("fallback", True)
