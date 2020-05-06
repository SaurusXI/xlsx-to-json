from setuptools import setup

setup(
    name = 'xlsx_to_json',
    version = '0.1.0',
    packages = ['xlsx_to_json'],
    license = 'MIT',
    description = 'Convert a single Excel sheet to JSON',
    author = 'SaurusXI',
    author_email = 'vermashantanu@hotmail.com',
    url = '',
    download_url = '',
    keywords = ['EXCEL', 'JSON', 'CONVERT'],
    install_requires=[
        'pandas'
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