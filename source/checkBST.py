def checkBST(root):
    numbers = []
    def isOrder(root):
        if root.left is not None:
            isOrder(root.left)
        numbers.append(root.data)
        if root.right is not None:
            isOrder(root.right)
    if numbers == sorted(numbers):
        print("Yes")
    else:
        print("No")
