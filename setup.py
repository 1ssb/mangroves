from setuptools import setup, find_packages

setup(
    name='mangroves',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'torch>=1.8.1',
    ],
    author='Subhransu S. Bhattacharjee',
    author_email='your.email@example.com',
    description='A Dynamic Data Management Engine for Advanced AI Applications',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/1ssb/mangroves',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
