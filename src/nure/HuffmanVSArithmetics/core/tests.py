from sys import getsizeof
from decimal import Decimal
from bitarray import bitarray
from src.nure.HuffmanVSArithmetics.core.classes.huffman import HuffmanCompress
from src.nure.HuffmanVSArithmetics.core.classes.arithmetic_compress import ArithmeticCompress
from src.nure.HuffmanVSArithmetics.utils import beautiful_print
from src.nure.HuffmanVSArithmetics.utils import decimal_to_bin_file

def info(message_name: str, message):
    print(f"{message_name} has capacity = {getsizeof(message)} bytes (in Python)")


def test_huffman_compression(message, FILE_PATH):
    beautiful_print("Huffman Algorithm")

    info("Input message", message)
    huffman_compressor = HuffmanCompress(message)
    encoded_message: bitarray = huffman_compressor.encode_message()
    info("Encoded message", encoded_message)

    # Write encoded message to a file and retrieve it for a checking
    with open(FILE_PATH[:-4] + "_huffman_code.bin", 'wb') as output:
        encoded_message.tofile(output)
    with open(FILE_PATH[:-4] + "_huffman_code.bin", 'rb') as encoded_file:
        encoded_message_from_file = bitarray()
        encoded_message_from_file.fromfile(encoded_file)

    info("\nEncoded message from file", encoded_message_from_file)
    decoded_message = huffman_compressor.decode_message(encoded_message_from_file)
    print("Decoded message content:\n\"")
    print(decoded_message, end="\"\n")
    info("\nDecoded message", decoded_message)

    print(f"Compression coefficient = {getsizeof(message)/getsizeof(encoded_message)}")
    pass


def test_arithmetic_compression(message, FILE_PATH=None, precision=50):
    beautiful_print("Arithmetic Compression")

    info("Input message", message)
    arithmetic_compressor = ArithmeticCompress(message, precision)
    encoded_message: Decimal = arithmetic_compressor.encode_message()
    info("Encoded message", encoded_message)

    # Save variable to a file
    path = FILE_PATH[:-4] + "_arithmetic_code.txt" if FILE_PATH else "arithmetic_code.txt"
    with open(path, 'w') as output:
        output.write(encoded_message.to_eng_string())
    # Read variable from a file
    with open(path, 'r') as from_file:
        encoded_message_from_file = from_file.read()

    encoded_message_decimal = Decimal(encoded_message_from_file)
    info("\nEncoded message from file", encoded_message_decimal)

    decoded_message = arithmetic_compressor.decode_message(encoded_message_decimal, len(message))
    print("Decoded message content:\n\"")
    print(decoded_message, end="\"\n")
    info("\nDecoded message", decoded_message)
    print(f"Compression coefficient = {getsizeof(message) / getsizeof(encoded_message_decimal)}")


def test_both(precision=24):
    message = 'Абракадабра'

    beautiful_print("Huffman Algorithm")
    info("Input message", message)
    huffman_compressor = HuffmanCompress(message)
    encoded_message: bitarray = huffman_compressor.encode_message( )
    info("Encoded message", encoded_message)

    decoded_message = huffman_compressor.decode_message(encoded_message)
    print("Decoded message content:\n\"")
    print(decoded_message, end="\"\n")
    info("\nDecoded message", decoded_message)

    print(encoded_message == decoded_message)
    print(f"Huffman algorithm's compression coefficient = {getsizeof(message) / getsizeof(encoded_message)}")
    # -------------------------------------------------------------------------------
    beautiful_print("Arithmetic Compression")
    info("Input message", message)
    arithmetic_compressor = ArithmeticCompress(message, precision=precision)
    encoded_message: Decimal = arithmetic_compressor.encode_message()
    print(encoded_message)
    info("Encoded message", encoded_message)

    decoded_message = arithmetic_compressor.decode_message(encoded_message, len(message))
    print("Decoded message content:\n\"")
    print(decoded_message, end="\"\n")
    info("\nDecoded message", decoded_message)

    print(encoded_message == decoded_message)
    print(f"Arithmetic compression algorithm's compression coefficient = {getsizeof(message) / getsizeof(encoded_message)}")


def test_binary_saving(message, path:str, precision=24, encoding='ascii'):
    arithmetic_compressor = ArithmeticCompress(message, precision)
    encoded_message: Decimal = arithmetic_compressor.encode_message( )
    # var to .bin file
    decimal_to_bin_file(encoded_message, path, encoding)

    # Read variable from a file
    with open(path, 'rb') as input_binary:
        bitarray_from_file = bitarray()
        bitarray_from_file.fromfile(input_binary)

    # bitarray to bytearray by encoding
    dec_bytearray_message = bitarray_from_file.tobytes()
    # bytearray to str by encoding
    dec_str_message = dec_bytearray_message.decode(encoding)
    print(dec_str_message)
