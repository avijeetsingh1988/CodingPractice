import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hello')
args = parser.parse_args()
idk = args.hello
print(idk)
if idk is None:
     print("what man")