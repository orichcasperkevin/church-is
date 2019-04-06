from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class MemberContact(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    postal = models.CharField(max_length=200, blank=True, verbose_name='Postal Address')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Telephone(Mobile)')
    contact = models.CharField(max_length=200, blank=True, verbose_name='Contact No.')

    def __str__(self):
        return str(self.member)

class MemberAge(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    d_o_b = models.DateField()

class MemberMaritalStatus(models.Model):
    STATUS = (
        ('M', 'Married'),
        ('S', 'Single'),
    )
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, null=True, choices=STATUS)

class MemberResidence(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    town = models.CharField(max_length=200, blank=True, verbose_name='town')
    road = models.CharField(max_length=200, blank=True, verbose_name='Road')
    street = models.CharField(max_length=200, blank=True, verbose_name='street')
    village_estate = models.CharField(max_length=200, blank=True, verbose_name='village/estate')
    description = models.CharField(max_length=200, blank=True, verbose_name='description')
     

    def __str__(self):
        return str(self.member)


class Role(models.Model):
    '''
        roles that the members can have in the church
    '''
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,default = Role.get_role)

class Family(models.Model):
    '''
    a family  in church
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    head = models.ForeignKey(Member,on_delete= models.CASCADE,blank = True,related_name="familyHeads")

class FamilyMember(models.Model):
    '''
        a member in a family
    '''
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    family = models.ForeignKey(Family,on_delete=models.CASCADE)
