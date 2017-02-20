def make_float(string_value):
    """
    Return a float for the string,  handle exceptions.
    :string_value: string
    :return: float(string_value)
    """
    try:
        x = float(string_value)
    except ValueError:
        print("String could not be converted to a float!")
        x = "Err"
    return x
