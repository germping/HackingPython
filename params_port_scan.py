import argparse
parser = argparse.ArgumentParser(description='Params port scan')

parser.add_argument("-t", dest="target", help="Target", required=True)
parser.add_argument("-p", "--port", type=int, default=80, help="Port to scan (default: 80)")
parser.add_argument("-v", "--verbose", dest="verbosity", help="Verbosity level",default=0)
parser.add_argument("--open", dest="only_open", action="store_true", help="only display open ports", default=False)
params = parser.parse_args()
print(f"Target: {params.target}")
print(f"Port: {params.port}")
print(f"Verbosity: {params.verbosity}")
print(f"Only open ports: {params.only_open}")