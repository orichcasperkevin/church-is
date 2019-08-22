import os
import csv
import random
import datetime

from django.contrib.auth.models import User
from member.models import (Member, MemberContact, MemberAge, MemberResidence,
    Role, RoleMembership, MemberMaritalStatus, Family, FamilyMembership, )

class CSVLoader():

    errors = []

    def _check_names(self,file_name):
        '''
            check that the names are valid
        '''

        initial_dir = os.getcwd()
        os.chdir("Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    names =  row[0].split(" ")
                    if (len(names) == 1):
                        CSVLoader.errors.append("only one name given  at line " + str(line_count))
                    line_count += 1
            if (len(CSVLoader.errors) > 0):
                return False
            else:
                return True

    def _check_gender(self,file_name):
        initial_dir = os.getcwd()
        os.chdir("Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                gender = row[1]
                if line_count == 0:
                    line_count += 1
                else:
                    for data in gender.split(" "):
                        #ignore all white spaces
                        if (data != "M" and data != "F" and len(data) != 0):
                            CSVLoader.errors.append("expected M or F at line " + str(line_count))
                    line_count += 1
            if (len(CSVLoader.errors) > 0):
                return False
            else:
                return True

    def _check_d_o_b(self,file_name):
        '''
            check that the date input given is of correct format
        '''
        initial_dir = os.getcwd()
        os.chdir("Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                d_o_b = row[2]
                if line_count == 0:
                    line_count += 1
                else:
                    for data in d_o_b.split(" "):
                        #ignore all white spaces
                        if (len(data) != 10 and len(data) != 0):
                            CSVLoader.errors.append("incorrect date format at line " + str(line_count) + " use format YYYY-MM-DD")
                        if (len(data) == 10):
                            date = data.split("-")
                            year = date[0]
                            month = date[1]
                            day = date[2]
                            try:
                                datetime.datetime(int(year),int(month),int(day))
                            except ValueError:
                                CSVLoader.errors.append("incorrect date format at line " + str(line_count) + " use format YYYY-MM-DD")
                    line_count += 1
            if (len(CSVLoader.errors) > 0):
                return False
            else:
                return True

    def _check_phone_number(self,file_name):
        '''
            check that the phone number input provided is correct
        '''
        initial_dir = os.getcwd()
        os.chdir("Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                phone_number = row[3]
                if line_count == 0:
                    line_count += 1
                else:
                    for data in phone_number.split(" "):
                        #ignore all white spaces
                        if (len(data) != 10 and len(data) != 13 and len(data) != 0):
                            CSVLoader.errors.append("incorrect phone number format at line " + str(line_count) + " use format 0712345678")
                        if (len(data) == 10):
                            if(data[0] != "0"):
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count) + " use format 0712345678")
                            try:
                                int(int(data[1:10]))
                            except ValueError:
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count) + " use format 0712345678")

                        if (len(data) == 13):
                            if(data[0] != "+"):
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count) + " use format +254712345678")
                            try:
                                int(int(data[1:10]))
                            except ValueError:
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count) + " use format +254712345678")

                    line_count += 1
            if (len(CSVLoader.errors) > 0):
                return False
            else:
                return True

    def _check_marital_status(self,file_name):
        initial_dir = os.getcwd()
        os.chdir("Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                status = row[5]
                if line_count == 0:
                    line_count += 1
                else:
                    for data in status.split(" "):
                        #ignore all white spaces
                        if (data != "M" and data != "s" and data != "D" and data != "W" and len(data) != 0):
                            CSVLoader.errors.append("expected M,S,D or W at line " + str(line_count))
                    line_count += 1
            if (len(CSVLoader.errors) > 0):
                return False
            else:
                return True

    #TODO add regex to validate email
    def _check_email(self,file_name):
        '''
            check that the email input is of correct format
        '''
        initial_dir = os.getcwd()
        os.chdir("Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                email = row[4]
                if line_count == 0:
                    line_count += 1
                else:
                    for data in email.split(" "):
                        #ignore all white spaces
                        if (len(data) < 1 and len(data) != 0):
                            CSVLoader.errors.append("incorrect email format at line " + str(line_count) + " use format example@nano.com")
                    line_count += 1
            if (len(CSVLoader.errors) > 0):
                return False
            else:
                return True

    def _create_user(self, first_name, last_name, username, email):
        '''
            create a user from data from CSV
        '''
        username_does_not_exist = True
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(first_name=first_name, username=username, last_name=last_name, email=email)
            user.save()
            user.set_unusable_password()
            user_id = user.id
        else:
            username = username + str(random.choice(range(100)))
            user = User(first_name=first_name, username=username, last_name=last_name, email=email)
            user.save()
            user.set_unusable_password()
            user_id = user.id
        return user_id

    def _create_member(self,*var_tuple):
        '''
            create a member from a created user
        '''
        user_id = var_tuple[0]
        gender = var_tuple[1]
        #ignore all spaces before or after the gender input
        for data in gender.split(" "):
            if (data == "M" or data == "F"):
                gender = data
                break
        if (len(var_tuple) == 2):
            user = User.objects.get(id = user_id)
            member = Member.objects.create(member=user,gender=gender)
            return member.id

        if (len(var_tuple) == 3):
            middle_name = var_tuple[2]

            user = User.objects.get(id = user_id)
            member = Member.objects.create(member=user,gender=gender,middle_name=middle_name)
            return member.id

    def _set_date_of_birth(self, member_id, d_o_b):
        '''
            set a date of birth from data from the CSV
        '''
        #ignore all spaces, commas or full stops that may have been placed
        for data in d_o_b.split(" "):
            if (len(data)==10):
                d_o_b = data
                member = Member.objects.get(id=member_id)
                d_o_b = MemberAge.objects.create(member=member, d_o_b=d_o_b)
                break

    def _create_contact(self,member_id,phone_number):
        '''
            create contact for a member
        '''
        # ignore all spaces, commas or full stops that may be placed
        for data in phone_number.split(" "):
            if (len(data)==10 or len(data)==13):
                phone_number = data
        member = Member.objects.get(id=member_id)
        contact = MemberContact.objects.create(member=member, phone=phone_number)
        return contact

    def _create_marital_status(self,member_id,status):
        '''
            set marital status for member.
        '''
        # ignore all spaces, commas or full stops that may be placed
        for data in status.split(" "):
            if (data=="M" or data=="S" or data=="W" or data=="D"):
                status = data
        member = Member.objects.get(id=member_id)
        status = MemberMaritalStatus.objects.create(member=member, status=status)
        return status

    #public methods
    def check_CSV(self, file_name):
        '''
            check if CSV meets the required standards
        '''

        if (not self._check_names(file_name)):
            return False

        if (not self._check_gender(file_name)):
            return False

        if (not self._check_d_o_b(file_name)):
            return False

        if (not self._check_phone_number(file_name)):
            return False

        if (not self._check_email(file_name)):
            return False

        if (not self._check_marital_status(file_name)):
            return False

        return True

    def load(self, file_name):
        '''
            load a csv file and get its detail
        '''
        initial_dir = os.getcwd()
        os.chdir("Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            member_id = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    names =  row[0].split(" ")
                    gender = row[1]
                    d_o_b = row[2]
                    phone_number = row[3]
                    email = row[4]
                    marital_status = row[5]

                    if ( len(names) == 2 ):
                        first_name = names[0]
                        last_name = names[1]
                        username = '@' + first_name.lower() + last_name.lower()
                        user_id = self._create_user(first_name,last_name, username, email)
                        member_id = self._create_member(user_id,gender)

                    if ( len(names) == 3 ):
                        first_name = names[0]
                        middle_name = names[1]
                        last_name = names[2]
                        username = '@' + first_name.lower() + last_name.lower()
                        user_id = self._create_user(first_name,last_name, username, email)
                        member_id = self._create_member(user_id,gender,middle_name)

                    self._set_date_of_birth(member_id, d_o_b)
                    self._create_contact(member_id,phone_number)
                    self._create_marital_status(member_id,marital_status)