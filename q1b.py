# Name:
# Email ID:

def is_compatible(patient_group, donor_group):
    compatibility_map = {
        'A': ['A', 'AB'],
        'B': ['B', 'AB'],
        'AB': ['AB'],
        'O': ['O', 'AB', 'A', 'B']
    }

    return True if donor_group in compatibility_map[patient_group] else False