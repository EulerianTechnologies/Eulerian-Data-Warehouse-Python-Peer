from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    author='Xavier THORILLON',
    author_email='x.thorillon@eulerian.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent"
    ],
    description='Request Eulerian Data Warehouse',
    download_url='https://github.com/EulerianTechnologies/Eulerian-Data-Warehouse-Python-Peer/archive/master.zip',
    install_requires=[
        'requests>=2.23.0',
        'ijson>=3.0.4'
    ],
    keywords=[
        'eulerian',
        'rest',
        'data warehouse',
        'analytics',
        'data science'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='Eulerian-Data-Warehouse-Python-Peer',
    packages=find_packages(exclude=("tests",)),
    platforms=['any'],
    python_requires='>=3.6',
    url='https://github.com/EulerianTechnologies/Eulerian-Data-Warehouse-Python-Peer',
    version='0.1',
)
