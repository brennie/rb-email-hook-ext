#!/usr/bin/env python

from setuptools import find_packages

from reviewboard.extensions.packaging import setup


setup(
    name='rb-email-hook-ext',
    version='0.0.0',
    description='An extension contianing e-mail hooks for testing.',
    author='Barret Rennie',
    author_email='barret@beanbaginc.com',
    packages=find_packages(),
    entry_points={
        'reviewboard.extensions':
            'rb-email-hook-ext = rb_email_hook_ext.extension:EmailHookExt',
    },
)
