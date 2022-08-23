'''
Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?
'''

# This involves the use of Merkle Trees. Every leaf contains the hash of its data, and every branch has a hash of its child hashes.

from abc import ABC, abstractmethod
import hashlib
h = hashlib.sha256

class Node(ABC):
    def __init__(self):
        self.parent = None
        self.digest = None

    def addToDirectory(self, directory):
        self.parent = directory
        directory.addChild(self)

    @abstractmethod
    def calculateDigest(self):
        pass

class Directory(Node):
    def __init__(self):
        Node.__init__(self)
        self.children = set()
        self.calculateDigest()

    def calculateDigest(self):
        new_hash = h(b"")
        for child in self.children:
            new_hash.update(child.digest.encode())
        if self.digest != new_hash.hexdigest():
            self.digest = new_hash.hexdigest()
            if self.parent:
                self.parent.calculateDigest()

    def addChild(self, child):
        self.children.add(child)
        self.calculateDigest()

    def sync(self, other_dir):
        if self.digest == other_dir.digest:
            return
        for node in self.children:
            if not node in other_dir.children:
                type(node)(node.addToDirectory(other_dir))
        for node in other_dir.children:
            if not node in self.children:
                type(node)(node.addToDirectory(self))

class File(Node):
    def __init__(self, data):
        Node.__init__(self)
        self._data = data
        self.calculateDigest()

    def calculateDigest(self):
        new_digest = h(self._data.encode()).hexdigest()
        if new_digest != self.digest:
            self.digest = new_digest
            if self.parent:
                self.parent.calculateDigest()

    def update_data(self, new_data):
        self._data = new_data
        self.calculateDigest()

class Computer:
    def __init__(self):
        self.root = Directory()
    
    def sync(self, other_cp):
        self.root.sync(other_cp.root)