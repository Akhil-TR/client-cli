import sys
import os
def main():
	try:
		args = sys.argv[1:]
		for arg in args:
			p=format(arg)
    		print(p)
	except Exception as e:
		raise e
	else:
		pass
	finally:
		pass
    
if __name__ == '__main__':
    main()

