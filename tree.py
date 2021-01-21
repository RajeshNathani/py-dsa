class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        for child in self.children:
            print("  ", child.data)
            for childs in child.children:
                print("    ", childs)


def Electronics_tree():
    root = TreeNode("Electronics")
    Laptop = TreeNode("Laptop")
    Mobile = TreeNode("Mobile")
    Tv = TreeNode("TV")
    root.addChild(Laptop)
    root.addChild(Mobile)
    root.addChild(Tv)
    Laptop.addChild("Mac")
    Laptop.addChild("Windows")
    Laptop.addChild("Linux")
    Mobile.addChild("IOS")
    Mobile.addChild("Andriod")
    Tv.addChild("LG")
    Tv.addChild("Sony")
    return root


if __name__ == "__main__":
    root = Electronics_tree()
    root.print_tree()
    pass
