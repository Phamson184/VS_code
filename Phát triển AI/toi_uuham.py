import copy

class Node:
    def __init__(self, state, g, move="Initial"):
        self.state = state
        self.g = g
        self.move = move
        self.h = self.calculate_h(state)
        self.f = self.g + self.h

    # Hàm h(x): Đếm số ô sai vị trí
    def calculate_h(self, state):
        goal = [[1, 2, 3], [8, 4, 5], [7, 0, 6]]
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != goal[i][j]:
                    misplaced += 1
        return misplaced

    def print_node(self):
        print(f"--- Move: {self.move} ---")
        for row in self.state:
            # In số 0 thành dấu '_' cho dễ nhìn
            print(" ".join(str(x) if x != 0 else "_" for x in row))
        print(f"g={self.g}, h={self.h}, f={self.f}\n")

# Đường đi tối ưu dựa trên phân tích ở trên
initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# Tạo các node theo từng bước tối ưu
n0 = Node(initial_state, g=0)
n1 = Node([[1, 2, 3], [8, 4, 0], [7, 6, 5]], g=1, move="Right (Swap with 4)")
n2 = Node([[1, 2, 3], [8, 4, 5], [7, 6, 0]], g=2, move="Down (Swap with 5)")
n3 = Node([[1, 2, 3], [8, 4, 5], [7, 0, 6]], g=3, move="Left (Swap with 6) - GOAL!")

print("CÁCH TRÌNH BÀY ĐƯỜNG ĐI TỐI ƯU:\n")
n0.print_node()
n1.print_node()
n2.print_node()
n3.print_node()