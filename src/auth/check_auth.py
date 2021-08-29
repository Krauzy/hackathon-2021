def get_auth(id):
    if id == '123':
        return 'pacient'
    elif id =='321':
        return 'fisio'
    else:
        return None

def set_key(id):
    file = open('.key', 'w')
    file.write(id)
    file.close()

def get_key():
    file = open('.key')
    content = file.read()
    file.close()
    return content