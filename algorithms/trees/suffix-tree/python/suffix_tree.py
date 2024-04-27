#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""suffix_tree.py



.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import List, Optional


def main() -> None:
    """Driving code and main function"""
    text = "banana"
    suffix_tree = SuffixTree(text)
    suffix_tree.print_suffixes()
 
    return None


class SuffixTreeNode:
    """A node in the suffix tree."""
    def __init__(self, start: int, end: Optional[int] = None):
        self.children: dict[str, SuffixTreeNode] = {}
        self.suffix_link: Optional[SuffixTreeNode] = None
        self.start = start
        self.end = end

class SuffixTree:
    """A suffix tree data structure."""
    def __init__(self, text: str):
        self.root = SuffixTreeNode(-1)
        self.text = text
        self.build_suffix_tree()

    def build_suffix_tree(self) -> None:
        """Build the suffix tree for the given text."""
        n = len(self.text)
        active_node = self.root
        active_edge = 0
        active_length = 0
        remaining_suffix_count = 0
        last_new_node = None

        for i in range(n):
            last_new_node = None
            remaining_suffix_count += 1

            while remaining_suffix_count > 0:
                if active_length == 0:
                    active_edge = i

                if self.text[i] not in active_node.children:
                    active_node.children[self.text[i]] = SuffixTreeNode(i, n-1)

                    if last_new_node is not None:
                        last_new_node.suffix_link = active_node
                        last_new_node = None

                else:
                    next_node = active_node.children[self.text[active_edge]]

                    if active_length >= next_node.end - next_node.start + 1:
                        active_edge += next_node.end - next_node.start + 1
                        active_length -= next_node.end - next_node.start + 1
                        active_node = next_node
                        continue

                    if self.text[next_node.start + active_length] == self.text[i]:
                        if last_new_node is not None and active_node != self.root:
                            last_new_node.suffix_link = active_node
                            last_new_node = None

                        active_length += 1
                        break

                    new_node = SuffixTreeNode(next_node.start, next_node.start + active_length - 1)
                    active_node.children[self.text[active_edge]] = new_node
                    new_node.children[self.text[i]] = SuffixTreeNode(i, n-1)
                    next_node.start += active_length
                    new_node.children[self.text[next_node.start]] = next_node

                    if last_new_node is not None:
                        last_new_node.suffix_link = new_node

                    last_new_node = new_node

                remaining_suffix_count -= 1

                if active_node == self.root and active_length > 0:
                    active_length -= 1
                    active_edge = i - remaining_suffix_count + 1
                elif active_node != self.root:
                    active_node = active_node.suffix_link

    def traverse(self, node: SuffixTreeNode, suffix: str) -> None:
        """Traverse the suffix tree and print all the suffixes."""
        if node.start != -1:
            print(suffix + self.text[node.start:node.end+1])

        for child in node.children.values():
            self.traverse(child, suffix + self.text[node.start:node.end+1])

    def print_suffixes(self) -> None:
        """Print all the suffixes of the text."""
        self.traverse(self.root, "")



if __name__ == '__main__':
    main()

