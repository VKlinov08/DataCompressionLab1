import io
from src.nure.HuffmanVSArithmetics.core.tests import test_huffman_compression
from src.nure.HuffmanVSArithmetics.core.tests import test_arithmetic_compression

INPUT_FILE_PATH = r'D:\PYTHON\PyWorkspace\DataCompressionLab1\recources\input_message.txt'
INPUT_FILE_PATH2 = r'D:\PYTHON\PyWorkspace\DataCompressionLab1\recources\ascii_message.txt'
INPUT_FILE_PATH3 = r'D:\PYTHON\PyWorkspace\DataCompressionLab1\recources\input_message_2.txt'


if __name__ == '__main__':
    current_path = input('Input path to text file:\n>>> ')
    input_path = current_path if current_path != '' else INPUT_FILE_PATH
    current_encoding = input('Input encoding: ')
    current_encoding = current_encoding if current_encoding != '' else 'utf-8'
    with io.open(input_path, 'r', encoding=current_encoding) as file:
        message = ''.join(file.readlines())

    test_huffman_compression(message, input_path)
    test_arithmetic_compression(message, input_path, precision=800)


