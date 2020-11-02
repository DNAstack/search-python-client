from setuptools import find_packages, setup


setup(
    name='covidcloud_search',
    packages=find_packages(include=['covidcloud_search']),
    version='0.1.1',
    description='DNAstack CovidCloud Search Library',
    author='Ayman A',
    license='MIT',
    install_requires=['requests==2.22.0'],
    test_suite='tests',
)
