contacts = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(data):
    name, phone = data
    if not name in contacts:
        contacts[name] = phone
        return 'Contact added.'
    else:
        return 'Contact was created.'
    
def change_contact(data):
    name, phone = data
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return 'Contact not found.'
    
def get_phone(data):
    name = data[0]
    if name in contacts:
        return contacts[name]
    else:
        return 'Contact not found.'
    
def all():
    result = ''
    for user, phone in contacts.items():
        result += f'User:{user}, Phone:{phone}\n'
    return result

def main():
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, data = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(data))
        elif command == 'change':
            print(change_contact(data))
        elif command == 'phone':
            print(get_phone(data))
        elif command == 'all':
            print(all())
        else:
            print('Invalid command.')

if __name__ == "__main__":
    main()