import random

from decouple import config
from fabric.api import cd, run, local, sudo
from fabric.contrib.files import exists, append

REPO_URL = 'git@github.com:orichcasperkevin/church-is.git'


def deploy():
    site_folder = f'/home/nanoafrika/church-is'
    run(f'mkdir  -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv_live()
        _update_database()
        _create_main_server_folders()
        _create_main_webserver_files()
        _restart_live_server()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git init')
        run(f'git remote add origin {REPO_URL}')
        run('git fetch')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv():
    if not exists('venv/bin/pip'):
        run(f'python3.6 -m venv venv')
    run('./venv/bin/pip install --upgrade pip')
    run('./venv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv_live():
    append('.env', f'DEBUG =false')
    append('.env',
           f'ALLOWED_HOSTS=church.nanocomputing.co.ke')
    append('.env', f'DATABASE_URL={config("LIVE_DATABASE_URL")}')
    append('.env', f'AFRICAS_TALKING_API_KEY = {config("AFRICAS_TALKING_API_KEY")}')
    append('.env', f'AFRICAS_TALKING_USERNAME = {config("AFRICAS_TALKING_USERNAME")}')
    current_contents = run('cat .env')
    if 'SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50))
        append('.env', f'SECRET_KEY={new_secret}')


def _update_database():
    run('./venv/bin/python manage.py migrate --noinput')


def _create_main_server_folders():
    run(f'mkdir  -p /home/nanoafrika/run/')
    run(f'mkdir  -p /home/nanoafrika/logs')


def _create_main_webserver_files():
    if not exists('/home/nanoafrika/church_is_supervisor'):
        run('cp church_is_supervisor /home/nanoafrika/')
        run('chmod u+x /home/nanoafrika/church_is_supervisor')
        run('touch /home/nanoafrika/logs/church_is.log')
        sudo('cp church_is.conf /etc/supervisor/conf.d/')
        sudo('sudo supervisorctl reread')
        sudo('sudo supervisorctl update')
        sudo('sudo supervisorctl status church_is')
        sudo('cp nginx.template.conf /etc/nginx/sites-available/church_is')
        sudo('ln -s /etc/nginx/sites-available/church_is /etc/nginx/sites-enabled/church_is')
        sudo('service nginx restart')


def _restart_live_server():
    sudo('supervisorctl restart church_is')
