from rest_framework.views import APIView
from datetime import date

from rest_framework.response import Response
from rest_framework.views import APIView

from member.api.serializers import (MemberSerializer, MemberContactSerializer,
    MemberResidenceSerializer, RoleMemberShipSerializer,MemberMaritalStatusSerializer,
    FamilyMembershipSerializer, )

from member.models import (Member, MemberContact, MemberAge,
    MemberResidence, RoleMembership,MemberMaritalStatus, FamilyMembership, ParentRelation,
    SiblingRelation, SpouseRelation)

from member.resources.importCSV import CSVLoader
loader = CSVLoader()

class GetMemberWithId(APIView):
    '''
        get:
        get a member with id <id>
    '''

    def get(self, request, id):
        member = Member.objects.filter(member__id=id)
        data = MemberSerializer(member, many=True).data
        return Response(data)


class GetMemberWithUsername(APIView):
    '''
        get:
        get a member with username
    '''

    def get(self, request, username):
        member = Member.objects.filter(member__username=username)

        data = MemberSerializer(member, many=True).data
        return Response(data)


class GetContactForMemberWithId(APIView):
    '''
        get:
        get a contact for a member with id <id>
    '''

    def get(self, request, id):
        contact = MemberContact.objects.filter(member__member__id=id)

        data = MemberContactSerializer(contact, many=True).data
        return Response(data)


class GetAgeForMemberWithId(APIView):
    '''
        get:
        get age for a member with id <id>
        and date of birth
    '''

    def get(self, request, id):
        age = MemberAge.objects.get(member__member__id=id)

        today = date.today()
        data = today.year - age.d_o_b.year - ((today.month, today.day) < (age.d_o_b.month, age.d_o_b.day))
        age_dict = {"age": '', "d_o_b": ''}
        age_dict["age"] = data
        age_dict["d_o_b"] = age.d_o_b

        data = age_dict

        return Response(data)


class GetResidenceForMemberWithId(APIView):
    '''
        get:
        get a residence for a member with id <id>
    '''

    def get(self, request, id):
        residence = MemberResidence.objects.filter(member__member__id=id)

        data = MemberResidenceSerializer(residence, many=True).data
        return Response(data)


class GetMaritalStatusForMemberWithId(APIView):
    '''
        get:
        get marital status for a member with id <id>
    '''

    def get(self, request, id):
        residence = MemberMaritalStatus.objects.filter(member__member__id=id)

        data = MemberMaritalStatusSerializer(residence, many=True).data
        return Response(data)


class GetFamilyForMemberWithId(APIView):
    '''
        get:
        get the family members of the family the member belongs to
    '''

    def get(self, request, id):
        family_membership = FamilyMembership.objects.filter(member__member__id=id)

        data = FamilyMembershipSerializer(family_membership, many=True).data
        return Response(data)

class GetMemberFamilyTree(APIView):
    '''
        get:
        get the family tree for a member
    '''
    def __init__(self):
        self.current_node = 0
        self.root = 0
        self.level = 0
        self.family_tree = []

    def _node_has_parent(self,member_id):
        '''check if a node has a parent node'''
        try:
            parent = ParentRelation.objects.get(member__member__id=member_id)
        except ParentRelation.DoesNotExist:
            return False
        else:
            try:
                self.current_node = parent.dad.member.id
            except:
                self.current_node = parent.mom.member.id
            return True

    def _get_family_tree_root(self, member_id):
        '''get the root of the family tree'''
        if (self._node_has_parent(member_id) == False):
            root = member_id
        else:
            root = self._get_family_tree_root(self.current_node)
        return root

    def _grow_family_tree(self, root):
        '''starting from the root, grow family root until all its leaves'''

        node = {'level':self.level, 'member': None, 'spouse': None, 'children': []}

        #get root's  member
        member = Member.objects.get(member__id=root)
        member = member.member.first_name + ' ' +member.member.last_name

        #get root's spouse
        try:
            spouse_relation = SpouseRelation.objects.get(member__member__id=root)
        except SpouseRelation.DoesNotExist:
            spouse = None
        else:
            spouse = spouse_relation.spouse.member.first_name + ' '+ spouse_relation.spouse.member.last_name

        node['member'] = member
        node['spouse'] = spouse

        #get root's children
        children = []
        parent_relation = ParentRelation.objects.filter(mom__member__id=root)
        if (len(parent_relation) > 0):
            self.level += 1
            # if root has any children
            for data in parent_relation:
                node['children'].append(data.member.member.first_name +' '+data.member.member.last_name)
                self.family_tree.append({'member': node})
                self._grow_family_tree(data.member.member.id)

        else:
            parent_relation = ParentRelation.objects.filter(dad__member__id=root)
            if (len(parent_relation) > 0):
                self.level += 1
                for data in parent_relation:
                    node['children'].append(data.member.member.first_name+' '+data.member.member.last_name)
                    self.family_tree.append({'member': node})
                    self._grow_family_tree(data.member.member.id)

            if(len(parent_relation) == 0):
                    self.family_tree.append({'member': node})

    def get(self,request,id):
        member = Member.objects.get(member__id=id)
        self.root = self._get_family_tree_root(member.member.id)
        self._grow_family_tree(self.root)

        data = self.family_tree

        return Response(data)

class GetRolesForMemberWithId(APIView):
    '''
        get:
        get the role groups the member belongs to
    '''

    def get(self, request, id):
        role_membership = RoleMembership.objects.filter(member__member__id=id)

        data = RoleMemberShipSerializer(role_membership, many=True).data
        return Response(data)

class PreviewCSV(APIView):
    '''
        get:
        get csv data for preview in the UI
    '''

    def get(self, request, file_name):
        data = loader.preview_CSV(file_name)
        return Response(data)
