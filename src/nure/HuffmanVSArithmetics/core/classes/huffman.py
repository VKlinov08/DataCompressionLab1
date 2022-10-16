from bitarray import bitarray
import heapq
from collections import Counter
from typing import Optional, Any


class Node:
    __slots__ = ["frequency", "chars", "left", "right"]

    frequency: int
    chars: Optional[str]
    left: Optional[Any]
    right: Optional[Any]

    def __init__(self, frequency=0, chars=None, left=None, right=None):
        self.frequency = frequency
        self.chars = chars
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __add__(self, other):
        sum_frequency = self.frequency + other.frequency
        return Node(sum_frequency, left=self, right=other)


def build_huffman_tree(node_queue: heapq) -> Node:
    while len(node_queue) > 1:
        left = heapq.heappop(node_queue)
        right = heapq.heappop(node_queue)
        composite_node = left + right
        heapq.heappush(node_queue, composite_node)
    return heapq.heappop(node_queue)


class HuffmanCompress:
    __slots__ = ["__message", "encoded_message", "huffman_tree"]

    __message: str
    encoded_message: Optional[bitarray]
    huffman_tree: Optional[Node]

    def __init__(self, message):
        self.__message = message
        self.encoded_message = None
        self.huffman_tree = None

    def set_message(self, new_message):
        self.__message = new_message
        self.encoded_message = None
        self.huffman_tree = None

    def get_codes(self) -> dict:
        if self.huffman_tree is None:
            raise AttributeError("Huffman tree was not initialized!")

        result = {}

        def traverse(node: Node, prefix=bitarray()):
            if node.chars is not None:
                result[node.chars] = prefix
            else:
                traverse(node.left, prefix + bitarray([0]))
                traverse(node.right, prefix + bitarray([1]))

        traverse(self.huffman_tree)
        return result

    def encode_message(self) -> bitarray:
        if self.encoded_message is not None:
            return self.encoded_message

        # Creating a list of Nodes from a list of pairs (str, freq)
        node_queue = [Node(freq, el) for (el, freq) in Counter(self.__message).items( )]
        # Transform a list into a priority queue
        heapq.heapify(node_queue)

        self.huffman_tree = build_huffman_tree(node_queue)
        huffman_codes = self.get_codes()

        encoded_message = bitarray()
        encoded_message.encode(huffman_codes, self.__message)
        self.encoded_message = encoded_message
        return self.encoded_message

    def decode_message(self, encoded_message: bitarray) -> str:
        # encoded_message_str = str(encoded_message)

        decoded_message = ''.join(self.iterdecode(encoded_message))
        return decoded_message

    def traverse(self, iterator) -> str:
        """
        Traverse tree until a leaf node is reached, and return its symbol.
        This function consumes an iterator on which next() is called during each
        step of traversing.
        """
        node = self.huffman_tree
        while 1:
            bit = next(iterator)
            node = node.right if bit else node.left
            if node is None:
                raise ValueError("Prefix code does not match data in bitarray")

            if node.chars is not None:
                return node.chars

        pass

    def iterdecode(self, bitsequence: bitarray):
        """
        Given a bitsequence, decode the bitsequence by self.huffman_tree
        and generate the symbols.
        """
        iterator = iter(bitsequence)
        while True:
            try:
                yield self.traverse(iterator)
            except StopIteration:
                return
