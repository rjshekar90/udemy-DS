
from __future__ import print_function

class BinaryTree(object):

    def __init__(self, rootObj):

        self.key = rootObj
        self.lchild = None
        self.rchild = None

    def insertLeft(self, newNode):

        if self.lchild == None:
            self.lchild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.lchild = self.lchild
            self.lchild = t

    def insertRight(self, newNode):

        if self.rchild == None:
            self.rchild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rchild = self.rchild
            self.rchild = t


    def getrChild(self):
        return self.rchild

    def getlChild(self):
        return self.lchild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree("a")

print (r.getRootVal())

r.insertLeft("b")
r.insertRight("c")

print (r.getlChild().getRootVal())
print (r.getrChild().getRootVal())
