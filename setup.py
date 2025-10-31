# from distutils.core import setup
from setuptools import setup

_dependencies = [
    'numpy<=1.16.1,>=1.14.5',
    'scipy<=1.3.3,>=1.1.0',
    'scikit-learn>=0.21.3,<=1.5.0',
    'matplotlib==3.1.2',
    'Keras==3.12.0',
    'seaborn<=0.11.0,>=0.9.0',
    'tqdm>=4.35.0,<=4.66.3',
    'pyparsing<=2.4.7,>=2.4.2'
]

setup(
    name='cade',
    version='1.0',
    description='CADE: A library for detecting drifting sample using contrastive autoencoder.',
    maintainer='Limin Yang',
    maintainer_email='liminy2@illinois.edu',
    url='https://github.com/whyisyoung/CADE',
    packages=['cade'],
    setup_requires=_dependencies,
    install_requires=_dependencies,
    extras_require={
        "tf": ["tensorflow==2.12.1"],
        "tf_gpu": ["tensorflow-gpu==1.12.0"],
    }
)
