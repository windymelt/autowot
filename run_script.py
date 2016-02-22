import os, subprocess, ConfigParser

def run_script(inifilename):
    ini = ConfigParser.SafeConfigParser()
    if os.path.exists(inifilename):
        ini.read(inifilename)
    else:
        raise Exception('No autowot.ini found.')

    version = ini.get('autowot', 'autowot_version')

    if version != "0":
        raise Exception('Version error')

    posix_script_filename = ini.get('autowot', 'script_posix')
    nt_script_filename = ini.get('autowot', 'script_nt')

    if os.name == 'posix':
        print 'Detected OS: [POSIX (OSX)]'
        print 'Executing ' + posix_script_filename + '...'
        subprocess.Popen(['sh', posix_script_filename])
    elif os.name == 'nt':
        print 'Detected OS: [Windows]'
        print 'Executing ' + nt_script_filename + '...'
        subprocess.Popen(['start', nt_script_filename])
    else:
        raise Exception('Unsupported OS.')
