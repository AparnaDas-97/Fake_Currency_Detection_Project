import os
def fake(u):
    exists = os.path.isfile(u)
    print u
    if 'fake' in u:
        return 1
    else:
        return 0
