#!/usr/local/bin/python3

class TreeNode:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def __repr__(self):
        return str(self.value)+" -> ["+",".join([str(node) for node in self.children])+"]"

    def __str__(self):
        return str(self.value)+" -> ["+",".join([str(node.value) for node in self.children])+"]"


def bfs(start, target):
    Open, Closed = [start], []
    while Open:
        print("open:"+",".join([node.value for node in Open])+" close:"+",".join([node.value for node in Closed]))
        x = Open.pop(0)
        if x.value == target:
            return True
        else:
            Closed = [x] + Closed
            for child in x.children:
                if child not in Closed:
                    Open.append(child)
    return False


if __name__ == "__main__":
    A = TreeNode("A", [])
    B = TreeNode("B", [])
    C = TreeNode("C", [])
    D = TreeNode("D", [])
    E = TreeNode("E", [])
    F = TreeNode("F", [])
    G = TreeNode("G", [])
    H = TreeNode("H", [])
    I = TreeNode("I", [])
    J = TreeNode("J", [])
    K = TreeNode("K", [])
    L = TreeNode("L", [])
    M = TreeNode("M", [])
    N = TreeNode("N", [])
    O = TreeNode("O", [])
    P = TreeNode("P", [])
    Q = TreeNode("Q", [])
    R = TreeNode("R", [])
    S = TreeNode("S", [])
    T = TreeNode("T", [])
    A.children += [B,C,D]
    B.children += [E,F]
    C.children += [G,H]
    D.children += [I,J]
    E.children += [K,L]
    F.children += [M,N]
    G.children += [O]
    H.children += [P,Q]
    I.children += [R,S]
    J.children += [T]

    print("Breadth First Search for Node T")
    print(bfs(A, "T"))
