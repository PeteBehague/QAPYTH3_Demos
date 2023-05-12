# Multi-byte characters
# \unnnn for a two-byte Unicode character
# \Unnnnnnnn for a four-byte Unicode character
# \N{name} for a named Unicode character


euro = "\u20ac"
print(euro)

euro = "\N{dollar sign}"
print(euro)


chars_as_bytes = b"single-byte string"
chars_as_string = "character string"
print(chars_as_bytes)
print(chars_as_string)
