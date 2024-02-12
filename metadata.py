"""
To check versions as all packages

"""

from importlib import metadata

print(metadata.version('pip'))  # 23.3.2

metadata_pip = metadata.metadata('pip')

print(list(metadata_pip))

print(metadata_pip['Project-URL'])

print(len(metadata.files('pip')))
