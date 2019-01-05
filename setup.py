# -*- coding: utf-8 -*-

from setuptools import setup, Command
import os
import sys
from shutil import rmtree

here = os.path.abspath(os.path.dirname(__file__))

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(name='weather-api',
      version='1.0.7',
      description='A Python Wrapper for the Yahoo Weather API.',
      entry_points={
          "console_scripts": ['weather = weather.main:main']
      },
      long_description=long_descr,
      url='https://github.com/AnthonyBloomer/weather-api',
      author='Anthony Bloomer',
      keywords=['weather', 'api'],
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['weather', 'weather.objects', 'weather.helpers'],
      install_requires=[
          'requests',
          'ptable',
          'colorize'
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      cmdclass={
          'publish': PublishCommand,
      },
      zip_safe=False)
