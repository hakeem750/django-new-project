import os
from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key

class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('current', type=str, nargs='+', help='The current Django project folder name')
        parser.add_argument('new', type=str, nargs='+', help='The new Django project name')

    def handle(self, *args, **kwargs):
        current_project_name = kwargs['current'][0]
        new_project_name = kwargs['new'][0]

        # logic for renaming the files

        files_to_rename = ['.env', f'{current_project_name}/settings/base.py',
                           f'{current_project_name}/wsgi.py', 'manage.py']

        for key, f in enumerate(files_to_rename):
            if key == 0:
                filedata = "SECRET_KEY="+ get_random_secret_key()+ "\n"+"DEBUG=False"
                with open(f, 'w') as file:
                    file.write(filedata)      
            else:
                
                with open(f, 'r') as file:
                    filedata = file.read()

                filedata = filedata.replace(current_project_name, new_project_name)

                with open(f, 'w') as file:
                    file.write(filedata)
        os.rename(current_project_name, new_project_name)

        self.stdout.write(self.style.SUCCESS(f'Project has been renamed to {new_project_name}'))