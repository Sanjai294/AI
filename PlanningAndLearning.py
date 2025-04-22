class BlocksWorld:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks
        self.blocks = [[] for _ in range(num_blocks)]  # Create stacks for blocks

        for i in range(num_blocks):
            self.blocks[i].append(i)  # Place each block in its own stack

    def move(self, source, destination):
        # Check for invalid moves
        if source == destination or source >= self.num_blocks or destination >= self.num_blocks:
            print(f"Invalid move from {source} to {destination}")
            return

        if not self.blocks[source]:  # If the source stack is empty, do nothing
            print(f"Stack {source} is empty. Cannot move.")
            return

        block = self.blocks[source].pop()  # Remove the top block from the source stack
        self.blocks[destination].append(block)  # Place it on the destination stack
        print(f"Moved block {block} from Stack {source} to Stack {destination}")

    def print_state(self):
        print("\nCurrent State of Blocks:")
        for i in range(self.num_blocks):
            print(f"Stack {i}: {self.blocks[i]}")
        print("-" * 30)


# Initialize a Blocks World with 4 stacks
world = BlocksWorld(4)

# Print initial state
world.print_state()

# Move block from stack 1 to stack 2
world.move(1, 2)

# Move block from stack 3 to stack 0
world.move(3, 0)

# Print final state
world.print_state()
