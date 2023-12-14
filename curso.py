import json

class curso:
  def __init__(self, id, nome, professores, vagas, nivel):
    self.__id = id
    self.__nome = nome
    self.__professores = professores
    self.__vagas = vagas
    self.__nivel = nivel

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_professores(self): return self.__professores
  def get_vagas(self): return self.__vagas
  def get_nivel(self): return self.__nivel

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_professores(self, professores): self.__professores = professores
  def set_vagas(self, vagas): self.__vagas = vagas
  def set_nivel(self, nivel): self.__nivel = nivel

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__professores == x.__professores and self.__vagas == x.__vagas and self.__nivel == x.__nivel:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__professores} - {self.__vagas} - {self.__nivel}"


class Ncurso:
  __cursos = [] 

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0 
    for aux in cls.__cursos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__cursos.append(obj)  
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__cursos  

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__cursos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_professores(obj.get_professores())
      aux.set_vagas(obj.get_vagas())
      aux.set_nivel(obj.get_nivel())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__cursos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__cursos = []
    try:
      with open("cursos.json", mode="r") as arquivo:
        cursos_json = json.load(arquivo)
        for obj in cursos_json:
          aux = curso(obj["_curso__id"], obj["_curso__nome"], obj["_curso__professores"], obj["_curso__vagas"], obj["_curso__nivel"])
          cls.__cursos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("cursos.json", mode="w") as arquivo:
      json.dump(cls.__cursos, arquivo, default=vars)
