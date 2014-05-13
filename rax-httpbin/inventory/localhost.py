#!/usr/bin/env python

import sys
import json
import argparse


def localhost():
    hosts = {
        'localhost': {
            'hosts': ['127.0.0.1']
        },
        '_meta': {
            'hostvars': {
                '127.0.0.1': {
                    'ansible_connection': 'local',
                    'ansible_python_interpreter': sys.executable
                }
            }
        }
    }
    return json.dumps(hosts, indent=4, sort_keys=True)


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--host', help='List details about a specific host')
    group.add_argument('--list', action='store_true', default=False,
                       help='List active servers')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.host:
        sys.stderr.write('--host is not implemented')

    sys.stdout.write(localhost())
    sys.exit(0)


if __name__ == '__main__':
    main()
