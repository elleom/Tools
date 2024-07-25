import paramiko, sys, os, socket, termcolor, argparse

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
                termcolor.cprint(line.strip("\n"), "yellow")



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

    return parser.parse_args()


if __name__ == "__main__":
    try:
        cli_args = get_arguments()
        main(cli_args)
    except:
        termcolor.cprint("[!] One or more arguments have not being introduced", "red", "on_black")




