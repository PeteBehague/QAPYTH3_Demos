import argparse

prs = argparse.ArgumentParser()
prs.add_argument('-c', action="store_true", default=False)
prs.add_argument('-f', type=open)
prs.add_argument('-u', action="store", dest="user")
prs.add_argument('posargs', default=[], nargs="*")
try:
    nsp = prs.parse_args()
except (FileNotFoundError, PermissionError) as err:
    prs.error(str(err))
print(nsp)
