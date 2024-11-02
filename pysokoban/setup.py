from setuptools import setup, find_packages

setup(
    name='pysokoban',
    version='1.1',
    license='BSD',
    author='Nilangshu Mondal',
    author_email='nilangshumondal4@gmail.com',
    url='https://github.com/Nilangshu98',
    long_description=open("Nil.fast").read(),
    packages=find_packages(),
    include_package_data=True,
    package_data={'' : ['*.gif', '*.skb']},
    description="A highly customizable sokoban implementation using Python's tkinter.",
    entry_points = {
        'console_scripts': ['pysokoban=pysokoban.sokoban:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Games/Entertainment :: Puzzle Games',
        ],
)

