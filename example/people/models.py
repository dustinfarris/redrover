from django.db import models


class Person(models.Model):
  GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')]
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  age = models.IntegerField()
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

  def __unicode__(self):
    return self.full_name

  @models.permalink
  def get_absolute_url(self):
    return ('people:detail', (self.pk, ))


  @property
  def full_name(self):
    return '%s %s' % (self.first_name, self.last_name)

  def is_owner_of(self, pet):
    return pet in self.pets.all()


class Pet(models.Model):
  SPECIES_CHOICES = [
    ('Dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Bird', 'Bird')]
  name = models.CharField(max_length=20)
  species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
  owner = models.ForeignKey(Person, related_name='pets')
