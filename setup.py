from setuptools import setup

setup(name='tidyverse',
      version=0.1,
      description='convenience package importing standard packages',
      url='http://github.com/redst4r/pytidyverse/',
      author='redst4r',
      maintainer='redst4r',
      maintainer_email='redst4r@web.de',
      license='BSD 2-Clause License',
      keywords='',
      packages=['tidyverse'],
      install_requires=[
          'numpy',
          'pandas',
          'seaborn',
          'toolz',
          'tqdm',
          'matplotlib',
          'plotnine',
          ],
      zip_safe=False)
