#testemail.py
from wtforms import ValidationError

def IsUnique(form, field):
     if (len(field.data) % 2 == 1):
          raise ValidationError('email already exists')