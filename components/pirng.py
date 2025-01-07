from components.prng import *;
from components.pi import *;

def rrng() :
	x_str = prng();
	y_str = prng();
	rdm_str = prng();
	p = pi();
	x = int(x_str);
	y = int(y_str);
	rdm = int(rdm_str);
	r1 = str(p)[x:x+4];
	r2 = str(p)[y:y+4];
	r_nbr1 = int(r1);
	r_nbr2 = int(r2);
	r_nbr1 *= 2;
	r_nbr2 *= 2;
	r_nbr = str(r_nbr1 * r_nbr2 * rdm).zfill(12)[:12];  
	print(r_nbr);