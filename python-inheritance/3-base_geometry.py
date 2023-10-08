class BaseGeometry:
    pass

base_geometry = BaseGeometry()

memory_address = hex(id(base_geometry))
formatted_memory_address = f'0x{memory_address[2:]}'

print(f'<3-3-base_geometry.BaseGeometry object at {formatted_memory_address}>')
print(dir(base_geometry))
print(dir(BaseGeometry))