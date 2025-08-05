### Docstrings

# You can use docstrings to write multiline comments that document your code.

# Syntax
# Just enclose your text inside a pair of three double quotes.

# e.g.
# """ 
# My 
# Multiline 
# Comment 
# """

# Documenting Functions
# A neat feature of docstrings is you can use it just below the definition of a function and that text will be displayed when you hover over a function call. It's a good way to remind yourself what a self-created function does.

# e.g.
# def my_function(num):
#     """Multiplies a number by itself."""
#     return num * num


def format_name(f_name, l_name):
    """Take a first and last name and format it to 
    return the title case version of the name."""""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
