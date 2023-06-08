import base64

my_text = "Hello World"
my_text_encoded = my_text.encode("ascii")
my_text_b64 = base64.b64encode(my_text_encoded)

print(my_text_encoded)
print(my_text_b64)
