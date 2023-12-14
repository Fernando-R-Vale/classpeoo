import json

class Agenda:
  def __init__(self, id, nome, local, id_departamento, telefone):
    self.__id = id
    self.__nome = nome
    self.__local = local
    self.__id_departamento = id_departamento
    self.__telefone = telefone

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_local(self): return self.__local
  def get_id_departamento(self): return self.__id_departamento
  def get_telefone(self): return self.__telefone

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_local(self, local): self.__local = local
  def set_id_departamento(self, id_departamento): self.__id_departamento = id_departamento
  def set_telefone(self, telefone): self.__telefone = telefone

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__local == x.__local and self.__id_departamento == x.__id_departamento and self.__telefone == x.__telefone:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__local} - {self.__id_departamento} - {self.__telefone}"

  def to_json(self):
    return {
      'id': self.__id,
      'nome': self.__nome,
      'local': self.__local,
      'id_departamento': self.__id_departamento,
      'telefone': self.__telefone}


class NUniversidades:
  __universisdades = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__universisdades:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__universisdades.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__universisdades

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__universisdades:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_local(obj.get_local())
      aux.set_id_departamento(obj.get_id_departamento())
      aux.set_telefone(obj.get_telefone())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__universisdades.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__universisdades = []
    try:
      with open("universisdades.json", mode="r") as arquivo:
        universisdades_json = json.load(arquivo)
        for obj in universisdades_json:
          aux = Agenda(
            obj["id"],
            obj["nome"],
            obj["local"], obj["id_departamento"], obj["telefone"])
          cls.__universisdades.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("universisdades.json", mode="w") as arquivo:
      json.dump(cls.__universisdades, arquivo, default=Agenda.to_json)
