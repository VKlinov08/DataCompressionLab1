# Lossless Text Compression

This project implements two popular lossless data compression algorithms: **Huffman Coding** and **Arithmetic Coding**. Both algorithms are used for compressing text messages and allow reducing the size of the text while preserving all the original information.

## Algorithms

1. **Huffman Coding**:
    - A lossless data compression algorithm that builds an optimal binary tree for encoding symbols. Symbols that appear more frequently in the message are encoded with shorter codes, while less frequent symbols are encoded with longer codes.
    
2. **Arithmetic Coding**:
    - A more advanced compression method that represents the entire text as a fraction. This allows achieving higher compression ratios than Huffman coding, especially for messages with high symbol repetition.
