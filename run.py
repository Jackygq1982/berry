import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RL Service')
    parser.add_argument('--model', '-m', required=True)
    parser.add_argument('--function', '-f', required=True)
    args = parser.parse_args()
    module = __import__("%s.%s" % (args.model,args.model))
    file_module = getattr(module, "%s" % (args.model))
    func = getattr(file_module, "%s" % (args.function))
    func()
