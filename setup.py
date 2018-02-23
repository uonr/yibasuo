from setuptools import setup

setup(
    name='yibasuo',
    version='1.0-alpha',
    description='A script to generate GIF-like video for Telegram/Twitter/etc.',
    url='https://github.com/quanbrew/yibasuo',
    author='Quan Brew',
    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Video',
        'Programming Language :: Python :: 3.2',
    ],
    scripts=['yibasuo.py'],
)