"""${project.title}"""

from distutils.version import LooseVersion

import pkg_resources


__all__ = ['__version__']

__version__ = LooseVersion(
    pkg_resources.require('${project.base}')[0].version)
