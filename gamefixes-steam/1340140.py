"""DRACU-RIOT!"""

from protonfixes import util


def main() -> None:
    util.disable_protonmediaconverter()
    util.protontricks('mf')
    util.protontricks('quartz')
    util.protontricks('amstream')
    util.protontricks('wmp11')

