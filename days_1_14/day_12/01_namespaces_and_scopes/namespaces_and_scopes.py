## Namespaces and Scopes


enemies = 1


# Local Scope
# Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by 
# other code within the same block of code.

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")



# Global Scope
# Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible 
# anywhere in the code file.

increase_enemies()
print(f"enemies outside function: {enemies}")



# This will print as follows:
# enemies inside function: 2
# enemies outside function: 1


## Example:
# Local Scope
# def drink_potion():               # We are commenting this for testing purposes of the Global Scope example below this.
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()                    # We are commenting this for testing purposes of the Global Scope example below this.
# Can't access this potion_strength outside of its scope
# print(potion_strength)

# Global Scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()                  # Here its not giving an error, because it can be accessed because its a local function now.



# drink_potion()                    # This line is giving an error if we uncomment, because it cannot be accessed because its not on a top level.
print(player_health)