import atexit
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install

# from urllib.request import urlretrieve


def post_install():
    package_files = Path.home() / ".ciawf"


class Installation(install):
    def __init__(self, *args, **kwargs):
        super(Installation, self).__init__(*args, **kwargs)
        atexit.register(post_install)


setup(
    name="ciawf",
    version="0.0.0",
    author="harttraveller.com",
    url="harttraveller.com/ciawf",
    license="MIT",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
    # entry_points={"console_scripts": ["ciawf=ciawf.cli:entry"]},
    cmdclass={
        "install": Installation,
    },
)
