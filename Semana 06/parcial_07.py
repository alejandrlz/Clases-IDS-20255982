nombre = input()
apellido = input()

nick = nombre.lower()[:5:]+apellido.lower()[0]
pin = (len(nombre) * 1000) + len(apellido)
pin2 = pin % 10000

ID = (f"C3-{nick}-{pin2}")

print(f"Nick: {nick}")
print(f"Pin: {pin2}")
print(f"ID: {ID}")