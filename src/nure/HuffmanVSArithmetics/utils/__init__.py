from pyfiglet import Figlet
from bitarray import bitarray
from decimal import Decimal

def beautiful_print(text: str, font='standard'):
    preview = Figlet(font=font)
    rendered_text = preview.renderText(text)
    print("\033[01m\033[31m{} \033[0m" .format(rendered_text))


def decimal_to_bin_file(variable: Decimal,
                        path:str="bin_saving.bin",
                        encoding:str='ascii'):
    str_message = variable.to_eng_string( )
    # str to bytearray
    bytearray_message = str_message.encode(encoding)
    # bytearray to bitarray
    bitarray_message = bitarray()
    bitarray_message.frombytes(bytearray_message)
    # Save variable to a file
    with open(path, 'wb') as output_binary:
        bitarray_message.tofile(output_binary)
