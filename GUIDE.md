## How to create a module executable from cmd line

This is the tree flow:
repository
    |__ README
    |__ setup.py (needed to create all the stuff)
    |__ License
    |__ script.py
    |__ bin
        |__ symbolink to the script.pyp
    |__ test
        |__ some tests


We must create all the file we have to upload to on pypi. 
The following command create the dist directory

python setup.py sdist 

then, we upload the module to pypi with twine

python -m twine upload --skip-existing -u GNicola -p 'jZtL02!6mn@' --repository-url https://test.pypi.org/legacy/ dist/*