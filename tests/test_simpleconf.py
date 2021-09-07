import argparse
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)

sys.path.insert(0, str(Path(THISDIR).parent))

from fhconfparser import FHConfParser, SimpleConf

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument(
	"--format",
	"-f",
	help=f"Output format. one of: . default=simple",
)
parser.add_argument(
	"--file",
	"-o",
	help="Filename to write to (omit for stdout)",
)
parser.add_argument(
	"--using",
	"-u",
	help=f"Environment to use e.g. requirements.txt. one of: . default=poetry",
)
parser.add_argument(
	"--ignore-packages",
	help="a list of packages to ignore (compat=True)",
	nargs="+",
)
parser.add_argument(
	"--fail-packages",
	help="a list of packages to fail (compat=False)",
	nargs="+",
)
parser.add_argument(
	"--ignore-licenses",
	help="a list of licenses to ignore (skipped, compat may still be False)",
	nargs="+",
)
parser.add_argument(
	"--fail-licenses",
	help="a list of licenses to fail (compat=False)",
	nargs="+",
)
parser.add_argument(
	"--zero",
	"-0",
	help="Return non zero exit code if an incompatible license is found",
	action="store_true",
)
args = vars(parser.parse_args())

print(args)

# ConfigParser (Parses in the following order: `pyproject.toml`, `setup.cfg`
configparser = FHConfParser()
configparser.parseConfigList(
	[("pyproject.toml", "toml"), ("setup.cfg", "ini")],
	["tool"],
	["tool"],
)

sc = SimpleConf(configparser, "licensecheck", args)

print(sc.get("zero", False))  # Provide the actual default here (used if not provided
# from the command line or through a config file)
print(sc.get("fail_packages", []))
