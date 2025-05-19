# kris kringle Van Der Haar
import random

def generate_kris_kringle_scheme(participants_groups):
    # Flatten the list of participants
    all_participants = [person for group in participants_groups for person in group]
    
    # Create a dictionary to track which group each person belongs to
    group_membership = {}
    for i, group in enumerate(participants_groups):
        for person in group:
            group_membership[person] = i
    
    # Attempt to generate a valid assignment
    max_attempts = 1000
    for attempt in range(max_attempts):
        givers = all_participants.copy()
        receivers = all_participants.copy()
        assignments = {}
        
        random.shuffle(givers)
        random.shuffle(receivers)
        
        valid_assignment = True
        
        for giver in givers:
            # Filter out invalid receivers (self or same group)
            valid_receivers = [r for r in receivers if r != giver and group_membership[r] != group_membership[giver]]
            
            if not valid_receivers:
                valid_assignment = False
                break
            
            # Choose a random valid receiver
            receiver = random.choice(valid_receivers)
            assignments[giver] = receiver
            receivers.remove(receiver)
        
        if valid_assignment:
            return assignments
    
    return None

# Define participant groups (people who cannot be matched with each other)
groups = [
    ["Robbo", "Monique", "Jack", "Kate"],
    ["Nicole", "John", "Alex", "Marcus", "Isabel"],
    ["Michelle", "Phil", "Xavier", "Caleb", "Lauren"],
    ["Damien", "Joanne", "Nicholas", "Emma", "Claire", "Rachael"],
    ["Mark", "Dylan"]
]

# Generate the scheme
scheme = generate_kris_kringle_scheme(groups)

if scheme:
    print("Kris Kringle Assignments:")
    for giver, receiver in scheme.items():
        print(f"{giver} → {receiver}")
else:
    print("Could not find a valid assignment after multiple attempts.")
    
# Test the scheme to verify it meets the constraints
if scheme:
    valid = True
    for giver, receiver in scheme.items():
        for group in groups:
            if giver in group and receiver in group:
                print(f"Invalid assignment: {giver} and {receiver} are in the same group!")
                valid = False
    
    if valid:
        print("\nAll assignments meet the constraints!")
    else:
        print("\nSome assignments violate the constraints.")
