from os import environ, walk, path, listdir, chdir, getcwd, mkdir
from zipfile import ZipFile
from shutil import rmtree, copy, copytree
from hashlib import sha1

back = getcwd()
temp = path.join(back, 'temp')
def generate_zip(filename, items, output_folder):
    back = getcwd()
    if not path.exists(temp):
        mkdir(temp)
    for item in items:
        if path.isfile(item):
            copy(file, temp)
        elif path.isdir(item):
            item = path.join(back, item)
            for newfile in listdir(item):
                newfile = path.join(item, newfile)
                if path.isfile(newfile):
                    copy(newfile, temp)
                else:
                    copytree(path.dirname(newfile), temp, dirs_exist_ok=True)
        else:
            print("Could not find path {} in the main directory".format(item))
    if not path.exists(output_folder):
        mkdir(output_folder)
    with ZipFile(output_folder + filename+".zip", 'w') as file:
        for item in listdir('temp'):
            chdir(temp)
            if path.isfile(item):
                file.write(item)
            else:
                for filepath, sub, filenames in walk(item):
                    for filename in filenames:
                        file.write(path.join(filepath, filename))
    chdir(back)
    if path.exists(temp):
        rmtree(temp)

BLOCKSIZE = 65536

def generate_sha1(filename, output_folder):
    hasher = sha1()
    with open(output_folder + filename+".zip", 'rb') as in_file:
        buf = in_file.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = in_file.read(BLOCKSIZE)
    with open(output_folder + filename+".sha1", 'w+') as out_file:
        out_file.write(hasher.hexdigest())

if __name__ == '__main__':
    filename = environ['FILENAME']
    items = environ['ITEMS'].split('\n')
    if 'GEN-SHA1' in environ:
        gen_sha1 = environ['GEN-SHA1']
    else:
        gen_sha1 = '0'
    if 'OUTPUT-FOLDER' in environ:
        output_folder = environ['OUTPUT-FOLDER']
    else:
        output_folder = 'build'
    if !output_folder.endswith('/'):
        output_folder += '/'
    generate_zip(filename, items, output_folder)
    if gen_sha1.lower() in ("yes", "y", "true", "t", "1"):
        generate_sha1(filename, output_folder)