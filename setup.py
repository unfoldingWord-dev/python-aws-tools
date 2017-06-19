import os
from setuptools import setup



def read(f_name):
    """
    Utility function to read the README file.

    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()

setup(
    name='d43-aws-tools',
    version='0.0.1',
    packages=[
        'dynamodb_handler',
        's3_handler',
        'ses_handler'
    ],
    # package_data={'converters': ['templates/*.html']},
    author='unfoldingWord',
    author_email='info@unfoldingword.org',
    description='Classes for accessing AWS APIs',
    license='MIT',
    keywords=[
        'aws tools',
        'unfoldingword',
        'lambda'
    ],
    url='https://github.org/unfoldingWord-dev/python-aws-tools',
    long_description=read('README.rst'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'requests==2.13.0',
        'responses==0.5.1',
        'gogs_client==1.0.3',
        'bs4==0.0.1',
        'boto3==1.4.4',
        'python-json-logger==0.1.5',
        'markdown==2.6.8',
        'future==0.16.0',
        'pyparsing==2.1.10',
        'usfm-tools==0.0.11',
        'PyYAML==3.12'
    ]
)
