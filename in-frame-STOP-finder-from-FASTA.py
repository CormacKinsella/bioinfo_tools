#!/usr/bin/env python

import argparse

def stop_handler(sequence, action):
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
            if action == "soft-mask":
                result.append(codon_table[codon])
        else:
            result.append(codon)

    return "".join(result), stop_codons

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finds in-frame stops in Genewise coding sequence output, and either soft masks or removes them, counting instances.")
    parser.add_argument("--task", choices=["soft-mask", "remove"], required=True, help="Task to perform on in-frame stop codons: 'soft-mask' to convert to lower case, 'remove' to delete.")
    parser.add_argument("--input", required=True, help="Path to the input FASTA format file.")

    args = parser.parse_args()

    with open(args.input, "r") as fasta_file:
        sequence = ""
        header = ""
        for line in fasta_file:
            if line.startswith(">"):
                if header:
                    modified_sequence, stop_codons = stop_handler(sequence, args.task)
                    new_header = f"{header}:found-{stop_codons}-premature-STOPs"
                    print(f">{new_header}")
                    print(modified_sequence)
                header = line.strip()[1:]
                sequence = ""
            else:
                sequence += line.strip()

        if header:
            modified_sequence, stop_codons = stop_handler(sequence, args.task)
            new_header = f"{header}:found-{stop_codons}-premature-STOPs"
            print(f">{new_header}")
            print(modified_sequence)
