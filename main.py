import sys

clients = [
	{
		'name': 'Pablo',
		'company': 'Google',
		'email': 'pablo@google.com',
		'position': 'Software Engineer' 
	},
	{
		'name': 'Ricardo',
                'company': 'Facebook',
                'email': 'ricardo@fabebook.com',
                'position': 'Data Engineer'
	},
]


def create_client(client):
	global clients
	if client not in clients:
		clients.append(client)
	else:
		print('Client already is in the client\'s list')


def list_clients(): 
	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(
            		uid=idx, 
	            	name=client['name'], 
           		company=client['company'], 
            		email=client['email'], 
            		position=client['position']))


def update_client(client_index, updated_client):
	global clients
	client_index = int(client_index)	

	if len(clients) -1 >= client_index:
		clients[client_index] = updated_client
	else:
		print('Client is not in clients list')

	list_clients()


def delete_client(client_index):
	global clients
	client_index = int(client_index)
	
	if len(clients) - 1 >= client_index:
		del clients[client_index]
	else:
		print('Client is not in clients list')


def search_client(client_name):
	for client in clients:
		if client['name'] != client_name:
			continue
		else:
			return True


def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[L]ist client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')

def _ask_for_client_data():
	client = {
                        'name': _get_client_field('name'),
                        'company': _get_client_field('company'),
                        'email': _get_client_field('email'),
                        'position': _get_client_field('position')
                }
	return client


def _get_client_field(field_name):
	field = None
	
	while not field:
		field = input(f'What is the client {field_name}? ')
	
	return field


if __name__ == '__main__':
	_print_welcome()
	
	command = input()
	command = command.upper()
	
	if command == 'C':
		client = _ask_for_client_data()
		create_client(client)
		list_clients()
	elif command == 'D':
		client_index = _get_client_field('index')
		delete_client(client_index)
		list_clients()
	elif command == 'L':
		list_clients()
	elif command == 'U':
		client_index = _get_client_field('index')
		updated_client_data = _ask_for_client_data()
		update_client(client_index, updated_client_data)
	elif command == 'S':
		client_name = _get_client_field('name')
		found = search_client(client_name)

		if found:
			print(f'The client \'{client_name}\' EXISTS in the client\'s list')
		else:
			print(f'The client \'{client_name}\' DOES NOT EXIST in the client\'s list')
	else:
		print('INVALID COMMAND')
