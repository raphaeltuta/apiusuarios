from fastapi import FastAPI
from database import Usuarios, db
import uvicorn

app = FastAPI()
db.connect()
db.create_tables([Usuarios])

# Visualizar lista de usuarios
@app.get('/list/usuarios')
def lista_usuarios():
    usuarios = [usuario.__data__ for usuario in Usuarios.select()]
    if usuarios:
        return usuarios
    return {"error: Nenhum usuario Cadastrado"}

# Cadastrar os usuarios
@app.post('/post/usuario')
def cadastrar_usuario(nome: str, email: str, senha: str, funcao: str):
    try:
        usuario = Usuarios.create(nome=nome, email=email, senha=senha, funcao=funcao)
        return {'sucess':f'Usuario {usuario.nome} cadastrado com sucesso.'}
    except:
        return {'error': 'Não foi possivel cadastrar o usuario...'}
    
# ver detalhes dos usuarios
@app.get('/usuarios/{id}')
def ver_usuario(id: int):
    try:
        usuario = Usuarios.get(Usuarios.id == id)
        return {
            'id': usuario.id,
            'nome': usuario.nome,
            'funcao': usuario.funcao,
            'email': usuario.email,
            'senha': usuario.senha
        }
    except:
        return {"erro": "Usuário não encontrado."}

    
# editar usuario
@app.put('/edit/usuario/{id}')
def editar_usuario(id: int, nome: str, funcao: str, email: str, senha: str):
    try:
        usuario = Usuarios.get(Usuarios.id == id)
        usuario.nome = nome
        usuario.funcao = funcao
        usuario.email = email
        usuario.senha = senha

        usuario.save()
        return {'sucess':f'Usuario {usuario.nome} Editado com sucesso!'}
    except:
        return {'erro':'Tivemos um erro :('}
    
# deletar usuarios
@app.delete('/delet/usuarios/{user_id}')
def deletar_usuario(user_id: int):
    try:
        usuario = Usuarios.get(Usuarios.id == user_id)
        usuario.delete_instance()
        return {'sucess':f'Usuario {usuario.nome} deletado com sucesso!'}
    except:
        return {'erro':'Tivemos um erro...'}
    
uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
