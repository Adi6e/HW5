import secrets
import string

def generate_code(segment_length=5, segment_count=5):
    # Validate segment_length and segment_count to prevent potential overflows
    if segment_length <= 0 or segment_count <= 0:
        raise ValueError("Segment length and count must be positive integers.")
    
    segments = []
    for _ in range(segment_count):
        # Use a fixed character set to avoid unexpected behavior
        segment = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(segment_length))
        segments.append(segment)
    
    return '-'.join(segments)

def generate_codes(n):
    # Validate n to prevent potential overflows
    if n <= 0:
        raise ValueError("Number of codes must be a positive integer.")
    
    return [generate_code() for _ in range(n)]

def save_codes_to_file(codes, filename):
    try:
        with open(filename, 'w') as file:
            for code in codes:
                file.write(code + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of codes to generate: "))
        if n <= 0:
            raise ValueError("The number of codes must be a positive integer.")
    except ValueError as e:
        print(f"Input error: {e}")
        exit(1)

    codes = generate_codes(n)
    save_codes_to_file(codes, 'codes.txt')
    print(f"{n} codes successfully generated and saved to 'codes.txt'.")