from sys import argv

# NOTE: You may use this function only for integer numbers
# k is num, n is the 'n' in nth root
def iroot(k, n):
	u, s = n, n+1
	while u < s:
		s = u
		t = (k-1) * s + n // pow(s, k-1)
		u = t // k
	return s

def lroot(x, n):
	 X = exp(log(n)/x)

def nroot(n, x):
	return x**(1./float(n))

if __name__ == "__main__":
	if len(argv) > 1:
		print(nroot(int(argv[1]), int(argv[2])))
		exit()
	else:
		print("No input\n" + "-"*24)
		exit()