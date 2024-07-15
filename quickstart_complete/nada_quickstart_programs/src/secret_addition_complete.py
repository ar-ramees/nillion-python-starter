from nada_dsl import *
def nada_main():

    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))

    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    multiply_value = my_int1 + my_int2

    geometric_mean = product ** (1 / 2)

    new_int = geometric_mean

    return [Output(new_int, "my_output", party1)]