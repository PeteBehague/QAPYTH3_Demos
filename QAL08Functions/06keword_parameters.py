def print_vat(**kwargs):
   print(kwargs)

print_vat(vatpc=15, gross=9.55, message='Summary')


argsdict = dict(vatpc=15, gross=9.55, message='Summary')
print_vat(**argsdict)


