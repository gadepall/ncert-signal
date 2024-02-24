import numpy as np

def generate_ap_sequence(start, end, num_terms, verify):
    # Generate the arithmetic progression sequence using linspace
    ap_sequence = np.linspace(start, end, num_terms, endpoint=True, retstep=False)

    try:
        # Write the AP sequence to the output file
        with open(verify, 'w') as file:
            file.write("Arithmetic Progression Sequence:\n")
            for term in ap_sequence:
                file.write(f"{term} ")

        print(f"AP sequence has been written to {verify}")

    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    # Specify the parameters for the AP sequence
    start_value = 8
    end_value = 26
    num_terms = 7
    verify = "verifydata.txt"  # Update with your desired file name

    # Generate and write the AP sequence to the output file
    generate_ap_sequence(start_value, end_value, num_terms, verify)

