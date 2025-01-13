from setuptools import setup, find_packages


setup(
    name='keepdelta',
    version='0.7',
    description='Efficient Delta Management for Python Data Structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aslan Noorghasemi',
    author_email='aslann@cmu.edu',
    url='https://github.com/aslan-ng/KeepDelta',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
)