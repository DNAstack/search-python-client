from setuptools import find_packages, setup


setup(
    name='search_python_client',
    packages=find_packages(include=['search_python_client']),
    version='0.1.4',
    description='DNAstack Search Library',
    author='Ayman A',
    license='MIT',
    install_requires=['requests>=2.0.0', 'pandas>=1.0.0'],
    test_suite='tests',
)
