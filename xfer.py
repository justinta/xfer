"""
Transfer files
ftp
sftp
others...?
"""

# Python libs
import sys
import shutil

import logging
import logging.config

import argparse

from ftplib

try:
    import paramiko
    HAS_PARAMIKO = True
except ImportError:
    HAS_PARAMIKO = False


# xfer libs


# logging
#logging.config.fileConfig('xfer_log.conf')
#logger = logging.getLogger('xfer_log')


def move_file(src, dest, clean_src=False):
    """
    Move a file from one place to another
    """
    clean_src = True
    if clean_src:
        shutil.move(src, dest)
    else:
        shutil.copyfile(src, dest)
    
    print('File moved from {0} to {1}'.format(src, dest))

    #logger.info(f'File moved from {src} to {dest}')


def from_ftp(host, files, src_path, dest_path):
    """
    Transfer a file using ftp
    """
    user = input('Username: ')
    passwd = getpass.getpass()

    ftp = ftplib.FTP(host, user, passwd)
    ftp.cwd(src_path)

    if not isinstance(files, list):
        files = files.split()

    try:
        for f in files:
            with open(f, 'wb') as new_file:
                ftp.retrbinary('RETR {0}'.format(f), new_file.write)
    except:
        pass


def to_ftp(host, files, src_path, dest_path):
    """
    Transfer a file to remote ftp
    """
    user = input('Username: ')
    passwd = getpass.getpass()

    ftp = ftplib.FTP(host, user, passwd)
    ftp.cwd(src_path)

    for f in files:
        with open(f, 'rb') as new_file:
            ftp.storbinary('STOR {0}'.format(f), f)
            
            
    
    

def sftp(host, files, src_path, dest_path):
    """
    transfer a file using sftp

    Requires paramiko
    """
    if not HAS_PARAMIKO:
        sys.exit('You need Paramiko to use sftp')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('xfer_type', choices=['move', 'ftp', 'sftp', 'ftps'], help='type of transfer')
    parser.add_argument('--source', required=True, help='source file')
    parser.add_argument('--destination', required=True, help='desination file')
    parser.add_argument('--clean-src', action='store_true', default=False, help='Clean the source directory')
    args = parser.parse_args()

    if args.xfer_type == 'move':
        move_file(args.source, args.destination, clean_src=args.clean_src)


if __name__ == '__main__':
    main()
