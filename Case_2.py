class TreeNode:
    def __init__(self, department, manager):
        self.department = department
        self.manager = manager
        self.children = []
        self.parent = None
 
def add_department(tree, parent_dept, department, manager):
    if tree.department == parent_dept:
        new_node = TreeNode(department, manager)
        tree.children.append(new_node)
        new_node.parent = tree
        return True
    for child in tree.children:
        if add_department(child, parent_dept, department, manager):
            return True
    return False
 
def find_department_node(root, department_name):
    if root.department == department_name:
        return root
    for child in root.children:
        result = find_department_node(child, department_name)
        if result:
            return result
    return None
 
def get_managers(node):
    managers = []
    while node:
        managers.append(node.manager)
        node = node.parent
    return managers
 
def print_tree(node, level=0):
    print(' ' * level * 4 + f"{node.department} ({node.manager})")
    for child in node.children:
        print_tree(child, level + 1)
 
def main():
    root_department = input("Enter the root department name: ")
    root_manager = input("Enter the root manager name: ")
    root = TreeNode(root_department, root_manager)
    while True:
        parent_dept = input("Enter the parent department name (or 'done' to finish): ")
        if parent_dept.lower() == 'done':
            break
        department = input("Enter the department name: ")
        manager = input("Enter the manager name: ")
        if not add_department(root, parent_dept, department, manager):
            print(f"Parent department '{parent_dept}' not found. Please try again.")
    print("\nCompany Hierarchy Tree:")
    print_tree(root)
    while True:
        department_name = input("\nEnter the department name to find its managers (or 'exit' to quit): ")
        if department_name.lower() == 'exit':
            break
        department_node = find_department_node(root, department_name)
        if department_node:
            managers = get_managers(department_node)
            print(f"Managers from department '{department_name}' up to the root: {managers}")
        else:
            print(f"Department '{department_name}' not found. Please try again.")
 
if __name__ == "__main__":
    main()
 