
def api(schema, *args):
    api = schema()
    method, name, passwd, email = args

    if 'POST' in method:
        post = api.post(name=name, passwd=passwd, email=email)
        next(post)  # Enviando objeto e aguardando sinal externo para concluir requisicão
        post.send('POST')  # Confirmando sinal externo
        print(post)
    
    elif 'GET' in method:
        get = api.get(name=name, passwd=passwd, email=email)
        next(get)
        get.send('GET')
        return print(get)

    elif 'PUT' in method:
        get = api.get(name='name', passwd='passwd', email='email')
        next(get)

        # Uma alteracão só pode ser feita após usuário 'LOGADO'
        get.send(('PUT', 'nama111', 'passwd111', 'email111'))
        get.send('GET')

    else:
        print('Method now allowed')
