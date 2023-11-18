import os

python_packages = []
data_list = []


def create_python_package(path, name):
    os.mkdir(os.path.join(path, name))
    python_packages.append(name)
    file = open(os.path.join(path, name, '__init__.py'), 'w')
    file.close()


def create_security_package(path, name='security'):
    os.mkdir(os.path.join(path, name))
    file = open(os.path.join(path, name, 'ir.model.access.csv'), 'w')
    file.write('id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink')
    file.close()


def create_views(path):
    os.mkdir(os.path.join(path, 'views'))


def create_static_package(path):
    os.mkdir(os.path.join(path, 'static'))
    os.mkdir(os.path.join(path, 'static/src'))
    os.mkdir(os.path.join(path, 'static/src/js'))
    os.mkdir(os.path.join(path, 'static/src/xml'))
    os.mkdir(os.path.join(path, 'static/src/scss'))


BASEDIR = os.path.dirname(os.path.realpath(__file__))
rel_path = input('Relative Path? ex: /custom/module_name\n')

os.mkdir(os.path.join(BASEDIR, rel_path))
model_name = os.path.basename(os.path.join(BASEDIR, rel_path))


if input('controllers y/n? ').lower() == 'y':
    create_python_package(os.path.join(BASEDIR, rel_path), 'controllers')
if input('models y/n? ').lower() == 'y':
    create_python_package(os.path.join(BASEDIR, rel_path), 'models')
if input('report y/n? ').lower() == 'y':
    create_python_package(os.path.join(BASEDIR, rel_path), 'report')
if input('wizard y/n? ').lower() == 'y':
    create_python_package(os.path.join(BASEDIR, rel_path), 'wizard')

if input('security y/n? ').lower() == 'y':
    create_security_package(os.path.join(BASEDIR, rel_path))
    data_list.append(f" '{os.path.join('security', 'ir.model.access.csv')}' ")

if input('static y/n? ').lower() == 'y':
    create_static_package(os.path.join(BASEDIR, rel_path))

if input('views y/n? ').lower() == 'y':
    create_views(os.path.join(BASEDIR, rel_path))

data_list = ',\n'.join(data_list)

base_file = open(os.path.join(BASEDIR, rel_path, '__init__.py'), 'w')
base_file.write('\n'.join(f'from . import {package_name}' for package_name in python_packages))
base_file.close()


def get_manifest_content():
    return f"""{{
    'name': '{model_name}',
    'version': '0.1',
    'summary': 'Summary',
    'sequence': 10,
    'description': " Description ",
    'category': '',
    'website': '',
    'depends': ['base'],
    'data': [
        {data_list}
    ],
}}"""


base_file = open(os.path.join(BASEDIR, rel_path, '__manifest__.py'), 'w')
base_file.write(get_manifest_content())
base_file.close()



