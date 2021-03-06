# Authors: Denis Engemann <d.engemann@fz-juelich.de>
#
# License: BSD (3-clause)

from . import utils  # noqa
from .edf._raw import RawEDF  # noqa
Raw = RawEDF  # noqa
from .hd5._raw import RawHD5  # noqa
from .epochs import Epochs  # noqa
from . import viz  # noqa

__version__ = '0.2.0.dev0'
