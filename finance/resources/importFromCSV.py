import os
import csv
import random
import datetime

from django.contrib.auth.models import User
from member.models import *

class CSVLoader():
    errors = []
    gender_column = None
    marital_status_column = None
    email_column = None
    phone_number_column = None
    names_column = None
    date_of_birth_column = None
    BASE_URL = ''

    def _check_names(self,file_name):
        '''
            check that the names are valid
        '''

        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL+"Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    names =  row[self.names_column].strip()
                    names =  names.split(" ")
                    if (len(names) == 1):
                        CSVLoader.errors.append("only one name given  at line " + str(line_count + 1))
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
        os.chdir(self.BASE_URL+"Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                d_o_b = row[self.date_of_birth_column]
                if line_count == 0:
                    line_count += 1
                else:
                    for data in d_o_b.split(" "):
                        #ignore all white spaces
                        if (len(data) != 10 and len(data) != 0):
                            CSVLoader.errors.append("incorrect date format at line " + str(line_count + 1) + " use format YYYY-MM-DD")
                        if (len(data) == 10):
                            try:
                                date = data.split("-")
                                year = date[0]
                                month = date[1]
                                day = date[2]
                                datetime.datetime(int(year),int(month),int(day))
                            except:
                                CSVLoader.errors.append("incorrect date format at line " + str(line_count + 1) + " use format YYYY-MM-DD")
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
        os.chdir(self.BASE_URL+"Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            CSVLoader.errors = []
            for row in csv_reader:
                phone_number = row[self.phone_number_column]
                if line_count == 0:
                    line_count += 1
                else:
                    for data in phone_number.split(" "):
                        #ignore all white spaces
                        if (len(data) != 10 and len(data) != 13 and len(data) != 0):
                            CSVLoader.errors.append("incorrect phone number format at line " + str(line_count + 1) + " use format 0712345678")
                        if (len(data) == 10):
                            if(data[0] != "0"):
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count + 1) + " use format 0712345678")
                            try:
                                int(int(data[1:10]))
                            except ValueError:
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count + 1) + " use format 0712345678")

                        if (len(data) == 13):
                            if(data[0] != "+"):
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count + 1) + " use format +254712345678")
                            try:
                                int(int(data[1:10]))
                            except ValueError:
                                CSVLoader.errors.append("incorrect phone number format at line " + str(line_count + 1) + " use format +254712345678")

                    line_count += 1
            if (len(CSVLoader.errors) > 0):
                return False
            else:
                return True

    def _create_user(self, first_name, last_name, username, email):
        '''
            create a user from data from CSV
        '''
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

        if (len(var_tuple) > 2):
            middle_name = var_tuple[2]

            user = User.objects.get(id = user_id)
            member = Member.objects.create(member=user,gender=gender,middle_name=middle_name)
            return member.id

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

    #public methods
    def set_base_url(self,base_url):
        self.BASE_URL = base_url.split(':')[0] + "/"

    def preview_CSV(self, file_name):
        '''
            return the csv as json for preview in the UI
        '''
        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL+"Resources")

        data = []
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.DictReader(csv_file,delimiter=',')
            row = {}
            count = 0
            for row in csv_reader:
                if count < 5:
                    row = row
                    data.append(row)
                    count += 1
                else:
                    break
        return data

    def configure_CSV(self, file_name, config_tuple):
        '''
            configure the csv file columns according to specifications by the config_tuple
        '''
        self.gender_column = None
        self.marital_status_column = None
        self.email_column = None
        self.phone_number_column = None
        self.names_column = None
        self.date_of_birth_column = None

        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL+"Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    for key in config_tuple:
                        for i in range(0,len(row)):
                            if row[i].strip() == key.strip():
                                if config_tuple[key] == 'gender':
                                    self.gender_column = i
                                if config_tuple[key] == 'marital status':
                                    self.marital_status_column = i
                                if config_tuple[key] == 'email':
                                    self.email_column = i
                                if config_tuple[key] == 'phone number':
                                    self.phone_number_column = i
                                if config_tuple[key] == 'names':
                                    self.names_column = i
                                if config_tuple[key] == 'date of birth':
                                    self.date_of_birth_column = i
                else:
                    break
                line_count += 1

    def check_CSV(self, file_name):
        '''
            check if CSV meets the required standards
        '''
        if (not self._check_names(file_name)):
            return False

        if (self.date_of_birth_column != None):
            if (not self._check_d_o_b(file_name)):
                return False

        if (self.phone_number_column != None):
            if (not self._check_phone_number(file_name)):
                return False
        #if everything is okay then return True
        return True

    # TODO: review length of this function
    def load(self, file_name):
        '''
            load a csv file and get its detail
        '''
        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL + "Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            member_id = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    names =  row[self.names_column].strip()
                    names =  names.split(" ")

                    gender = None
                    if (self.gender_column != None):
                        gender = row[self.gender_column]

                    d_o_b = None
                    if (self.date_of_birth_column != None):
                        d_o_b = row[self.date_of_birth_column]

                    phone_number = None
                    if (self.phone_number_column != None):
                        phone_number = row[self.phone_number_column]

                    email = ''
                    if (self.email_column != None):
                        email = row[self.email_column]

                    marital_status = None
                    if (self.marital_status_column != None):
                        marital_status = row[self.marital_status_column]

                    if ( len(names) == 2 ):
                        first_name = names[0]
                        last_name = names[1]
                        username = first_name.lower() + last_name.lower()
                        username = username.replace("'", "")
                        username = username.replace(".", "")
                        user_id = self._create_user(first_name,last_name, username, email)
                        member_id = self._create_member(user_id,gender)

                    if ( len(names) > 2 ):
                        first_name = names[0]
                        middle_name = names[1]
                        last_name = names[2]
                        username = first_name.lower() + last_name.lower()
                        username = username.replace("'", "")
                        username = username.replace(".", "")
                        user_id = self._create_user(first_name,last_name, username, email)
                        member_id = self._create_member(user_id,gender,middle_name)

                    if (self.date_of_birth_column != None):
                        self._set_date_of_birth(member_id, d_o_b)

                    if (self.phone_number_column != None):
                        self._create_contact(member_id,phone_number)

                    if (self.marital_status_column != None):
                        self._create_marital_status(member_id,marital_status)
