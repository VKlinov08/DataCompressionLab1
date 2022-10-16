import sys
import io
from src.nure.HuffmanVSArithmetics.core.tests import test_huffman_compression
from src.nure.HuffmanVSArithmetics.core.tests import test_arithmetic_compression
from src.nure.HuffmanVSArithmetics.core.tests import test_both

INPUT_FILE_PATH = r'D:\PYTHON\PyWorkspace\DataCompressionLab1\recources\input_message.txt'
INPUT_FILE_PATH2 = r'D:\PYTHON\PyWorkspace\DataCompressionLab1\recources\ascii_message.txt'
INPUT_FILE_PATH3 = r'D:\PYTHON\PyWorkspace\DataCompressionLab1\recources\input_message_2.txt'


if __name__ == '__main__':
    # current_encoding = input('Input encoding: ')
    # with io.open(INPUT_FILE_PATH2, 'r', encoding=current_encoding) as file:
    #     message = ''.join(file.readlines())

    test_both()
    # test_huffman_compression(message, INPUT_FILE_PATH2)
    # test_arithmetic_compression(message)
