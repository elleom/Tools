from port_scanner.port_scanner import PortScan
import argparse


def get_arguments() -> argparse.Namespace:
    """
    :return: arguments dict
    """
    parser = argparse.ArgumentParser(prog="Vulnerability Scanner")
    parser.add_argument("-port", dest="port", action="store", required=True, type=int)
    parser.add_argument("-target", dest="target", action="store", required=True, type=str)

    return parser.parse_args()


def init(target, port):
    target_ip = target
    port_number = port
    ps = PortScan
    ps.scan_port(target_ip, int(port_number))


if __name__ == '__main__':
    args = get_arguments()
    init(args.target, args.port)

