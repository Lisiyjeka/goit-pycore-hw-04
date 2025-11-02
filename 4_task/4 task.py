def parse_input(user_input):
    #Розбиває введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    #Додає новий контакт з перевіркою наявності 2 аргументів
    if len(args) != 2: 
        return "Error: Please provide both name and phone number. Usage: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    #Змінює номер телефону існуючого контакту
    if len(args) != 2:
        return "Error: Please provide both name and new phone number. Usage: change [name] [new_phone]"
    
    name, new_phone = args
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    #Показує номер телефону за ім'ям
    if len(args) != 1:
        return "Error: Please provide a name. Usage: phone [name]"
    
    name = args[0]
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    return contacts[name]

def show_all(contacts):
    #Показує всі контакти
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    #Основна функція для управління ботом
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        
        # Обробка порожнього вводу
        if not user_input:
            continue
            
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
            
        elif command in ["hello", "hi"]:
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()