import os
import django
import datetime

from django.db.models.fields.files import ImageFieldFile, FileField

from dashboard.models import Members
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Writes the data to the Users and Members database.'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        print("Populating database...")
        start_time = datetime.datetime.now().replace(microsecond=0)

        file = open("/home/cole/Desktop/members.csv", "r")
        file.readline()
        file.readline()

        current_line = file.readline()
        count = 1
        while current_line != '':
            processed = current_line.split(",")

            name = self.fix_name_format(processed[0])

            if name == "Cole Polyak":
                account = User.objects.get(username="cole")
                brother = Members.objects.get_or_create(
                                user=account,
                                name=name,
                                legal_name=legal_name,
                                phone=processed[2].strip(),
                                address=processed[3].strip().replace("\"", ""),
                                email=processed[4].strip(),
                                rollnumber=int(processed[5].strip()),
                                member_score=0,
                                inactive_flag=not bool(processed[6].strip()),
                                abroad_flag=not bool(processed[7].strip()),
                                present=0,
                                position=self.get_position(processed[8]),
                                avatar=ImageFieldFile(instance=None, field=FileField(), name='static/images/default.jpg')
                            )[0]
                count += 1
                current_line = file.readline()
                continue

            legal_name = self.fix_name_format(processed[1])

            account = User.objects.create_user(
                username=name.lower().replace(" ", "."),
                email=processed[4].strip(),
                password='password'
            )

            brother = Members.objects.get_or_create(
                user=account,
                name=name,
                legal_name=legal_name,
                phone=processed[2].strip(),
                address=processed[3].strip().replace("\"", ""),
                email=processed[4].strip(),
                rollnumber=int(processed[5].strip()),
                member_score=0,
                inactive_flag=not bool(processed[6].strip()),
                abroad_flag=not bool(processed[7].strip()),
                present=0,
                position=self.get_position(processed[8]),
                avatar=ImageFieldFile(instance=None, field=FileField(), name='static/images/default.jpg')

            )[0]

            count += 1
            current_line = file.readline()

        end_time = datetime.datetime.now().replace(microsecond=0)
        print("Populating complete...")
        print("Wrote " + str(count) + " entries in " + str(end_time - start_time))


    def fix_name_format(self, name):
        name = name.split(" ")

        if len(name) > 2:
            name.pop(1)

        new_name = ""
        for x in range(len(name)):
            new_name += str(name[x]) + " "
        return new_name.strip()


    def get_position(self, pos):
        if len(pos.strip()) == 0:
            return "Member"
        return pos.strip()
