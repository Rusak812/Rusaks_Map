from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='Demographics_dynamics',
    version='0.0.1',
    author='Akmetdinov Ruslan',
    author_email='rusak812@gmail.com',
    description='Demographics dynamics',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://phys.msu.ru',
    license='SCR',
    packages=find_packages(),
    # If all your code are in a module, use py_modules instead of packages:
    # py_modules=['ser'],
    scripts=['Demographics_dynamics.py'],
    test_suite='test',
    entry_points={'console_scripts':['ph_interp = Demographics_dynamics:with_args']}, # this is the last one
    install_requires=['numpy>=1.13', 'matplotlib>=2.0', 'scipy>=1.3'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: SCR License',
        'Topic :: Education',
        'Programming Language :: Python :: 3',
        # See full list on https://pypi.org/classifiers/
    ],
    keywords='sample science astrophysics',
)
