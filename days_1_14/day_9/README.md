# Day 9: Dictionaries, Nesting, and the Blind Auction

Day 9 introduces a new, powerful data structure in Python: the dictionary. We'll learn how to store data in key-value pairs, how to nest different data structures within each other, and apply these concepts to build a silent auction program.

---

## 1. Python Dictionaries

A dictionary in Python is a data structure that allows us to associate a **key** to a **value**. This is incredibly useful for storing related pieces of information.

### Dictionary Basics

-   **Creating a dictionary:**
    ```python
    # An example dictionary
    colours = {
        "apple": "red",
        "pear": "green",
        "banana": "yellow"
    }
    ```

-   **Retrieving items from a dictionary:** You use the key to look up its associated value.
    ```python
    print(colours["pear"])
    # Will print "green"
    ```

-   **Creating an empty dictionary:**
    ```python
    my_empty_dictionary = {}
    ```

-   **Adding new items to a dictionary:**
    ```python
    colours["peach"] = "pink"
    ```

-   **Editing an existing item:** You can change the value of an existing key by assigning a new value to it.
    ```python
    colours["apple"] = "green"
    ```

-   **Looping through a dictionary:**
    ```python
    # Loop through and print all the keys
    for key in colours:
        print(key)

    # Loop through and print all the values
    for key in colours:
        print(colours[key])
    ```

---

## 2. Nesting Data Structures

You can create complex data structures by nesting lists and dictionaries inside one another.

### Nesting a List inside a Dictionary
A dictionary's value can be a list, allowing you to associate a key with multiple items.
```python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
```
> #### PAUSE 1
> See if you can figure out how to print out "Lille" from the nested List called `travel_log`.
> > **Hint:** To get this part: `["Paris", "Lille", "Dijon"]` you would need: `travel_log["France"]`. Therefore to get Lille, you need: `travel_log["France"][1]`

### Nesting Lists inside other Lists
We've previously seen Nested Lists:
```python
nested_list = ["A", "B", ["C", "D"]]
```
> #### PAUSE 2
> Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list `nested_list`.
> > **Hint:** To get this list: `["C", "D"]` we need the code: `nested_list[2]`. Therefore, to get "D" we need: `nested_list[2][1]`

### Nesting a Dictionary inside a Dictionary
You can also nest a dictionary in a dictionary:
```python
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
```
> #### PAUSE 3
> Figure out how to print out "Stuttgart" from the following list.
> > **Hint:** You would need to access the keys in sequence: `travel_log["Germany"]["cities_visited"][2]`

---

## 3. Project: Blind Auction

The goal for Day 9 is to build a blind auction program where bidders can enter their names and bids secretly. The program then determines the highest bidder.

### Demo
[Try the live demo here.](https://appbrewery.github.io/python-day9-demo/)

### Functionality
- Each person writes their name and bid.
- The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking for a name and bid.
- Each person's name and bid are saved to a dictionary.
- Once all participants have placed their bid, the program works out who has the highest bid and prints it.

> **Hint:** Try writing out a flowchart to plan your program.
>
> **Hint:** The values that come from the `input()` function are Strings, you'll need to use the `int()` function to convert it to a number.
>
> **Hint:** There are several ways of clearing the output. The easiest is to simply print `"\n"` many times so that the output scrolls down many lines. e.g.
> ```python
> # This will add 20 new lines to the output
> print("\n" * 20)
> ```

### Flowchart
If you want to see an example flowchart, you can view it [here](https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Blind%20Auction%20Flow%20Chart#R3VnbcpswEP0aPzYDCLB5tHNrZ9pMpu6kzaMMilEDiBHyLV%2FfFYirHMdp7JD4JUGrXV3Ont2V5AE6j9fXHKfhDxaQaGAZwXqALgaWZRqmAf%2BkZFNIHM8qBHNOA6VUC6b0iZSWSrqgAclaioKxSNC0LfRZkhBftGSYc7Zqqz2wqD1riudEE0x9HOnS3zQQoZK6jl13fCV0HpZTm65X9MS41FZbyUIcsFVDhC4H6JwzJoqveH1OIoleCUxhd%2FVMb7UyThKxj8Hs4R5fx%2BMlu%2F52dxPepdM7H31BxShLHC3UjtVixaaEgASAiGoyLkI2ZwmOLmvphLNFEhA5jQGtWuc7YykITRD%2BJUJslHvxQjAQhSKOVG8xp5zo2b0pUcYW3Cc7NlSSBPM5ETv0rMoDwF3CYiL4Buw4ibCgy%2FY6sCLRvNKrYYYPhfQrUDc11Ke%2Fxj9%2FadDXwEqUViEVZJrifP8riLdtIC4JF2S9G0Z928rAHimuqmi1VXNVU99TorBBemQcCSfn1Nhp7clOu092Wjo7Q0hclhEBcDKJchbn6VWcpZsPx1mvZ84OT42z9p6cdfvkrK2hPs4e84LP4e8NjokcIUkXon%2FCOk6LsKajM9a0t1DWPhZlvVOjrLsnZUd9UtbdSdkJ2FrGLaew0Y%2FG2OpI2xtjTf0E9ckp%2B1YqKtNbRmHmynOO1fYcGnU8UoSIsuo4pVrG%2F%2FtppHM8COqEjJOgojqsQB4usLwsUl9QcESOAKwUIjmU6o9kUxnlQ54NLBfHkvDJLEsrh%2FQZKmh41gmWLQcSc%2BjoweIcLVhGfcQGWVPxR5nL7%2FuG%2FGLd6LjYlI0EdpubAISqed%2Fsq83yVml3wCg00Z6VwxweIl7HnONNQyGVcZg9H872yGxxy%2B5e%2BTv6yHN26cNHsYKDxnwFdi90Mxt0Uzw6CcI1noz6eLDQ34mKwwp9KLIzz9N5%2FpfJ5kCu141gR5MZNNy5%2FFpkhMtsvgplpl%2FhnKp51p%2FJEtBN3SGLZ4usp7RdVcqX0na3oh4Oc%2F2AeE8yDSbYtGjjgSM6T%2BDbh82DJ9BEQkN9HI1VR0yDoIg6ktEnPMuHksRW%2BQfGdSYD50KOBYGWFTF3IKiRZ7dzkmFrQG87S1pHw9nrtTxWOeo1BbKVrerk9Q75arhnvnrrC9b2gmZ1HnvQcL%2Fz7GsLbbdwOvbuQttd12v1zeE7FGZTf5o6jwjm1fk68zkhiZ6I3%2FkMjZzOK%2FSWVLztSe9ot80y9TSAu6L5LaTALYQ1kEyUdQyuMlVX%2ByqT2wTEj4pKCSpx%2B4azokkii2fPHnCGL3vA9LYUQ%2FdoLrA0F9ywT18LXdTB2dBxRoephdCsf2osMkr9iy26%2FAc%3D#%7B%22pageId%22%3A%22fezw1VAINj_9lBO2EaiH%22%7D).
