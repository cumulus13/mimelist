from setuptools import setup, find_packages
import __version__
version = __version__.version
setup(
    name = 'mimelist',
    version = version,
    author = 'Hadi Cahyadi LD',
    author_email = 'cumulus13@gmail.com',
    description = ('Get type mime or ext from mime text'),
    license = 'MIT',
    keywords = "mime extention mimetype",
    url = 'https://github.com/cumulus13/mimelist',
    scripts = [],
    py_modules = ['mimelist'],
    packages = find_packages(),
    download_url = 'https://github.com/cumulus13/mimelist/tarball/master',
    install_requires=[
        'argparse'
    ],
    # TODO
    #entry_points={
    #    "console_scripts": ["drawille=drawille:__main__"]
    #},
    entry_points = {
         "console_scripts": ["mimelist = mimelist:usage",]
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10-dev',
    ],
)
