# Unlimited positional arguments
def add(*args):
    print(args[0])
    print(args)


add(1,2,3)

print("=== **kwargs ===")
# Unlimited key value arguments
def calculate(**kwargs):
    # print(kwargs.get('a')) => if the key doesn't exist return None
    # print(kwargs)
    for key,value in kwargs.items():
        print(f"key: {key}")
        print(f"value: {value}")

    print(kwargs["a"])


calculate(a=1,b=2,c=3)