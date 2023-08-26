from setuptools import setup

setup(
    name='mangroves',
    version='1.0.1',
    packages=['mangroves'],
    install_requires=[
        'torch>=1.8.1',
    ],
    author='Subhransu S. Bhattacharjee',
    author_email='Subhransu.Bhattacharjee@anu.edu.au',
    description='A Dynamic Data Management system for Advanced AI Applications',
    long_description='For the full documentation and installation instructions, please visit the GitHub page: https://github.com/1ssb/mangroves',
    url='https://github.com/1ssb/mangroves',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
