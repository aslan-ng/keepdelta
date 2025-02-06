from setuptools import setup, find_packages


setup(
    name='keepdelta',
    version='1.0.0',
    description='Efficient Delta Management for Python Data Structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aslan Noorghasemi, Christopher McComb',
    author_email='aslann@cmu.edu, ccm@cmu.edu',
    url='https://github.com/aslan-ng/KeepDelta',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", 
)