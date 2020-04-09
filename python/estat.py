import math
import tables

def boxplot_creator(values):
	'''
	Inputs:
	values: list of float values representing the values 
	on the distribution.

	Outputs:
	boxplot_points: list of 5 floats representing the 5
	important points on the boxplot: minimum, 1st quartile, 
	2nd quartile, 3rd quartile and 4th quartile
	outliers: list os floats representing the distribution 
	outliers.
	'''
	boxplot_points=[]
	outliers=[]
	n=len(values)
	values.sort()
	if n%2:
		q2=values[n//2]
	else:
		q2=(values[n//2]+values[n//2+1])/2
	if n%4:
		q1=values[n//4]
		q3=values[3*n//4]
	else:
		q1=(values[n//4]+values[n//4+1])/2
		q3=(values[(3*n)//4]+values[(3*n)//4])/2
	iqr=q3-q1
	while values[0]<q1-1.5*iqr:
		outliers.append(values.pop(0))
	while values[len(values)-1]>q3+1.5*iqr:
		outliers.append(values.pop(len(values)-1))
	n=len(values)
	q0=values[0]
	q4=values[n-1]
	boxplot_points=[q0, q1, q2, q3, q4]
	return boxplot_points, outliers

def histogram_creator(values, k=None, k_mode=1):
	'''
	Inputs:
	values: list of float values representing the values 
	on the distribution.
	k: int or None. Represents the number of bars on the
	histogram, if None it will be generated automaticaly.
	k_mode: 1, 2 or 3. Represents the method to generate 
	the k value.

	Outputs:
	heights: list of k floats. Represents the heights of
	each of the bars on the histogram.
	'''
	heights=[]
	n=len(values)
	values.sort()
	if k==None:
		if k_mode==1:
			k=2*(n**(1/3))
		elif k_mode==2:
			k=n**(1/2)
		elif k_mode==3:
			k=1+math.log(n, 2)
		else:
			print("Incorrect value for k_mode.")
			exit()
	k=int(k)
	h=(values[n-1]-values[0])/k
	heights=[0]*k
	for num in values[:-1]:
		heights[int(num/h)]+=1
	heights[-1]+=1
	return heights

def parameters(values):
	'''
	Inputs:
	values: list of float values representing the values 
	on the distribution.

	Outputs: 
	params: list of 8 floats. Each one representing one
	parameter of the given distribution. Given in the 
	following order: mean, mode, median, variance,
	standart deviation, Pearson assymmetry, assymmetry
	kind, kurtosis.
	'''
	values.sort()
	n=len(values)
	#mean
	mean=sum(values)/len(values)
	#mode
	max_repeat=1
	mode=values[0]
	current=values[0]
	current_max_repeat=1
	for elem in values[1:]:
		if elem==current:
			current_max_repeat+=1
		elif current_max_repeat>max_repeat:
			max_repeat=current_max_repeat
			mode=current
			current=elem
			current_max_repeat=1
		else:
			current=elem
			current_max_repeat=1
	if current_max_repeat>max_repeat:
		max_repeat=current_max_repeat
		mode=current
	#median
	if n%2:
		median=values[n//2]
	else:
		median=(values[n//2]+values[n//2]+1)/2
	#variance
	variance=0
	for elem in values:
		variance+=(elem-mean)**2
	variance/=(len(values)-1)
	#standart deviation
	stddev=variance**(1/2)
	#Pearson Assymmetry
	p_assymmetry=(median-mode)/stddev
	#constants
	m2=variance*(1-1/len(values))
	m3=0
	for elem in values:
		m3+=(elem-mean)**3
	m3/=len(values)
	m4=0
	for elem in values:
		m4+=(elem-mean)**4
	m4/=len(values)
	#assymmetry
	assymemtry=m3/(m2**(2/3))
	#kurtosis
	kurtosis=m4/(m2**2)
	return [mean, mode, median, variance, stddev, p_assymmetry, assymemtry, kurtosis]

def confidence_interval(parameter, n, confidence, mean=None, proportion=None, variance=None, stddev=None):
	'''
	Inputs:
	parameter: string representing which kind of confidence
	interval is to be calculated. It can be "mean_known_var",
	"mean_unkown_var", "proportion" or "variance".
	n: int representing the number os values on the 
	distrubution
	confidence: float between 0 and 1 representing the
	confidence level desired on the interval
	mean: float representing the distrbution mean. Mandatory 
	if parameter is "mean_kown_var" or "mean_unkown_var".
	proportion: float representing the distribution proportion.
	Mandatory when parameter is "proportion".
	stddev: float representing the distribution standart 
	deviation. Mandatory if parameter is "mean_unkown_var" or
	"variance".
	variance: float reŕesenting the distribution real variance.
	Mandatory if parameter is "mean_known_var".

	Outputs:
	two floats representing limits of the confidence interval.
	'''
	if parameter=="mean_known_var":
		z=normal.get_values(confidence/2)
		delta=z*variance/(n**.5)
		return mean-delta, mean+delta
	elif parameter=="mean_unknown_var":
		t=student.get_values((1-confidence)/2, n-1)
		delta=t*stddev/(n**.5)
		return mean-delta, mean+delta
	elif parameter=="proportion":
		z=normal.get_values(confidence/2)
		delta=z*(proportion*(1-proportion)/n)**.5
		return proportion-delta, proportion+delta
	elif parameter=="variance":
		return (stddev**2)*(n-1)/chi_square.get_values((1-confidence)/2, n-1), (stddev**2)*(n-1)/chi_square.get_values(.5+confidence/2, n-1)
	else:
		print("Unidentified parameter")
		exit()

def hypotesis_test(kind, parameter, param_0, alternate_h, n, confidence, mean=None, proportion=None, variance=None, stddev=None):
	if kind=="single":
		if parameter=="mean_known_var":
			z_calc=(mean-param_0)/((variance/n)**.5)
			if alternate_h=="=/=":
				z_tab_sup=normal.get_values(confidence/2)
				z_tab_inf=(-1)*z_tab_sup
				print("z_tab=["+str(z_tab_inf)+","+str(z_tab_sup)+"]")
				print("z_calc="+str(z_calc))
				return (z_calc>z_tab_inf and z_calc<z_tab_sup)
			elif alternate_h=="<":
				z_tab=normal.get_values(confidence-.5)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc<z_tab
			elif alternate_h==">":
				z_tab=normal.get_values(1-confidence)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc>z_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="mean_unknown_var":
			t_calc=(mean-param_0)/(stddev/(n**.5))
			if alternate_h=="=/=":
				t_tab_sup=student.get_values(confidence/2, n-1)
				t_tab_inf=(-1)*t_tab_sup
				print("t_tab=["+str(t_tab_inf)+","+str(t_tab_sup)+"]")
				print("t_calc="+str(t_calc))
				return (z_calc>t_tab_inf and z_calc<t_tab_sup)
			elif alternate_h=="<":
				t_tab=Student.get_values(confidence-.5, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc<t_tab
			elif alternate_h==">":
				t_tab=Student.get_values(1-confidence, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc>t_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="proportion":
			z_calc=(proportion-param_0)/(((param_0*(1-param_0))/n)**.5)
			if alternate_h=="=/=":
				z_tab_sup=normal.get_values(confidence/2)
				z_tab_inf=(-1)*z_tab_sup
				print("z_tab=["+str(z_tab_inf)+","+str(z_tab_sup)+"]")
				print("z_calc="+str(z_calc))
				return (z_calc>z_tab_inf and z_calc<z_tab_sup)
			elif alternate_h=="<":
				z_tab=normal.get_values(confidence-.5)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc<z_tab
			elif alternate_h==">":
				z_tab=normal.get_values(1-confidence)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc>z_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="variance":
			chis_calc=((n-1)*stddev**2)/param_0
			if alternate_h=="=/=":
				chis_tab_sup=chi_square.get_values(confidence/2, n-1)
				chis_tab_inf=chi_square.get_values(.5-confidence/2, n-1)
				print("chis_tab=["+str(chis_tab_inf)+","+str(chis_tab_sup)+"]")
				print("chis_calc="+str(chis_calc))
				return (chis_calc>chis_tab_inf and chis_calc<chis_tab_sup)
			elif alternate_h=="<":
				chis_tab=chi_square.get_values(confidence, n-1)
				print("chis_tab="+str(chis_tab))
				print("chis_calc="+str(chis_calc))
				return chis_calc>chis_tab
			elif alternate_h==">":
				chis_tab=chi_square.get_values(1-confidence, n-1)
				print("chis_tab="+str(chis_tab))
				print("chis_calc="+str(chis_calc))
				return chis_calc<chis_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		else:
			print("Unidentified parameter")
	elif kind=="dual":
		if parameter=="paired_mean":
			t_calc=(mean-param_0)/(stddev/(n**.5))
			if alternate_h=="=/=":
				t_tab_sup=student.get_values(confidence/2, n-1)
				t_tab_inf=(-1)*t_tab_sup
				print("t_tab=["+str(t_tab_inf)+","+str(t_tab_sup)+"]")
				print("t_calc="+str(t_calc))
				return (z_calc>t_tab_inf and z_calc<t_tab_sup)
			elif alternate_h=="<":
				t_tab=Student.get_values(confidence-.5, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc<t_tab
			elif alternate_h==">":
				t_tab=Student.get_values(1-confidence, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc>t_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="independent_mean_known_stddev":
			z_calc=(mean[0]-mean[1]-param_0)/((stddev[0]**2/n[0]+stddev[1]**2/n[1])**.5)
			if alternate_h=="=/=":
				z_tab_sup=normal.get_values(confidence/2)
				z_tab_inf=(-1)*z_tab_sup
				print("z_tab=["+str(z_tab_inf)+","+str(z_tab_sup)+"]")
				print("z_calc="+str(z_calc))
				return (z_calc>z_tab_inf and z_calc<z_tab_sup)
			elif alternate_h=="<":
				z_tab=normal.get_values(confidence-.5)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc<z_tab
			elif alternate_h==">":
				z_tab=normal.get_values(1-confidence)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc>z_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="independent_mean_unknown_equal_stddev":
			t_calc=(mean[0]-mean[1]-param_0)/(((((n[0]-1)*stddev[0]**2+(n[1]-1)*stddev[1]**2)/(n[0]+n[1]-2))**.5)*((1/n[0]+1/n[1])**.5))
			if alternate_h=="=/=":
				t_tab_sup=student.get_values(confidence/2, n-1)
				t_tab_inf=(-1)*t_tab_sup
				print("t_tab=["+str(t_tab_inf)+","+str(t_tab_sup)+"]")
				print("t_calc="+str(t_calc))
				return (z_calc>t_tab_inf and z_calc<t_tab_sup)
			elif alternate_h=="<":
				t_tab=Student.get_values(confidence-.5, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc<t_tab
			elif alternate_h==">":
				t_tab=Student.get_values(1-confidence, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc>t_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="independent_mean_unknown_diff_stddev":
			t_calc=(mean[0]-mean[1]-param_0)/((stddev[0]**2/n[0]+stddev[1]**2/n[1])**.5)
			if alternate_h=="=/=":
				t_tab_sup=student.get_values(confidence/2, n-1)
				t_tab_inf=(-1)*t_tab_sup
				print("t_tab=["+str(t_tab_inf)+","+str(t_tab_sup)+"]")
				print("t_calc="+str(t_calc))
				return (z_calc>t_tab_inf and z_calc<t_tab_sup)
			elif alternate_h=="<":
				t_tab=Student.get_values(confidence-.5, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc<t_tab
			elif alternate_h==">":
				t_tab=Student.get_values(1-confidence, n-1)
				print("t_tab="+str(t_tab))
				print("t_calc="+str(t_calc))
				return t_calc>t_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="proportion":
			z_calc=(proportion[0]-proportion[1]-param_0)/(((proportion[0]*(1-proportion[0]))/n[0]+(proportion[1]*(1-proportion[1]))/n[1])**.5)
			if alternate_h=="=/=":
				z_tab_sup=normal.get_values(confidence/2)
				z_tab_inf=(-1)*z_tab_sup
				print("z_tab=["+str(z_tab_inf)+","+str(z_tab_sup)+"]")
				print("z_calc="+str(z_calc))
				return (z_calc>z_tab_inf and z_calc<z_tab_sup)
			elif alternate_h=="<":
				z_tab=normal.get_values(confidence-.5)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc<z_tab
			elif alternate_h==">":
				z_tab=normal.get_values(1-confidence)
				print("z_tab="+str(z_tab))
				print("z_calc="+str(z_calc))
				return z_calc>z_tab	
			else:
				print("Unknown alternate hypotesis")
				exit()
		elif parameter=="variance":
			pass
		else:
			print("Unidentified parameter")
	else:
		print("Unknown kind")
		exit()

normal=tables.Normal()
student=tables.Student()
chi_square=tables.Chi_Square()