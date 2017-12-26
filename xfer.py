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

try:
    import paramiko
    HAS_PARAMIKO = True
except ImportError:
    HAS_PARAMIKO = False

if not HAS_PARAMIKO:
    sys.exit('You need Paramiko')

# xfer libs


# logging
logging.config.fileConfig('xfer_log.conf')
logger = logging.getLogger('xfer_log')


def move_file(src, dest, clean_src=False):
    """
    Move a file from one place to another
    """
    clean_src = True
    if clean_src:
        shutil.move(src, dest)
    else:
        shutil.copyfile(src, dest)

    logger.info(f'File moved from {src} to {dest}')


def sftp(host, files, src_path, dest_path):
    """
    transfer a file using sftp
    """
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('xfer_type', help='type of transfer')
    parser.add_argument('--source', help='source file')
    parser.add_argument('--destination', help='desination file')
    args = parser.parse_args()

    if args.xfer_type == 'move':
        move_file(args.source, args.destination)


if __name__ == '__main__':
    main()
