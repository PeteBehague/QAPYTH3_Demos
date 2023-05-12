nebula = {'M42':'Orion',
          'C33':'Veil',
          'M8' :'Lagoon',
          'M17':'Swan'
}

for kv in nebula.items():
    print(kv)

print("\nNebula Keys")
lkeys = list(nebula.keys())
print(lkeys)

print("\nNebula Keys")
jelly = nebula.keys() | {'M37', 'M5'} # union of both sets of nebula
print(jelly)
