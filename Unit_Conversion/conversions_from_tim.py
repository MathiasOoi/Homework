# This is our input
in_conversions = [
        ('inches', 'feet', 12),
        ('feet', 'yards', 3),
        ('cm', 'feet', 30),
        ('cm', 'm', 100),
        ('m', 'km', 1000),
        ]

# Convert to a dict of dicts
factors = {}
for (from_unit, to_unit, factor) in in_conversions:
    if from_unit not in factors: factors[from_unit] = {}
    if to_unit not in factors: factors[to_unit] = {}
    factors[from_unit][to_unit] = factor
    factors[to_unit][from_unit] = 1.0 / factor

# Initialize our data structures
base_unit = in_conversions[0][0]
conversions = {base_unit : 1.0}
explored = set()
queue = [base_unit]

# Do a BFS ONCE, and save the table as we go, searching until
# we run out of reachable units
while queue:
    from_unit = queue.pop()
    explored.add(from_unit)
    for (to_unit, factor) in factors[from_unit].items():
        if to_unit in explored:
            continue
        conversions[to_unit] = factor * conversions[from_unit]
        if to_unit not in queue:
            queue.append(to_unit)

# With conversions defined, we can now define the convert function
def convert(unit_from, unit_to, amount):
    return amount * conversions[unit_from] / conversions[unit_to]

# Here, just make every possible conversion
amount = 1
for a in conversions:
    for b in conversions:
        print(amount, a, 'into', b, convert(a, b, amount))








