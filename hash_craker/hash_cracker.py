#!/usr/bin/env python

import argparse
import hashlib
import termcolor


def get_password_match(digest: str, hash_list: list) -> None:
    for item in hash_list:
        if item['digest'] == digest:
            termcolor.cprint(f'[+] Match found, {digest} : password: {item['password']}', 'black', 'on_light_green')


def process_digest(alg: str, filepath: str) -> list:
    try:
        hash_list = []
        with open(filepath, 'r') as file:
            for line in file.readlines():
                match alg:
                    case 'md5':
                        hash_object = hashlib.md5(line.strip().encode())
                    case 'sha1':
                        hash_object = hashlib.sha1(line.strip().encode())
                    case 'sha2':
                        hash_object = hashlib.sha256(line.strip().encode())
                    case _:
                        print('Hash type not found/supported')
                        exit(1)
                hash_digest = hash_object.hexdigest()
                hash_dic = {"digest": hash_digest, "password": line.strip()}
                hash_list.append(hash_dic.copy())
            return hash_list

    except FileNotFoundError:
        print(f'{filepath} incorrect, no file found')


def get_argument():
    parser = argparse.ArgumentParser(prog='Hash Cracker')
    parser.add_argument('-a', '--alg', dest='algorithm', help='hash algorithm to use [Supported -> md2, sha1, sha2]',
                        type=str, required=True)
    parser.add_argument('--digest', '-d', dest='digest', help='hash to decrypt', type=str, required=True)
    parser.add_argument('--filepath', '-f', dest='filepath', help='Filepath to passwords list', required=True)
    return parser.parse_args()


def main():
    arguments = get_argument()
    digest = arguments.digest
    hash_type = arguments.algorithm
    filepath = arguments.filepath
    hash_dictionary = process_digest(hash_type, filepath)
    get_password_match(digest, hash_dictionary)


if __name__ == '__main__':
    main()
