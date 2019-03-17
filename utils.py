import logging
import os
import argparse
import sys

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--accessKey', help='define oss access id')
parser.add_argument('-s', '--accessSecret', help='define oss access secret')
parser.add_argument('-n', '--bucketName', help='define oss bucket name')
parser.add_argument('-e', '--endpoint', help='define oss bucket endpoint url')
parser.add_argument('-d', '--backupDir', help='define destination directory to store files')


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info('Created new directory: ' + path)
    else:
        logger.info('Directory {0} existed'.format(path))


def parse_argv(config):
    args = parser.parse_args()
    if args.accessKey:
        config['AccessKey'] = args.accessKey
    if args.accessSecret:
        config['AccessSecret'] = args.acessSecret
    if args.bucketName:
        config['BucketName'] = args.bucketName
    if args.endpoint:
        config['Endpoint'] = args.endpoint
    if args.backupDir:
        config['BackupDir'] = args.backupDir


def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        if rate == 100:
            print('\r{0}%'.format(rate))
        else:
            print('\r{0}%'.format(rate), end='')
        sys.stdout.flush()