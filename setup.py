from setuptools import setup

setup(
    name = 'xlsx-to-json',
    version = '0.1.0',
    packages = ['xlsx-to-json'],
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
            'xlsx-to-json = xlsx-to-json.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)