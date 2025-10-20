# doctor_tree.py

class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        parent = self._find(self.root, parent_name)
        if not parent:
            print(f"Parent '{parent_name}' not found.")
            return
        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(child_name)
            else:
                print(f"{parent_name} already has a left report.")
        elif side == "right":
            if parent.right is None:
                parent.right = DoctorNode(child_name)
            else:
                print(f"{parent_name} already has a right report.")
        else:
            print("Invalid side. Use 'left' or 'right'.")

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        return self._find(node.left, name) or self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# emergency_queue.py

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while index < size:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        return self.data[0] if self.data else None

    def remove_min(self):
        if not self.data:
            return None
        min_patient = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return min_patient


# -------------------------------
# Design Memo (200–300 words)
# -------------------------------

'''
Design Memo:

A binary tree is ideal for modeling the hospital’s doctor reporting structure because it allows each doctor to have up to two direct reports, mirroring many real-world organizational hierarchies. The recursive nature of tree traversal makes it easy to visualize workflows and reporting chains. Preorder traversal is useful when generating top-down reports, starting from department heads. Inorder traversal can help with alphabetical or role-based sorting when the structure is balanced. Postorder traversal is valuable for bottom-up evaluations, such as performance reviews or cascading updates.

The emergency intake system benefits from a min-heap because it ensures that the most urgent patient (lowest urgency score) is always served first. This priority queue structure maintains efficiency even as new patients arrive or others are treated. Heaps are commonly used in real-time systems where dynamic prioritization is essential—such as operating systems, network packet routing, and healthcare triage.

Together, these data structures demonstrate how software engineers choose tools based on problem constraints. Trees offer clarity and hierarchy, while heaps offer speed and fairness. Implementing both systems reinforces algorithmic thinking and prepares students for technical interviews and real-world engineering challenges.
'''
