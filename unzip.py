import zipfile

def unzip(filename):
    zf = zipfile.ZipFile(filename, 'r')
    zf.extractall('.')
