import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid >= 1.9',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_retry',
    'SQLAlchemy>=1.0',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'wtforms==2.1',
    'webhelpers2==2.0',
    'paginate==0.5.6',
    'paginate_sqlalchemy==0.2.0'
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='simple_blog',
    version='0.0',
    description='Simple Blog',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = simple_blog:main',
        ],
        'console_scripts': [
            'initialize_simple_blog_db = simple_blog.scripts.initializedb:main',
        ],
    },
)
