""" General utility methods """


def split_to_chunks(list_to_split, chunk_size):
    """ Split the given list into chunks of chunk_size. """
    for i in range(0, len(list_to_split), chunk_size):
        yield list_to_split[i:chunk_size + i]
