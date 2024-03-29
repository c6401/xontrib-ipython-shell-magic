#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-ipython-shell-magic',
    version='0.1.0',
    license='MIT',
    author='Xonsh IPython shell magic',
    author_email='nc6401@gmail.com',
    description="Adds IPython like shell execution magic.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh', 'ipython==7.23.1'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/c6401/xontrib-ipython-shell-magic',
    project_urls={
        "Documentation": "https://github.com/c6401/xontrib-ipython-shell-magic/blob/master/README.md",
        "Code": "https://github.com/c6401/xontrib-ipython-shell-magic",
        "Issue tracker": "https://github.com/c6401/xontrib-ipython-shell-magic/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
