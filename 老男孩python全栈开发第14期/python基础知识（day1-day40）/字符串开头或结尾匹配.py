if __name__ == '__main__':
	filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
	print([filename for filename in filenames
	       if filename.startswith("f") or filename.endswith("py")])
	
	print([filename for filename in filenames
	       if filename.startswith("f") or filename.endswith(("py","h"))])#使用元组匹配多种情况
