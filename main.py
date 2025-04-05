import random

# Count hits based on the target number
def count_hits(rolls, target_number):
    """
    Counts how many rolls meet or exceed the target number.
    """
    return sum(1 for roll in rolls if roll >= target_number)

# General dice rolling function
def rolling_dice(num_rolls, num_sides):
    """
    Rolls a specified number of dice and returns the results.
    """
    return [random.randint(1, num_sides) for _ in range(num_rolls)]

# Argent: Rolling 3d10
def argent(target_number=9, num_rolls=3, num_sides=10):
    """
    Rolls 3d10 and counts dice that meet or exceed the target number.
    """
    rolls = rolling_dice(num_rolls, num_sides)
    print_results(rolls, target_number)
    return count_hits(rolls, target_number)

# Jolnar: Rolling 2d10 with rerolls and subtracting 1 from all rolls
def jolnar(target_number=9, num_rolls=2, num_sides=10):
    """
    Rolls 2d10, subtracts 1 from all rolls, rerolls missed dice once,
    and counts dice that meet or exceed the target number.
    """
    rolls = rolling_dice(num_rolls, num_sides)
    #rolls = [roll - 1 for roll in rolls]  # Subtract 1 from each roll
    rerolled = [roll if roll >= target_number else random.randint(1, num_sides) for roll in rolls]
    print_results(rerolled, target_number)  # Print the results after reroll
    return count_hits(rerolled, target_number)

# Print results of dice rolls and hits
def print_results(rolls, target_number):
    """
    Prints the results of the rolls and the number of hits.
    """
    print(f"Rolls: {rolls}")
    print(f"Number of hits (>= {target_number}): {count_hits(rolls, target_number)}")

# Example usage
hits_argent = argent(6, 4, 10)  # Rolls for Argent
print(f"Total hits for Argent: {hits_argent}")

hits_jolnar = jolnar(6, 3, 10)  # Rolls for Jolnar with reroll and subtraction
print(f"Total hits for Jolnar: {hits_jolnar}")

# Simulate and compare
def simulate(trials=20000):
    argent_results = [argent() for _ in range(trials)]
    jolnar_results = [jolnar() for _ in range(trials)]

    avg_argent = sum(argent_results) / trials
    avg_jolnar = sum(jolnar_results) / trials

    print(f"Average hits for Argent: {avg_argent}")
    print(f"Average hits for Jolnar (with reroll): {avg_jolnar}")

simulate()
