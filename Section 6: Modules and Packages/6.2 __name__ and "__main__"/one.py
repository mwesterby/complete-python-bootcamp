# When you call `python one.py` all the code at indentation level 0 is going to get run

# When you call `python one.py` the `__name__` variable is assigned to "__main__"
# __name__ = "__main__"


def func():
    print('FUNC() IN ONE.PY')

print('TOP LEVEL IN ONE.PY')

if __name__ == "__main__":
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')