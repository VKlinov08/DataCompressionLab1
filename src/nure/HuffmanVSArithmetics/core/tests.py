from sys import getsizeof
from bitarray import bitarray
from src.nure.HuffmanVSArithmetics.core.classes.huffman import HuffmanCompress
from src.nure.HuffmanVSArithmetics.core.classes.arithmetic_compress import ArithmeticCompress
from src.nure.HuffmanVSArithmetics.utils import beautiful_print
from decimal import Decimal

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
    # assert encoded_message == encoded_message_from_file

    decoded_message = huffman_compressor.decode_message(encoded_message_from_file)
    print("Decoded message content:\n\"")
    print(decoded_message, end="\"\n")
    info("\nDecoded message", decoded_message)

    print(f"Compression coefficient = {getsizeof(message)/getsizeof(encoded_message)}")
    pass


def test_arithmetic_compression(message):
    beautiful_print("Arithmetic Compression")

    info("Input message", message)
    arithmetic_compressor = ArithmeticCompress(message)
    encoded_message: Decimal = arithmetic_compressor.encode_message()
    print(encoded_message)
    info("Encoded message", encoded_message)

    decoded_message = arithmetic_compressor.decode_message(encoded_message, len(message))
    print("Decoded message content:\n\"")
    print(decoded_message, end="\"\n")
    info("\nDecoded message", decoded_message)

    print(f"Compression coefficient = {getsizeof(message) / getsizeof(encoded_message)}")


def test_both():
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
    arithmetic_compressor = ArithmeticCompress(message, precision=24)
    encoded_message: Decimal = arithmetic_compressor.encode_message()
    print(encoded_message)
    info("Encoded message", encoded_message)

    decoded_message = arithmetic_compressor.decode_message(encoded_message, len(message))
    print("Decoded message content:\n\"")
    print(decoded_message, end="\"\n")
    info("\nDecoded message", decoded_message)

    print(encoded_message == decoded_message)
    print(f"Arithmetic compression algorithm's compression coefficient = {getsizeof(message) / getsizeof(encoded_message)}")



