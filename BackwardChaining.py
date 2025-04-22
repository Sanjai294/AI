knowledge_base = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": []
}

# Let's assume H, F, and G are known facts (they have no dependencies)
known_facts = {"F", "G", "H"}

def backward_chaining(kb, goal):
    # If it's a known fact
    if goal in known_facts:
        return True

    # If the goal is not in KB, it can't be inferred
    if goal not in kb:
        return False

    # Check all conditions for the goal
    for subgoal in kb[goal]:
        if not backward_chaining(kb, subgoal):
            return False
    return True

goal = "A"
result = backward_chaining(knowledge_base, goal)

if result:
    print(f"The goal '{goal}' can be inferred.")
else:
    print(f"The goal '{goal}' cannot be inferred.")
