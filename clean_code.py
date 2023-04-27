from typing import List


def check_subsequence_match(sequence: List[str], subsequence: List[str]) -> bool:
    """Checks if a list of strings match another list of strings."""

    # index pointing to the next string to be checked in the
    # sequence list
    sequence_index = 0
    for subsequence_item in subsequence:
        for index in range(sequence_index, len(sequence)):
            if sequence[index] == subsequence_item:
                break
        else:
            # this is executed only when we fail to find a match
            # in the sequence list for the current subsequence_item
            # in the subsequence list
            return False
        # this is executed only when we find a match at index
        sequence_index = index + 1
    return True


def get_matching_sequences(
    sequences: List[List[str]], subsequence: List[str]
) -> List[List[str]]:
    """Filters a list of lists of strings based on a list of strings
    that represents a pattern."""
    return [
        sequence
        for sequence in sequences
        if check_subsequence_match(sequence, subsequence)
    ]


def get_matching_sequences_in_reverse(
    sequences: List[List[str]], subsequence: List[str]
) -> List[List[str]]:
    """Filters a list of lists of strings based on a list of strings
    that represents a reversed pattern."""
    subsequence.reverse()
    return get_matching_sequences(sequences, subsequence)


def main() -> None:
    # trying some examples on subsequence match in original order
    print(get_matching_sequences(sequences=[], subsequence=["hi"]))
    print(
        get_matching_sequences(
            sequences=[["", "hi"], [], ["", "a"]], subsequence=["hi"]
        )
    )
    print(
        get_matching_sequences(
            sequences=[["hi", "", "again"], [], ["", "a"]], subsequence=["hi", "again"]
        )
    )

    # trying some examples on subsequence match in reverse order
    print(get_matching_sequences_in_reverse(sequences=[], subsequence=["hi"]))
    print(
        get_matching_sequences_in_reverse(
            sequences=[["", "hi", "", "again"], [], ["", "a"]],
            subsequence=["again", "hi"],
        )
    )


if __name__ == "__main__":
    main()
