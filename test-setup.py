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
        'coveralls==1.1',
        'boto3==1.4.4',
        'moto==0.4.31'
        'mock',  # travis reports syntax error in mock setup.cfg if we give version
    ],
    test_suite='tests'
)
