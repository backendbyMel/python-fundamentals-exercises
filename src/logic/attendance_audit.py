"""
A retail store manager needs to audit which 
employees were present during a specific week 
and identify duplicates or missing entries
"""

def run_attendance_audit(set_a, set_b):
    """
    make the list to set to audit it instead of for-loop
    """

    sanitize = [name.capitalize() for name in set_a]
    expected_staff = set(set_a)
    clocked_in = set(set_b)
    no_shows = expected_staff - clocked_in
    unexpected_guests = clocked_in.difference(expected_staff)
    worked = expected_staff.difference(no_shows)
    return worked, no_shows, unexpected_guests

def main():
    expected_staff = ['Ana','Bob','Ralph','Christy','Michael','Mel','Far']
    clocked_in_staff = ['Ana','Bob','Ralph','Christy','Louis']

    result = run_attendance_audit(expected_staff, clocked_in_staff)
    print("-" * 60)
    print(f"{'Worked:':<20} {sorted(result[0])}")
    print("-" * 60)
    print(f"{'No Show:':<20} {sorted(result[1])}")
    print("-" * 60)
    print(f"{'Unscheduled':<20} {sorted(result[2])}")
    
if __name__ == "__main__":
    main()