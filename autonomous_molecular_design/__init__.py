"""
Autonomous Molecular Design
Skeleton for testing of active learning strategies for autonomous molecular design.
"""

# Add imports here
from .autonomous_molecular_design import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
