# # Basic class definition 
# class Person: 
#     # Class attribute (shared by all instances)
#     species = "Homo sapiens"

#     # Constructor method
#     def __init__(self, name, age):
#         # Instance attributes 
#         self.name = name 
#         self.age = age 

#     # Instance method 
#     def introduce(self):
#         return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
#     # Method with parameters
#     def have_birthday(self):
#         self.age += 1
#         return f"Happy birthday! {self.name} is now {self.age}."
    
# # Creating objects (instances)
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)

# # Accessing attributes
# print(person1.name) # "Alice"
# print(person1.age)  # 25

# # Calling methods
# print(person1.introduce())      
# print(person1.have_birthday())  


# # Class attributes 
# print(Person.species)   # "Homo sapiens"
# print(person1.species)  # "Homo sapiens"


# class BankAccount:

#     def __init__(self, account_number, owner, balance=0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = balance
#         self.transaction_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transaction_history.append(f"Deposited ${amount}")
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount"

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             self.transaction_history.append(f"Withdrew ${amount}")
#             return f"Withdrew ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid withdrawal amount or insufficient funds"

#     def get_balance(self):
#         return f"Current balance: ${self.balance}"

#     def get_transaction_history(self):
#         return self.transaction_history


# # Using the BankAccount class
# account = BankAccount("12345", "Alice", 1000)

# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance())
# print(account.get_transaction_history())



# # 1. Create a simple game character class with health, 
# # attack and heal methods. 

# class Game:

#     def __init__(self, health = 100):
#         self.health = health
#         self.health_history = []
    
#     def heal(self, amount):
#         if amount > 0:
#             self.health += amount
#             self.health_history.append(f"Heal {amount}")
#             return f"Heal {amount}. New health: {self.health}"
#         else:
#             return "Invalid heal amount"

#     def attack(self, amount):
#         if amount > 0 and amount <= self.health:
#             self.health -= amount
#             self.health_history.append(f"Attack {amount}")
#             return f"Attack {amount}. New health: {self.health}"
#         else:
#             return "Invalid attack amount or insufficient health"

#     def get_health(self):
#         return f"Current Health: {self.health}"

#     def get_health_history(self):
#         return self.health_history


# # Using the Game class
# GameHealth = Game(1000)

# print(GameHealth.heal(500))
# print(GameHealth.attack(200))
# print(GameHealth.get_health())
# print(GameHealth.get_health_history())


# class GameCharacter:

#     def __init__(self, health=100):
#         self.health = health
#         self.health_history = []

#     def heal(self, amount):
#         if amount > 0:
#             self.health += amount
#             self.health_history.append(f"Healed {amount}")
#             return f"Healed {amount}. New health: {self.health}"
#         else:
#             return "Invalid heal amount"

#     def attack(self, amount):
#         if amount > 0 and amount <= self.health:
#             self.health -= amount
#             self.health_history.append(f"Attacked {amount}")
#             return f"Attacked {amount}. New health: {self.health}"
#         else:
#             return "Invalid attack amount or insufficient health"

#     def get_health(self):
#         return f"Current health: {self.health}"

#     def get_health_history(self):
#         return self.health_history


# # Create character
# player = GameCharacter(100)

# # Loop
# while True:
#     print("\n--- GAME MENU ---")
#     print("1. Heal")
#     print("2. Attack")
#     print("3. Check Health")
#     print("4. Health History")
#     print("5. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         amount = int(input("Enter heal amount: "))
#         print(player.heal(amount))

#     elif choice == "2":
#         amount = int(input("Enter attack amount: "))
#         print(player.attack(amount))

#     elif choice == "3":
#         print(player.get_health())

#     elif choice == "4":
#         print(player.get_health_history())

#     elif choice == "5":
#         print("Game Over!")
#         break

#     else:
#         print("Invalid choice")


# class GameCharacter:

#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#         self.max_health = health

#     def attack(self, target):
#         damage = 20
#         target.health -= damage
#         if target.health < 0:
#             target.health = 0
#         return f"{self.name} attacks {target.name} for {damage} damage!"

#     def defend(self):
#         heal_amount = 10
#         self.health += heal_amount
#         if self.health > self.max_health:
#             self.health = self.max_health
#         return f"{self.name} defends and heals for {heal_amount} HP!"

#     def is_alive(self):
#         return self.health > 0

#     def status(self):
#         return f"{self.name}: {self.health}/{self.max_health} HP"


# # Create characters
# hero = GameCharacter("Hero", 100)
# enemy = GameCharacter("Goblin", 80)

# # Initial status
# print(hero.status())
# print(enemy.status())
# print()

# # Round 2
# print(enemy.attack(hero))
# print(hero.status())
# print()

# # Round 3
# print(hero.defend())
# print(hero.status())
# print()

# # Round 4
# print(hero.attack(enemy))
# print(enemy.status())
# print()

# # Check if enemy is still alive
# if enemy.is_alive():
#     print(f"{enemy.name} is still fighting!")
# else:
#     print(f"{enemy.name} has been defeated!")


class GameCharacter:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.max_health = health
    
    def attack(self, target):
        damage = 20
        target.health -= damage
        if target.health < 0:
            target.health = 0
        return f"{self.name} attacks {target.name} for {damage} damage!"
    
    def defend(self):
        heal_amount = 10
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        return f"{self.name} defends and heals for {heal_amount} HP!"
    
    def is_alive(self):
        return self.health > 0
    
    def status(self):
        return f"{self.name}: {self.health}/{self.max_health} HP"

# Create characters
hero = GameCharacter("Hero", 100)
enemy = GameCharacter("Goblin", 80)

# Game simulation
print("=== BATTLE START ===")
print(hero.status())
print(enemy.status())
print()

# Round 1
print(hero.attack(enemy))
print(enemy.status())
print()

# Round 2
print(enemy.attack(hero))
print(hero.status())
print()

# Round 3
print(hero.defend())
print(hero.status())
print()

# Round 4
print(hero.attack(enemy))
print(enemy.status())
print()

# Check if enemy is still alive
if enemy.is_alive():
    print(f"{enemy.name} is still fighting!")
else:
    print(f"{enemy.name} has been defeated!")