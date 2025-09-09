def select_activities(activities):
    # Sort activities by finish time (greedy choice)
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    for act in activities[1:]:
        # If start time >= last finish time, take it
        if act[0] >= selected[-1][1]:
            selected.append(act)
    
    return selected

# Example:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (8,11)]
print("Selected Activities (Greedy):", select_activities(activities))
# Output: [(1, 4), (5, 7), (8, 9)]











# Iterate and choose non-overlapping activities:
# Next: (3, 5) → starts at 3, but 3 < 4 → overlaps → skip.

# Next: (0, 6) → starts at 0, 0 < 4 → overlaps → skip.

# Next: (5, 7) → starts at 5, 5 ≥ 4 → valid → add it.

# Next: (8, 9) → starts at 8, 8 ≥ 7 → valid → add it.