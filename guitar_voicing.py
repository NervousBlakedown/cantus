FRETBOARD = {
    'E': ['E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3'],
    'A': ['A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3'],
    'D': ['D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4'],
    'G': ['G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4'],
    'B': ['B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4'],
    'e': ['E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5']
}

def generate_voicing(selected_notes):
    """
    Generate all possible guitar voicings for the exact notes selected on the piano.
    """
    voicings = []
    # Map notes to all possible string/fret positions
    note_positions = {note: [] for note in selected_notes}

    for string, frets in FRETBOARD.items():
        for fret, note in enumerate(frets):
            if note in selected_notes:
                note_positions[note].append({"string": string, "fret": fret})

    print("Note positions:", note_positions)

    # Generate combinations for exact matches
    from itertools import product
    possible_combinations = list(product(*note_positions.values()))

    # Filter combinations to ensure no string is reused
    for combination in possible_combinations:
        strings_used = [pos['string'] for pos in combination]
        if len(strings_used) == len(set(strings_used)):  # Ensure unique strings
            voicings.append(combination)

    print("Final voicings:", voicings)
    return voicings
