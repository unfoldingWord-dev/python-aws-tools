from setuptools import setup

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
    author_email='unfoldingword.org',
    description='Unit test setup file.',
    keywords=[
        'aws tools',
        'unfoldingword',
        'lambda'
    ],
    url='https://github.org/unfoldingWord-dev/python-aws-tools',
    long_description='Unit test setup file',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'requests==2.13.0',
        'responses==0.5.1',
        'boto3==1.4.4',
        'bs4==0.0.1',
        'gogs_client==1.0.3',
        'coveralls==1.1',
        'python-json-logger==0.1.5',
        'markdown==2.6.8',
        'future==0.16.0',
        'pyparsing==2.1.10',
        'usfm-tools==0.0.11',
        'mock',  # travis reports syntax error in mock setup.cfg if we give version
        'moto==0.4.31',
        'PyYAML==3.12'
    ],
    test_suite='tests'
)
