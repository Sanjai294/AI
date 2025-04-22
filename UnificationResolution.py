import copy

class Predicate:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return f"{self.name}({', '.join(self.arguments)})"

    def __eq__(self, other):
        return isinstance(other, Predicate) and self.name == other.name and self.arguments == other.arguments

    def substitute(self, theta):
        self.arguments = [theta.get(arg, arg) for arg in self.arguments]


class Clause:
    def __init__(self, literals):
        self.literals = literals

    def __str__(self):
        return " v ".join(str(literal) for literal in self.literals)


def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta


def unify(x, y, theta):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, Predicate) and isinstance(y, Predicate):
        if x.name != y.name or len(x.arguments) != len(y.arguments):
            return None
        for x_arg, y_arg in zip(x.arguments, y.arguments):
            theta = unify(x_arg, y_arg, theta)
            if theta is None:
                return None
        return theta
    else:
        return None


def resolve(c1, c2):
    resolvents = []
    for l1 in c1.literals:
        for l2 in c2.literals:
            # Only try to resolve complementary literals
            if l1.name == l2.name:
                theta = unify(l1, l2, {})
                if theta is not None:
                    new_literals = []
                    for lit in c1.literals + c2.literals:
                        if lit != l1 and lit != l2:
                            new_lit = copy.deepcopy(lit)
                            new_lit.substitute(theta)
                            new_literals.append(new_lit)
                    resolvents.append(Clause(new_literals))
    return resolvents


# Example predicates
p = Predicate("P", ["x"])
q = Predicate("Q", ["y"])
r = Predicate("P", ["a"])
s = Predicate("S", ["y"])

# Example clauses
c1 = Clause([p, q])
c2 = Clause([r, s])

# Resolving clauses
resolvents = resolve(c1, c2)

# Printing resolvents
for resolvent in resolvents:
    print(resolvent)
