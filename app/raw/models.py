from django.db import models

# polls_test - mapeando los campos correctamente deacuerdo a nombre y tipo de columna
class Test(models.Model):    
    # int <type 'int'>
    iden = models.IntegerField(primary_key=True) # value: 1

    # unicode <type 'unicode'>
    code = models.CharField(max_length=4, unique=True) # value: u'0001'

    # unicode <type 'unicode'>
    name = models.CharField(max_length=50, db_column='fullname') # value: u'Antonio'

    # unicode <type 'unicode'>
    period = models.CharField(max_length=6, db_index=True) # value: u'201501'

    # unicode <type 'unicode'>
    dni = models.CharField(max_length=8, blank=True) # value: u'87654321'

    # unicode <type 'unicode'>
    email = models.EmailField(max_length=75, null=True) # value: u'anton@gmail.com'

    # unicode <type 'unicode'>
    comments = models.TextField(null=True) # value: u'nada que mostrar'

    # int <type 'int'>
    num = models.IntegerField(default=0, null=True) # value: 1

    # decimal.Decimal <class 'decimal.Decimal'>
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True) # value: Decimal('50.00')

    # decimal.Decimal <class 'decimal.Decimal'>
    vent = models.DecimalField(max_digits=13, decimal_places=4, null=True) # value: Decimal('80.0000')

    # float <type 'float'>
    total = models.FloatField(null=True) # value: 130.0

    # int <type 'int'>
    sec = models.SmallIntegerField(null=True) # value: 1

    # long <type 'long'>
    big = models.BigIntegerField(null=True) # value: 987654321L

    # bool <type 'bool'>
    flag = models.NullBooleanField() # value: True

    # bool <type 'bool'>
    active = models.BooleanField(default=True) # value: True

    # datetime.date <type 'datetime.date'>
    cum_date = models.DateField(null=True) # value: datetime.date(2015, 8, 8)

    # datetime.datetime <type 'datetime.datetime'>
    reg_date = models.DateTimeField(auto_now_add=True, null=True) # value: datetime.datetime(2015, 8, 31, 5, 21, 12, 97657, tzinfo=<UTC>)

    # unicode <type 'unicode'>
    reg_user = models.CharField(max_length=30, null=True) # value: u'me'

    # datetime.datetime <type 'datetime.datetime'>
    mod_date = models.DateTimeField(auto_now=True, null=True) # value: datetime.datetime(2015, 8, 31, 5, 21, 12, 97691, tzinfo=<UTC>)

    # unicode <type 'unicode'>
    mod_user = models.CharField(max_length=30, null=True) # value: u'me'

# si el campo viene de la bd con NULL en python seria del tipo: NoneType <type 'NoneType'> con valor: None
"""
como esta mapeado correctamete con los valores de la tabla "polls_test" se ejecuto la siguiente consulta en el shell
    test = Test.objects.raw('SELECT * FROM polls_test')
"""


# apprest_autor - mapeando los campos correctamente deacuerdo a nombre de columna
class Author (models.Model):
    id = models.TextField(primary_key=True) # django obliga a poner este attr "primary_key=True" si se usa como nombre de campo "id"
    nombre = models.TextField()
    apellido = models.TextField()
"""
luego de ejecutar desde el shell: aut = Author.objects.raw('SELECT * FROM apprest_autor')
el campo id que lo defini como text, al momento de ejcutar la consulta lo recupera como int
ya que en la bd esta como integer
type(aut[0].id) # <type 'int'>
"""

# apprest_libro - mapeando los campos correctamente deacuerdo a tipo de columna
class Book (models.Model):
    codigo = models.IntegerField()
    libro = models.TextField()
    edit = models.TextField()
    gene = models.TextField()
    cod_aut = models.IntegerField()
"""
para esta clase como no se especifica su pk en ningun campo, django le pone como campo "id" automaticamente
por eso obliga que el query retorne un campo id, se tuvo que hacer la siguiente consulta en el shell
    book = Book.objects.raw('SELECT id, id AS codigo, nombre AS libro, editorial AS edit, genero AS gene, autor_id AS cod_aut FROM apprest_libro')
los alias son para relacionar con los campos de la clase Book
otra solucion era porner al campo "codigo" el attr "primary_key=True" y la consulta quedaria:
    book = Book.objects.raw('SELECT id AS codigo, nombre AS libro, editorial AS edit, genero AS gene, autor_id AS cod_aut FROM apprest_libro')    
"""

# polls_question
class Pregunta (models.Model):
    cod = models.IntegerField()
    desc = models.TextField()
    pub = models.DateTimeField()
"""
el mismo problema que la clase Book, ya que no se especifico ningun pk, se tuvo que ejecutar la siguiente consulta en el shell
    qs = Pregunta.objects.raw('select id, id AS cod, question_text AS desc, pub_date AS pub from polls_question;')
"""

# polls_choice 
class Respuesta (models.Model):
    cod = models.IntegerField(primary_key=True)
    desc = models.TextField()
    votos = models.IntegerField()
    preg_cod = models.IntegerField()
"""
para esta clase no hubo problema en el query ya que se especifico su pk, se hizo la siguiente consulta
    rs = Respuesta.objects.raw('select id AS cod, choice_text AS desc, votes AS votos, question_id AS preg_cod FROM polls_choice')
apesar de que se especifico como pk el campo "cod", el resultser que retorna no necesariamente tiene que ser unicos el alias "cod"
por ejemplo se hizo esta siguiente consulta en el shell
    rs2 = Respuesta.objects.raw('select votes AS cod, choice_text AS desc, votes AS votos, question_id AS preg_cod FROM polls_choice')
el campo "votes" de la bd no es pk y obtenia valores repetidos en el resultado, a pesar que esta asociado a la prop "cod" que 
se definio como pk en la clase "Respuesta", no se genero problemas
"""

# clase compuesta para respuestas y preguntas
class RespuestaPregunta (models.Model):
    res = models.TextField(primary_key=True) # se define como pk para django no oblique que el query tenga un alias "id"
    votos = models.TextField()
    pre = models.TextField()
"""
    select choice_text as res, 
           votes as votos, 
           question_text as pre 
    from polls_choice r 
    inner join polls_question p on r.question_id = p.id;

consulta en el shell
    pr = RespuestaPregunta.objects.raw('select choice_text as res, votes as votos, question_text as pre from polls_choice r inner join polls_question p on r.question_id = p.id;')
"""

# clase compuesta para libros y autores
class BookAuthor (models.Model):
    libro = models.TextField(primary_key=True) # se define como pk para django no oblique que el query tenga un alias "id"
    edit = models.TextField()
    gen = models.TextField()
    autor = models.TextField()
"""
    select l.nombre as libro, 
           l.editorial as edit, 
           l.genero as gen, 
           a.nombre as autor 
    from apprest_libro l 
    right join apprest_autor a on l.autor_id = a.id;

consulta en el shell
    ba = BookAuthor.objects.raw('select l.nombre as libro, l.editorial as edit, l.genero as gen, a.nombre as autor from apprest_libro l right join apprest_autor a on l.autor_id = a.id')
si viene valores nullos en el resultado de la query, para la propiedad respectiva del tipo None , ejm:
en la tercera fila del resultado el campo libro es NULL, en el shel
    ba[2].libro
    type(ba[2].libro) # <type 'NoneType'>
    ba[2].libro is None # True        
"""
