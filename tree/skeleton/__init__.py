"""${project.title}"""


from distutils.version import LooseVersion

import pkg_resources

__all__ = ["PACKAGE", "__version__"]

PACKAGE = pkg_resources.get_distribution("${project.base}")

__version__ = LooseVersion(PACKAGE.version)
