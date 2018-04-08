from setuptools import setup

setup(
    name='pycgp',
    version='0.2',
    description='CGP library',
    author='Jaroslav Loebl',
    author_email='jaroslavloebl@gmail.com',
    packages=['pycgp'],
    package_data={'pycgp': ['benchmarks/*.txt', 
        'benchmarks/bin_class_data',
        'benchmarks/bin_class_X_train',
        'benchmarks/bin_class_X_test',
        'benchmarks/bin_class_y_train',
        'benchmarks/bin_class_y_test']}
)
