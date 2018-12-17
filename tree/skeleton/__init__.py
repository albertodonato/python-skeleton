"""${project.title}"""

from distutils.version import LooseVersion

import pkg_resources


__all__ = ['__version__']

__version__ = LooseVersion(
    pkg_resources.require('${project.name}')[0].version)
