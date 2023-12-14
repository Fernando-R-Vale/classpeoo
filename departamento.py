import json

class departamento:
  def __init__(self, id, nome, id_cursos, telefone):
    self.__id = id
    self.__nome = nome
    self.__id_cursos = id_cursos
    self.__telefone = telefone

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_id_cursos(self): return self.__id_cursos
  def get_telefone(self): return self.__telefone

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_id_cursos(self, id_cursos): self.__id_cursos = id_cursos
  def set_telefone(self, telefone): self.__telefone = telefone

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__id_cursos == x.__id_cursos and self.__telefone == x.__telefone:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__id_cursos} - {self.__telefone}"


class Ndepartamento:
  departamentos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.departamentos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.departamentos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.departamentos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.departamentos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_id_cursos(obj.get_id_cursos())
      aux.set_telefone(obj.get_telefone())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.departamentos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.departamentos = []
    try:
      with open("departamentos.json", mode="r") as arquivo:
        departamentos_json = json.load(arquivo)
        for obj in departamentos_json:
          aux = departamento(obj["_departamento__id"], obj["_departamento__nome"], obj["_departamento__id_cursos"], obj["_departamento__telefone"])
          cls.departamentos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("departamentos.json", mode="w") as arquivo:
      json.dump(cls.departamentos, arquivo, default=vars)
