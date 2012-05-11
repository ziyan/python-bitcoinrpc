from distutils.core import setup

setup(
    name = "python-bitcoinrpc",
    version = "0.1.0",
    author = "Jeff Garzik",
    author_email = "jgarzik@github.com",
    description = "AuthServiceProxy is an improved version of python-jsonrpc.",
    #download_url = "",
    url = "https://github.com/ziyan/python-bitcoinrpc",
    packages=['jsonrpc'],
    platforms=['any'],
    classifiers=['Development Status :: 3 - Alpha',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Application Frameworks',
                'Topic :: Software Development :: Libraries :: Python Modules',
                'Topic :: Utilities'],
)
