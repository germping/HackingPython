import argparse
parser= argparse.ArgumentParser(description='Paso de parametros')
parser.add_argument("-p1", dest="param1", help="parameter1")
parser.add_argument("-p2", dest="param2", help="parameter2")
params= parser.parse_args()
#print (params._get_args)
print (params.param2)
