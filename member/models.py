from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Member(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=15, blank=True,  default=" ")
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('R', 'Rather not say'),
    )
    gender = models.CharField(max_length=2, null=True, blank=True, choices=GENDER)

    class Meta:
        indexes = [
            models.Index(fields=['gender']),
        ]


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
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    )
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, null=True, choices=STATUS)


class MemberResidence(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    town = models.CharField(max_length=15, blank=True, verbose_name='town')
    road = models.CharField(max_length=15, blank=True, verbose_name='Road')
    street = models.CharField(max_length=15, blank=True, verbose_name='street')
    village_estate = models.CharField(max_length=15, blank=True, verbose_name='village/estate')
    description = models.CharField(max_length=30, blank=True, verbose_name='description')

    def __str__(self):
        return str(self.member)


class Role(models.Model):
    '''
        roles that the members can have in the church
    '''
    id = models.AutoField(primary_key=True)
    member_admin = models.BooleanField(default=False)
    site_admin = models.BooleanField(default=False)
    group_admin = models.BooleanField(default=False)
    event_admin = models.BooleanField(default=False)
    projects_admin = models.BooleanField(default=False)
    finance_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=20, default="member")
    description = models.TextField(max_length=30,blank=True,null=True)

class RoleMembership(models.Model):
    '''
        a membership roster for used for adding members to a role
    '''
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Family(models.Model):
    '''
        a family  in church
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    head = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name="familyHeads")
    members = models.ManyToManyField(Member, through='FamilyMembership')

class FamilyMembership(models.Model):
    '''
        a member in a family
    '''
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

class ParentRelation(models.Model):
    '''
         member - parent relation
    '''
    member = models.OneToOneField(Member,on_delete=models.CASCADE)
    mom = models.ForeignKey(Member,on_delete=models.CASCADE, blank=True, null=True, related_name="moms")
    dad = models.ForeignKey(Member,on_delete=models.CASCADE, blank=True, null=True, related_name="dads")

class SiblingRelation(models.Model):
    '''
        Member - sibling relation
    '''
    member = models.OneToOneField(Member,on_delete=models.CASCADE)
    sibling = models.ForeignKey(Member,on_delete=models.CASCADE, related_name="siblings")

class SpouseRelation(models.Model):
    '''
        Member - spouse relation
    '''
    member = models.OneToOneField(Member,on_delete=models.CASCADE)
    spouse = models.ForeignKey(Member,on_delete=models.CASCADE, related_name="spouses")

class ImportantDateType(models.Model):
    '''
        a type of date that is marked by the church for its members
    '''
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=160)

class MemberImportantDate(models.Model):
    '''
        important date for member
    '''
    type = models.ForeignKey(ImportantDateType, on_delete=models.CASCADE, blank=True, null=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    description = models.CharField(max_length=160)
    overseen_by_member = models.ForeignKey(Member,on_delete=models.CASCADE, blank=True, null=True,related_name="overseer")
    overseen_by_non_member = models.CharField(max_length=50, blank=True, null=True)
    non_member_description = models.CharField(max_length=160, blank=True, null=True)


class CSV(models.Model):
    '''
        csv for importing Member data
    '''
    csv = models.FileField(upload_to='Resources/',null=True)
