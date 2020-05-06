from setuptools import setup

setup(
    name = 'xlsx_to_json',
    version = '0.1.2',
    packages = ['xlsx_to_json'],
    license = 'MIT',
    description = 'Convert a single Excel sheet to JSON',
    author = 'SaurusXI',
    author_email = 'vermashantanu@hotmail.com',
    url = 'https://github.com/SaurusXI/xlsx-to-json',
    download_url = 'https://github.com/SaurusXI/xlsx-to-json/archive/0.1.2.tar.gz',
    keywords = ['EXCEL', 'JSON', 'CONVERT'],
    install_requires=[
        'pandas',
        'xlrd>=1.0.0'
    ],
    entry_points = {
        'console_scripts': [
            'xlsx_to_json = xlsx_to_json.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)