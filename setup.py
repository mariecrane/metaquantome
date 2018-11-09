from setuptools import setup

VERSION='0.1.3b'
URL='https://github.com/caleb-easterly/metaquantome'
AUTHOR = 'Caleb Easterly'
AUTHOR_EMAIL = 'easte080@umn.edu'

setup(
    name='metaquantome',
    version=VERSION,
    packages=['metaquantome'],
    package_data={'metaquantome': ['data/*']},
    license='Apache License 2.0',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='Quantitative microbiome analysis',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[
        'pandas',
        'ete3',
        'goatools',
        'wget',
        'numpy',
        'statsmodels'
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['metaquantome=metaquantome.__main__:main'],
    },
    project_urls={
        "Bug Tracker": "https://github.com/caleb-easterly/metaquantome/issues",
        "Source Code": "https://github.com/caleb-easterly/metaquantome",
    }
)
