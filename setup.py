from setuptools import find_packages
from distutils.core import setup

if __name__== '__main__':
    setup(include_package_data=True,
          description='Vibe Check',
          long_description="""Python package for exploring a vibe-based psychological theory""",
          author="Avanti Shrikumar",
          author_email="avanti.shrikumar@gmail.com",
          url='https://github.com/AvantiShri/vibecheck',
          version='0.1.0.0',
          packages=find_packages(),
          setup_requires=[],
          install_requires=['numpy', 'pandas', 'scipy', 'sklearn'],
          extras_require={},
          scripts=[],
          name='vibecheck')
