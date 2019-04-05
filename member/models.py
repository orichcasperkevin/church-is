from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class MemberContact(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    postal = models.CharField(max_length=200, blank=True, verbose_name='Postal Address')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Telephone(Mobile)')
    contact = models.CharField(max_length=200, blank=True, verbose_name='Contact No.')

    def __str__(self):
        return str(self.member)

class MemberResidence(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    residence = models.CharField(max_length=200, blank=True, verbose_name='Residence/Estate')
    road = models.CharField(max_length=200, blank=True, verbose_name='Road/Street')

    def __str__(self):
        return str(self.member)


class Role(models.Model):
    '''
        roles that the members can have in the church
    '''
    role = models.CharField(max_length=20, default = "member")
    description = models.TextField(max_length=200)

    def get_role():
        '''
            returns the default role which is just a'member'
        '''
        return Role.objects.get(role = "member")

class MemberRole(models.Model):
    '''
        a member and the role they have , defualts to just 'member'
    '''
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,default = Role.get_role)

class Family(models.Model):
    '''
    a family  in church
    '''
    name = models.CharField(max_length = 50)
    head = models.ForeignKey(Member,on_delete= models.CASCADE,blank = True,related_name="familyHeads")
    members = models.ManyToManyField(Member,blank = True,related_name= "members")
