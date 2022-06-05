from setuptools import setup

setup(
    name='remotePyDuino',
    version='0.1.0',
    description='A python package to control arduino serially',
    url='https://github.com/IronLung127/SuperRemoteArduino',
    author='IronLung',
    packages=['remotePyDuino'],
    install_requires=['pySerial>=3.5'],
)