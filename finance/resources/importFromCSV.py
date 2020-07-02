import os
import csv
import random
import datetime

from django.contrib.auth.models import User
from member.models import *

from finance.models import ModeOfPayment,OfferingType,Offering,Tithe

class CSVLoader():
    def __init__(self):
        self.errors = []
        self.amount_column = None
        self.payment_method_column = None
        self.offering_type_column = None
        self.phone_number_column = None
        self.names_column = None
        self.date_column = None
        self.BASE_URL = ''

    def _check_size_of_file(self,file_name):
        '''
            check that the file has a decent amount of rows.
        '''

        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL+"Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            self.errors = []
            for row in csv_reader:
                if any(row):
                    if line_count == 0:
                        line_count += 1
                    else:
                        line_count += 1

            if line_count > 250:
                self.errors.append("File has too many rows ("\
                                    + str(line_count + 1)\
                                    + ") expected 250 or less")

            if (len(self.errors) > 0):
                return False
            else:
                return True

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
            self.errors = []
            for row in csv_reader:
                if any(row):
                    if line_count == 0:
                        line_count += 1
                    else:
                        names =  row[self.names_column].strip()
                        names =  names.split(" ")
                        if (len(names) == 1):
                            self.errors.append("got only one name ("\
                                                + names[0] \
                                                + " ) at line "\
                                                + str(line_count + 1)\
                                                + " expected two or more")
                        line_count += 1

            if (len(self.errors) > 0):
                return False
            else:
                return True

    def _check_date(self,file_name):
        '''
            check that the date input given is of correct format
        '''
        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL+"Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            self.errors = []
            for row in csv_reader:
                if any(row):
                    date = row[self.date_column]
                    if line_count == 0:
                        line_count += 1
                    else:
                        date = date.strip()
                        #ignore all white spaces
                        if (len(date) != 10 and len(date) != 0):
                            self.errors.append("incorrect date format ("\
                                                + date \
                                                + " ) at line "\
                                                + str(line_count + 1) \
                                                + " use format DD/MM/YYYY")
                        #if it is corrects length
                        if (len(date) == 10):
                            date = date.split("/")
                            year = date[2]
                            month = date[1]
                            day = date[0]
                            try:
                                datetime.datetime(int(year),int(month),int(day))
                            except:
                                self.errors.append("incorrect date format ("\
                                                    + date \
                                                    + " ) at line "\
                                                    + str(line_count + 1)\
                                                    + " use format DD/MM/YYYY")
                        #increment line count
                        line_count += 1

            if (len(self.errors) > 0):
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
            self.errors = []
            for row in csv_reader:
                if any(row):
                    phone_number = row[self.phone_number_column]
                    if line_count == 0:
                        line_count += 1
                    else:
                        phone_number = phone_number.strip()
                        #ignore all white spaces
                        if (    len(phone_number) != 10
                            and len(phone_number) != 9#when the leading zero was left out
                            and len(phone_number) != 0):
                            self.errors.append("incorrect phone number format ("\
                                                + phone_number \
                                                + " ) at line "\
                                                + str(line_count + 1) \
                                                + " use format 0712345678")

                        if (len(phone_number) == 10):
                            if(phone_number[0] != "0"):
                                self.errors.append("incorrect phone number format ("\
                                                    + phone_number \
                                                    + " ) at line "\
                                                    + str(line_count + 1)\
                                                    + " use format 0712345678")
                            # check that they are all numbers
                            try:
                                int(int(phone_number[1:10]))
                            except ValueError:
                                self.errors.append("incorrect phone number format ("\
                                                    + phone_number \
                                                    + " ) at line "\
                                                    + str(line_count + 1)\
                                                    + " use format 0712345678")
                        if (len(phone_number) == 9):
                            try:
                                int(int(phone_number[0:8]))
                            except ValueError:
                                self.errors.append("incorrect phone number format ("\
                                                    + phone_number \
                                                    + " ) at line "\
                                                    + str(line_count + 1) \
                                                    + " use format 712345678")
                        line_count += 1

            if (len(self.errors) > 0):
                return False
            else:
                return True

    def _check_amount(self,file_name):
        '''
            check that the amount given are correct
        '''
        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL + "Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            self.errors = []
            for row in csv_reader:
                if any(row):
                    amount = row[self.amount_column]
                    if line_count == 0:
                        line_count += 1
                    else:
                        amount = amount.strip()
                        try:
                            amount = str(amount)
                            amount = amount.replace(',','')#remove commas and try converting to int
                            int(int(amount))
                        except ValueError:
                            self.errors.append("incorrect amount format ("\
                                                + amount \
                                                + " )at line "\
                                                + str(line_count + 1)\
                                                + " use integer format for amounts")
                        line_count += 1

            if (len(self.errors) > 0):
                return False
            else:
                return True

    def _check_payment_method(self,file_name):
        '''
            check that the payment methods given are correct
        '''
        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL + "Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            self.errors = []
            for row in csv_reader:
                if any(row):
                    payment_method = row[self.payment_method_column]
                    if line_count == 0:
                        line_count += 1
                    else:
                        payment_method = payment_method.strip()
                        # if a mode of payment with this name does not exist
                        if not ModeOfPayment.objects.filter(name__icontains = payment_method).exists():
                            self.errors.append("payment method ( "\
                                                + payment_method \
                                                + " )does not exist, line"\
                                                + str(line_count + 1)\
                                                + " You may need to add this payment method")
                        line_count += 1

            if (len(self.errors) > 0):
                return False
            else:
                return True

    def _check_offering_type(self,file_name):
        '''
            check that the payment methods given are correct
        '''
        initial_dir = os.getcwd()
        os.chdir(self.BASE_URL + "Resources")
        with open(file_name) as csv_file:
            os.chdir(initial_dir)
            csv_reader = csv.reader(csv_file,delimiter=',')
            line_count = 0
            self.errors = []
            for row in csv_reader:
                offering_type = row[self.offering_type_column]
                if line_count == 0:
                    line_count += 1
                else:
                    offering_type = offering_type.strip()
                    # if type is not tithe then check if offering type exists
                    if  (   offering_type != 'Tithe'
                        and offering_type != 'tithe'
                        and offering_type != 'tithes'
                        and offering_type != 'Tithes'):
                        # if an offering type with this name does not exist
                        if not OfferingType.objects.filter(name__icontains = offering_type)\
                                                   .exists():
                            self.errors.append("envelope Type ( "\
                                                + offering_type\
                                                + " ) does not exist, line"\
                                                + str(line_count + 1)\
                                                + " You may need to add envelope type")
                    line_count += 1

            if (len(self.errors) > 0):
                return False
            else:
                return True

    def _create_user(self, first_name, last_name, username):
        '''
            create a user from data from CSV
        '''
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(first_name=first_name, username=username,
                        last_name=last_name)
            user.save()
            user.set_unusable_password()
            user_id = user.id
        else:
            username = username + str(random.choice(range(100)))
            user = User(first_name=first_name, username=username,
                        last_name=last_name)
            user.save()
            user.set_unusable_password()
        return user

    def _create_member(self,*var_tuple):
        '''
            create a member from a created user
        '''
        user = var_tuple[0]
        #ignore all spaces before or after the gender input
        if (len(var_tuple) == 1):
            member = Member.objects.create(member=user)
            return member

        if (len(var_tuple) > 1):
            middle_name = var_tuple[1]

            user = User.objects.get(id = user_id)
            member = Member.objects.create(member=user,middle_name=middle_name)
            return member

    def _create_contact(self,member,phone_number):
        '''
            create contact for a member
        '''
        # ignore all spaces, commas or full stops that may be placed
        phone_number =  phone_number.strip()
        if len(phone_number)==10 or len(phone_number) == 13 :
            phone_number = str(phone_number)

        if len(phone_number) == 9:
            phone_number = '0'+ str(phone_number)

        contact = MemberContact.objects.create(member=member, phone=phone_number)
        return contact

    def _member_from_phone_number(self,phone_number):
        if len(phone_number) == 10:
            if MemberContact.objects.filter(phone__contains=phone_number[1:10])\
                                    .exists():
                contact =  MemberContact.objects.filter(phone__contains=phone_number[1:10])[0]
                return contact.member
            else:
                return None

        if len(phone_number) == 9:
            if MemberContact.objects.filter(phone__contains=phone_number[1:9])\
                                    .exists():
                contact =  MemberContact.objects.filter(phone__contains=phone_number[1:9])[0]
                return contact.member
            else:
                return None

    def _member_from_names(self,names):
        if ( len(names) == 2 ):
            first_name = names[0]
            last_name = names[1]
            username = first_name.lower() + last_name.lower()
            username = username.replace("'", "")
            username = username.replace(".", "")
            user = self._create_user(first_name,last_name, username)
            member = self._create_member(user)
            return member

        if ( len(names) > 2 ):
            first_name = names[0]
            middle_name = names[1]
            last_name = names[2]
            username = first_name.lower() + last_name.lower()
            username = username.replace("'", "")
            username = username.replace(".", "")
            user = self._create_user(first_name,last_name, username)
            member = self._create_member(user,middle_name)
            return member

    def _add_tithe_or_offering(self,amount,payment_method,type,date,member,
                              name_if_not_member,phone_if_not_member):
        if  (   type == 'Tithe'
            or type == 'tithe'
            or type == 'tithes'
            or type == 'Tithes'):
            try:
                Tithe.objects.create(
                    mode_of_payment = payment_method,
                    amount = amount,
                    member = member,
                    name_if_not_member = name_if_not_member,
                    phone_if_not_member = phone_if_not_member,
                    date = date
                )
            except:
                pass
        else:
            try:
                offering_type = OfferingType.objects.filter(name__icontains=type).first()
                if offering_type:
                    offering_type = offering_type
                else:
                    offering_type = None

                Offering.objects.create(
                    type = offering_type,
                    mode_of_payment = payment_method,
                    amount = amount,
                    member = member,
                    name_if_not_member = name_if_not_member,
                    phone_if_not_member = phone_if_not_member,
                    date = date
                )
            except:
                pass

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
                if count < 200:
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
        self.amount_column = None
        self.payment_method_column = None
        self.offering_type_column = None
        self.phone_number_column = None
        self.names_column = None
        self.date_column = None

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
                                if config_tuple[key] == 'amount':
                                    self.amount_column = i
                                if config_tuple[key] == 'payment method':
                                    self.payment_method_column = i
                                if config_tuple[key] == 'type':
                                    self.offering_type_column = i
                                if config_tuple[key] == 'phone number':
                                    self.phone_number_column = i
                                if config_tuple[key] == 'names':
                                    self.names_column = i
                                if config_tuple[key] == 'date':
                                    self.date_column = i
                else:
                    break
                line_count += 1

    def check_CSV(self, file_name):
        '''
            check if CSV meets the required standards
        '''
        if (not self._check_size_of_file(file_name)):
            return False

        if (not self._check_names(file_name)):
            return False

        if (not self._check_date(file_name)):
            return False

        if (not self._check_amount(file_name)):
            return False

        if (self.phone_number_column != None):
            if (not self._check_phone_number(file_name)):
                return False

        if (not self._check_offering_type(file_name)):
            return False

        if (self.payment_method_column != None):
            if (not self._check_payment_method(file_name)):
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
                    #get amount
                    amount = None
                    if (self.amount_column != None):
                        amount = row[self.amount_column]
                        amount = str(amount)
                        amount = int(amount.replace(',',''))
                    # get payment_method
                    payment_method = None
                    if (self.payment_method_column != None):
                        payment_method = row[self.payment_method_column]
                        payment_method = payment_method.strip()
                        if len(payment_method):
                            payment_method = ModeOfPayment.objects.filter(name__icontains=payment_method).first()
                            if payment_method:
                                payment_method = payment_method
                        else:
                            payment_method = None
                    # get offering types
                    offering_type = None
                    if (self.offering_type_column != None):
                        offering_type = row[self.offering_type_column]
                        offering_type =  offering_type.strip()
                    # get phone_number
                    phone_number = None
                    if (self.phone_number_column != None):
                        phone_number = row[self.phone_number_column]
                    # get date
                    date = None
                    if (self.date_column != None):
                        date = row[self.date_column]
                        date = date.split("/")
                        year = date[2]
                        month = date[1]
                        day = date[0]
                        date = datetime.datetime(int(year),int(month),int(day))
                    # get names
                    names =  row[self.names_column].strip()
                    names =  names.split(" ")

                    #try getting user by their phone number.
                    if phone_number:
                        member = self._member_from_phone_number(phone_number)
                        if member:
                            self._add_tithe_or_offering(
                                int(amount),#amount
                                payment_method,#payment_method
                                offering_type,#type
                                date,#date
                                member,#member
                                None,#name_if_not_member =
                                None #phone_if_not_memmber
                            )
                            continue

                    if len(names) > 1:
                        member = self._member_from_names(names)
                        if member and self.phone_number_column:
                            self._create_contact(member,phone_number)
                            #add tithe or offering
                            self._add_tithe_or_offering(
                                int(amount),#amount
                                payment_method,#payment_method
                                offering_type,#type
                                date,#date
                                member,#member
                                None,#name_if_not_member =
                                None #phone_if_not_memmber
                            )
                            continue
                        else:
                            self._add_tithe_or_offering(
                                int(amount),#amount
                                payment_method,#payment_method
                                offering_type,#type
                                date,#date
                                None,#member
                                names[0] + " " + names[1],#name_if_not_member =
                                None #phone_if_not_memmber
                            )
                            continue

                    if len(names) == 1:
                        self._add_tithe_or_offering(
                            int(amount),#amount
                            payment_method,#payment_method
                            offering_type,#type
                            date,#date
                            None,#member
                            names[0],#name_if_not_member =
                            None #phone_if_not_memmber
                        )
