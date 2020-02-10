from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Member(models.Model):
    ##fundamental design flaw at the beginning of the project...should've  used OneToOneField
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

    def __str__(self):
        return str(self.member.first_name + " " + self.member.last_name )


class MemberContact(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=15, blank=True, verbose_name='Telephone(Mobile)')
    phone2 = models.CharField(max_length=15, blank=True, verbose_name='Telephone(Mobile)')

    def __str__(self):
        return str(self.member)


class MemberAge(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE,null=True)
    d_o_b = models.DateField(null=True)

    def __str__(self):
        return str(self.member)

class MemberMaritalStatus(models.Model):
    STATUS = (
        ('M', 'Married'),
        ('S', 'Single'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    )
    member = models.OneToOneField(Member, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, null=True, choices=STATUS)


class MemberResidence(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE, null=True)
    town = models.CharField(max_length=15, blank=True, verbose_name='town')
    road = models.CharField(max_length=15, blank=True, verbose_name='Road')
    street = models.CharField(max_length=15, blank=True, verbose_name='street')
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
    members = models.ManyToManyField(Member, through='FamilyMembership')

class FamilyMembership(models.Model):
    '''
        a member in a family
    '''
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

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

class MemberNote(models.Model):
    '''
        notes made on a member.
    '''
    member = models.ForeignKey(Member,on_delete=models.CASCADE, related_name='mote_for')
    note_by = models.ForeignKey(Member,on_delete=models.CASCADE, related_name='note_by')
    note = models.CharField(max_length=160)

class CSV(models.Model):
    '''
        csv for importing Member data
    '''
    csv = models.FileField(upload_to='Resources/',null=True)
