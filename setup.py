from glob import glob
import os
from setuptools import setup, find_packages
from jupyterthemes import THEMES_PATH

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def themefiles():
    return glob('jupyterthemes/styles/*.css')

setup(
    name='jupyter-themes',
    version='0.2',
    packages=find_packages(),
    data_files=[(THEMES_PATH, themefiles())],
    include_package_data=True,
    package_data={'jupyterthemes': ['sandbox/*.js']},
    description='Select and install a Jupyter notebook theme',
    long_description=README,
    license='MIT',
    author='dunovank, miraculixx',
    author_email='dunovank@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: jupyter',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: CSS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[ 'jupyter' ],
    keywords = ['jupyter', 'ipython', 'notebook', 'themes', 'css'],
    entry_points={
        'console_scripts': [
            'jupyter-theme = jupyterthemes:main',
            'jt = jupyterthemes:main',
        ],
    }
)
