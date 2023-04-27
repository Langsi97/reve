from typing import List


def check_subsequence_match(sequence: List[str], subsequence: List[str]) -> bool:
    """Checks if a list of strings match another list of strings.

    The two lists match if every string in the second list appears
    in the first list keeping the same relative order as they appear
    in the second list.

    Args:
        sequence: A list of strings.
        subsequence: A sequence of strings representing the pattern
        we are searching for.

    Returns:
        A boolean representing whether all the strings of the second
        list appear in the first list in the same relative order.
    """

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
    that represents a pattern.

    A list of strings match another if every string in the second list
    appears in the first list keeping the same relative order as they
    appear in the second list.

    Args:
        sequences: A list of lists of strings.
        subsequence: A sequence of strings representing the pattern we
        are searching for.

    Returns:
        The list of list of strings in sequences that match the list
        subsequence keeping the relative order.
    """
    return [
        sequence
        for sequence in sequences
        if check_subsequence_match(sequence, subsequence)
    ]


def get_matching_sequences_in_reverse(
    sequences: List[List[str]], subsequence: List[str]
) -> List[List[str]]:
    """Filters a list of lists of strings based on a list of strings
    that represents a reversed pattern.

    Functions similar to the function get_matching_sequences where the
    order of the strings in the second list is reversed.

    Args:
        sequences: A list of lists of strings.
        subsequence: A sequence of strings representing the pattern we
        are searching for its reverse.

    Returns:
        The list of list of strings in sequences that match the list
        subsequence keeping the relative reversed order.
    """
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
