# def deltaFunction(x_1,x_2,t_1,t_2):
# 	delta = 0;
# 	for i in range(len(t_1)):
# 		for j in  range(len(t_2)):
# 			if i/2 == j:
# 				delta = max(delta, x_1[i]-x_2[j])
# 			else:
# 				if t_1[i]<t_2[j]: 
# 					break
# 	return abs(delta)

# while (delta>EPS):
# 	[tn,x,y] = MethodVilsona(h,a,b,c,d,x0,y0,t[0],t[1]);
# 	x_1 = x;
# 	y_1 = y; 
# 	t_1 = tn;
# 	[tn,x,y] = MethodVilsona(h/2,a,b,c,d,x0,y0,t[0],t[1]);
# 	x_2 = x; 
# 	y_2 = y; 
# 	t_2 = t;

# 	R1 = deltaFunction(x_1,x_2,t_1,t_2)/15;
# 	R2 = deltaFunction(y_1,y_2,t_1,t_2)/15;

# 	delta = max(R1,R2);
# 	h /= 2;


	# ti = np.linspace(t[0], t[1], intervals)
	# yi = np.array([y0])
	# xi = np.array([x0])


	# for i in range(len(ti)-1):
	# 	k, q = get_kq(dy, dx, ti[i], yi[i], xi[i], search_start_step(EPS)/126)
	# 	yi = np.append(yi, func_i(yi[i], k))
	# 	xi = np.append(xi, func_i(xi[i], q))