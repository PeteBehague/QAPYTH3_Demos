i = int("42")
i += 1
print(i)

s = str(42)

name = "Fred Quimby"
print(len(name))
print(name.lower())

new_name = name.replace("Qu", "Fr")
print(new_name)

first_name_with_trailing_space = "Tom        "
last_name_with_trailing_space = "Waits        "

print(first_name_with_trailing_space.rstrip(), last_name_with_trailing_space.rstrip(), ".")

pos = name.find("Qu")
print(pos)

pos = name.find("Zu")
print(pos)

print(name * 4)
