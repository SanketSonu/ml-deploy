# All the folder will have __init__.py file so that that internal folder will also behave like a package.
# If we want this SRC can be found as a package so we need this file.
# Whenever setup.py is running --> find_packages() function will try to find "In how many folders __init__.py is there".
# So, it will directly consider this SRC as a package and it will try to build it.
# Once it builds we can import it anywhere whenever we want to use it, just like we import -> pandas, munpy, seaborn etc. (For that we have to put it in Pypi package.)