# Finds in-frame stops in genewise output, converts them to lower case and counts them

def stop_finder(sequence):
    codon_table = {
        "TAA": "taa",
        "TAG": "tag",
        "TGA": "tga"
    }

    stop_codons = 0
    result = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]
        if codon in codon_table:
            stop_codons += 1
            result.append(codon_table[codon])
        else:
            result.append(codon)

    return "".join(result), stop_codons

if __name__ == "__main__":
    filename = "genewise"

    with open(filename, "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            coding_sequence = columns[10]  # Column 11 (0-based index)
            modified_sequence, stop_codons = stop_finder(coding_sequence)
            columns[10] = modified_sequence  # Replace the original sequence with the modified one
            print("\t".join(columns) + "\t" + str(stop_codons))
