import tkinter as tk
from tkinter import scrolledtext
from tkinter import StringVar
from tkinter import messagebox
import numpy as np
import cv2
from PIL import Image
import estat
import math
import matplotlib.pyplot as plt

def notimplemented():
	messagebox.showinfo("ALERT", "'-You shall not pass!'\n                   -Gandalf\n\nYou don't have permission to access this functions")

'''Boxplot and draw it'''
def do_box_plot(data):
	data=data.split(",")
	data[-1]=data[-1][:-1]
	for i in range(len(data)):
		data[i]=float(data[i])
	points, outliers=estat.boxplot_creator(data)
	if len(outliers)==0:
		start=points[0]
		end=points[-1]
	else:
		start=min(outliers[0], points[0])
		end=max(outliers[-1], points[-1])
	wid=1000
	heig=300
	fat=(wid-40)/(end-start)
	img=np.zeros((int(heig), int(wid), 3), np.uint8)
	img=cv2.line(img, (int(20+fat*(points[0]-start)), int(heig/2)), (int(20+fat*(points[1]-start)), int(heig/2)), (255,255,255))
	img=cv2.rectangle(img, (int(20+fat*(points[1]-start)), int(heig/4)), (int(20+fat*(points[2]-start)), int(3*heig/4)), (255,255,255))
	img=cv2.rectangle(img, (int(20+fat*(points[2]-start)), int(heig/4)), (int(20+fat*(points[3]-start)), int(3*heig/4)), (255,255,255))
	img=cv2.line(img, (int(20+fat*(points[3]-start)), int(heig/2)), (int(20+fat*(points[4]-start)), int(heig/2)), (255,255,255))
	for outlier in outliers:
		img=cv2.circle(img, (int(20+fat*(outlier-start)), int(heig/2)), int(wid/500), (255,255,255))
		img=cv2.putText(img, str(outlier), (int(20+fat*(outlier-start)), int(5*heig/6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
	img=cv2.putText(img, str(points[0]), (int(20+fat*(points[0]-start)), int(5*heig/6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
	img=cv2.putText(img, str(points[1]), (int(20+fat*(points[1]-start)), int(5*heig/6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
	img=cv2.putText(img, str(points[2]), (int(20+fat*(points[2]-start)), int(5*heig/6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
	img=cv2.putText(img, str(points[3]), (int(20+fat*(points[3]-start)), int(5*heig/6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
	img=cv2.putText(img, str(points[4]), (int(20+fat*(points[4]-start)), int(5*heig/6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
	box=Image.fromarray(img, 'RGB')
	box.show()

'''Histogram and draw it'''
def do_histogram(k, k_format, data):
	data=data.split(",")
	data[-1]=data[-1][:-1]
	for i in range(len(data)):
		data[i]=float(data[i])
	if k_format=="automatic" or k_format=="2*cbrt(n)":
		k=None
		mode=1
	elif k_format=="sqrt(n)":
		k=None
		mode=2
	elif k_format=="log2(n)+1":
		k=None
		mode=3
	else:
		mode=None
	heights=estat.histogram_creator(data, k, mode)
	heights.append(0)
	x=[str(min(data))]
	delta=(max(data)-min(data))/(len(heights)-1)
	for i in heights[1:]:
		x.append(str(float(x[-1])+delta))
	plt.bar(x,heights, align="edge", alpha=1, width=1)
	plt.show()

'''HIstogram and parameters and show it'''
def do_histogram_param(k, k_format, data):
	data=data.split(",")
	data[-1]=data[-1][:-1]
	for i in range(len(data)):
		data[i]=float(data[i])
	if k_format=="automatic" or k_format=="2*cbrt(n)":
		k=None
		mode=1
	elif k_format=="sqrt(n)":
		k=None
		mode=2
	elif k_format=="log2(n)+1":
		k=None
		mode=3
	else:
		mode=None
	heights=estat.histogram_creator(data, k, mode)
	n=len(heights)
	heights.append(0)
	x=[str(min(data))]
	delta=(max(data)-min(data))/(len(heights)-1)
	for i in heights[1:]:
		x.append(str(float(x[-1])+delta))
	heights.pop(-1)
	mean=0
	acum=[]
	for i in range(n):
		mean+=(float(x[i])+float(x[i+1]))*heights[i]/2
		acum.append(sum(heights[:i+1]))
	mean/=sum(heights)
	mdi=n/2
	if not n%2:
		mdi+=.5
	md=0
	while acum[md]<mdi:
		md+=1
	median=float(x[i])+(mdi-acum[i-1])*delta/heights[i]
	mo=heights.index(max(heights))
	mode=float(x[mo])+heights[mo+1]*delta/(heights[mo-1]+heights[mo+1])
	text="Summary statistics:\nMean: "+str(int(1000*mean)/1000)+"\nMode: "+str(int(1000*mode)/1000)+"\nMedian: "+str(int(1000*median)/1000)
	messagebox.showinfo("RESULTS", text)

'''Parameters and write it'''
def do_parameters(data):
	data=data.split(",")
	data[-1]=data[-1][:-1]
	for i in range(len(data)):
		data[i]=float(data[i])
	params=estat.parameters(data)
	text="Summary statistics:\nMean: "+str(int(1000*params[0])/1000)+"\nMode: "+str(int(1000*params[1])/1000)+"\nMedian: "+str(int(1000*params[2])/1000)+"\nVariance: "+str(int(1000*params[3])/1000)+"\nStandart Deviation: "+str(int(1000*params[4])/1000)+"\nPearson: "+str(int(1000*params[5])/1000)
	if abs(params[5])< -.15:
		text+=" -> symmetric"
	elif abs(params[5])>1:
		text+=" -> asymmetry"
	else:
		text+=" -> almost symmetric"
	text+="\nAssymmetry: "+str(int(1000*params[4])/1000)
	if params[6]< -.5:
		text+=" -> negative assymmetry"
	elif params[6]>.5:
		text+=" -> positive assymmetry"
	else:
		text+=" -> symmetric"
	text+="\nKurtosis: "+str(int(1000*params[4])/1000)
	if params[7]< 2.5:
		text+=" -> platykurtic"
	elif params[7]>3.5:
		text+=" -> leptokurtic"
	else:
		text+=" -> mesokurtic"
	messagebox.showinfo("RESULTS", text)

'''Confidence Interval and show'''
def do_mean_confidence_interval(n, confidence, mean, varstddev, kind):
	if kind=="known":
		interval=estat.confidence_interval("mean_known_var", n, confidence, variance=varstddev, mean=mean)
	elif kind=="unkown":
		interval=estat.confidence_interval("mean_unknown_var", n, confidence, stddev=varstddev, mean=mean)
	else:
		print("Unknow type")
		exit()
	text="Confidence interval is:\n["+str(int(10000*interval[0])/10000)+", "+str(int(10000*interval[1])/10000)+ "]"
	messagebox.showinfo("RESULTS", text)

'''Probability Interval and show'''
def do_prop_confidence_interval(n, confidence, proportion):
	interval=estat.confidence_interval("proportion", n, confidence, proportion=proportion)
	text="Confidence interval is:\n["+str(int(10000*interval[0])/10000)+", "+str(int(10000*interval[1])/10000)+ "]"
	messagebox.showinfo("RESULTS", text)

'''Variance Interval and show'''
def do_var_confidence_interval(n, confidence, stddev):
	interval=estat.confidence_interval("variance", n, confidence, stddev=stddev)
	text="Confidence interval is:\n["+str(int(10000*interval[0])/10000)+", "+str(int(10000*interval[1])/10000)+ "]"
	messagebox.showinfo("RESULTS", text)

'''Box Plot Screen'''
def bps():
	bp_screen=tk.Toplevel(choose_screen)
	bp_screen.title("StatCalc-Box Plot")
	bp_screen.geometry("500x300")
	label_values=tk.Label(bp_screen, text="Insert you data below. Use ',' as separator.", font=("Times", 15), height=3)
	data=scrolledtext.ScrolledText(bp_screen, width=40, height=10)
	button_actbp=tk.Button(bp_screen, text="Draw", width=20, command=lambda:do_box_plot(data.get("1.0", tk.END)))
	butc=tk.Button(bp_screen, text="Back", width=20, command=bp_screen.destroy)

	label_values.pack()
	label_values.place(anchor="nw", relx=.1)
	data.pack()
	data.place(anchor="n", relx=.5, rely=.2)
	button_actbp.pack()
	button_actbp.place(anchor="se", relx=.95, rely=.95)
	butc.pack()
	butc.place(anchor="sw",relx=.05, rely=.95)

'''Histogram Screen'''
def hgs():
	hg_screen=tk.Toplevel(choose_screen)
	hg_screen.title("StatCalc-Histogram")
	hg_screen.geometry("500x400")
	label_k=tk.Label(hg_screen, text="k format:", font=("Times", 15), height=3)
	k=StringVar(hg_screen)
	k.set("automatic")
	option_k=tk.OptionMenu(hg_screen, k, "automatic", "2*cbrt(n)", "sqrt(n)", "log2(n)+1", "personalized:")
	perso_k=tk.Entry(hg_screen, width=15)
	label_values=tk.Label(hg_screen, text="Insert you data below. Use ',' as separator.", font=("Times", 15), height=3)
	data=scrolledtext.ScrolledText(hg_screen, width=40, height=10)
	button_actbp=tk.Button(hg_screen, text="Draw", width=20, command=lambda:do_histogram(int(perso_k.get()), k.get(), data.get("1.0", tk.END)))
	button_param=tk.Button(hg_screen, text="Parameters", width=20, command=lambda:do_histogram_param(int(perso_k.get()), k.get(), data.get("1.0", tk.END)))
	butc=tk.Button(hg_screen, text="Back", width=20, command=hg_screen.destroy)

	label_k.pack()
	label_k.place(anchor="nw", relx=.1)
	option_k.pack()
	option_k.place(anchor="nw", relx=.3, rely=.05)
	perso_k.insert(0, "0")
	perso_k.pack()
	perso_k.place(anchor="nw", relx=.6, rely=.06)
	label_values.pack()
	label_values.place(anchor="nw", relx=.1, rely=.15)
	data.pack()
	data.place(anchor="n", relx=.5, rely=.3)
	button_actbp.pack()
	button_actbp.place(anchor="se", relx=.95, rely=.95)
	button_param.pack()
	button_param.place(anchor="se", relx=.95, rely=.85)
	butc.pack()
	butc.place(anchor="sw",relx=.05, rely=.95)

'''Distribution Parameters Screen'''
def dps():
	dp_screen=tk.Toplevel(choose_screen)
	dp_screen.title("StatCalc-Distrubution Parameters")
	dp_screen.geometry("500x300")
	label_values=tk.Label(dp_screen, text="Insert you data below. Use ',' as separator.", font=("Times", 15), height=3)
	data=scrolledtext.ScrolledText(dp_screen, width=40, height=10)
	button_actbp=tk.Button(dp_screen, text="Calculate", width=20, command=lambda:do_parameters(data.get("1.0", tk.END)))
	butc=tk.Button(dp_screen, text="Back", width=20, command=dp_screen.destroy)

	label_values.pack()
	label_values.place(anchor="nw", relx=.1)
	data.pack()
	data.place(anchor="n", relx=.5, rely=.2)
	button_actbp.pack()
	button_actbp.place(anchor="se", relx=.95, rely=.95)
	butc.pack()
	butc.place(anchor="sw",relx=.05, rely=.95)

'''Confidence Interval Screen'''
def cis():
	ci_screen=tk.Toplevel(choose_screen)
	ci_screen.title("StatCalc-Confidence Interval")
	ci_screen.geometry("500x100")
	label_type=tk.Label(ci_screen, text="Choose which parameter you want", font=("Times", 15), height=2)
	button_me=tk.Button(ci_screen, text="Mean", width=15, command=lambda:mcis())
	button_pr=tk.Button(ci_screen, text="Proportion", width=15, command=lambda:pcis())
	button_vr=tk.Button(ci_screen, text="Variance", width=15, command=lambda:vcis())

	label_type.pack()
	label_type.place(anchor="nw", relx=.1)
	button_me.pack()
	button_me.place(anchor="sw",relx=.03, rely=.85)
	button_pr.pack()
	button_pr.place(anchor="sw",relx=.35, rely=.85)
	button_vr.pack()
	button_vr.place(anchor="sw",relx=.67, rely=.85)

'''Mean Confidence Interval Screen'''
def go_var(label_var):
	label_var.config(text="Variance: ")

def go_std(label_var):
	label_var.config(text="Std Deviation: ")

def mcis():
	mci_screen=tk.Toplevel(choose_screen)
	mci_screen.title("StatCalc-Mean Confidence Interval")
	mci_screen.geometry("500x300")
	known=StringVar(mci_screen)
	rb_known=tk.Radiobutton(mci_screen, text="Known variance", value="known", variable=known, font=("Times", 15), command=lambda:go_var(label_var))
	rb_unkonw=tk.Radiobutton(mci_screen, text="Unknow variance", value="unkown", variable=known, font=("Times", 15), command=lambda:go_std(label_var))
	label_n=tk.Label(mci_screen, text="n: ", font=("Times", 15))
	entry_n=tk.Entry(mci_screen, width=15)
	label_conf=tk.Label(mci_screen, text="Confidence: 		       %", font=("Times", 15))
	entry_conf=tk.Entry(mci_screen, width=15)
	label_mean=tk.Label(mci_screen, text="Mean: ", font=("Times", 15))
	entry_mean=tk.Entry(mci_screen, width=15)
	label_var=tk.Label(mci_screen, text="Variance: ", font=("Times", 15))
	entry_var=tk.Entry(mci_screen, width=15)
	button_actbp=tk.Button(mci_screen, text="Calculate", width=20, command=lambda:do_mean_confidence_interval(int(entry_n.get()), float(entry_conf.get())/100, float(entry_mean.get()), float(entry_var.get()), known.get()))

	rb_known.pack()
	rb_known.place(anchor="nw", relx=.1)
	rb_unkonw.pack()
	rb_unkonw.place(anchor="nw", relx=.5)
	label_n.pack()
	label_n.place(anchor="nw", relx=.1, rely=.15)
	entry_n.pack()
	entry_n.place(anchor="nw", relx=.4, rely=.15)
	label_conf.pack()
	label_conf.place(anchor="nw", relx=.1, rely=.3)
	entry_conf.pack()
	entry_conf.place(anchor="nw", relx=.4, rely=.3)
	label_mean.pack()
	label_mean.place(anchor="nw", relx=.1, rely=.45)
	entry_mean.pack()
	entry_mean.place(anchor="nw", relx=.4, rely=.45)
	label_var.pack()
	label_var.place(anchor="nw", relx=.1, rely=.6)
	entry_var.pack()
	entry_var.place(anchor="nw", relx=.4, rely=.6)
	button_actbp.pack()
	button_actbp.place(anchor="se", relx=.95, rely=.95)

'''Proportion Confidence Interval'''
def pcis():
	pci_screen=tk.Toplevel(choose_screen)
	pci_screen.title("StatCalc-Probability Confidence Interval")
	pci_screen.geometry("500x200")
	label_n=tk.Label(pci_screen, text="n: ", font=("Times", 15))
	entry_n=tk.Entry(pci_screen, width=15)
	label_conf=tk.Label(pci_screen, text="Confidence: 		       %", font=("Times", 15))
	entry_conf=tk.Entry(pci_screen, width=15)
	label_prop=tk.Label(pci_screen, text="Proportion: ", font=("Times", 15))
	entry_prop=tk.Entry(pci_screen, width=15)
	button_actbp=tk.Button(pci_screen, text="Calculate", width=20, command=lambda:do_prop_confidence_interval(int(entry_n.get()), float(entry_conf.get())/100, float(entry_prop.get())))

	label_n.pack()
	label_n.place(anchor="nw", relx=.1, rely=.1)
	entry_n.pack()
	entry_n.place(anchor="nw", relx=.4, rely=.1)
	label_conf.pack()
	label_conf.place(anchor="nw", relx=.1, rely=.3)
	entry_conf.pack()
	entry_conf.place(anchor="nw", relx=.4, rely=.3)
	label_prop.pack()
	label_prop.place(anchor="nw", relx=.1, rely=.5)
	entry_prop.pack()
	entry_prop.place(anchor="nw", relx=.4, rely=.5)
	button_actbp.pack()
	button_actbp.place(anchor="se", relx=.95, rely=.95)

'''Variance Confidence Interval'''
def vcis():
	vci_screen=tk.Toplevel(choose_screen)
	vci_screen.title("StatCalc-Variance Confidence Interval")
	vci_screen.geometry("500x200")
	label_n=tk.Label(vci_screen, text="n: ", font=("Times", 15))
	entry_n=tk.Entry(vci_screen, width=15)
	label_conf=tk.Label(vci_screen, text="Confidence: 		       %", font=("Times", 15))
	entry_conf=tk.Entry(vci_screen, width=15)
	label_stddev=tk.Label(vci_screen, text="Std Deviation: ", font=("Times", 15))
	entry_stddev=tk.Entry(vci_screen, width=15)
	button_actbp=tk.Button(vci_screen, text="Calculate", width=20, command=lambda:do_var_confidence_interval(int(entry_n.get()), float(entry_conf.get())/100, float(entry_stddev.get())))

	label_n.pack()
	label_n.place(anchor="nw", relx=.1, rely=.1)
	entry_n.pack()
	entry_n.place(anchor="nw", relx=.4, rely=.1)
	label_conf.pack()
	label_conf.place(anchor="nw", relx=.1, rely=.3)
	entry_conf.pack()
	entry_conf.place(anchor="nw", relx=.4, rely=.3)
	label_stddev.pack()
	label_stddev.place(anchor="nw", relx=.1, rely=.5)
	entry_stddev.pack()
	entry_stddev.place(anchor="nw", relx=.4, rely=.5)
	button_actbp.pack()
	button_actbp.place(anchor="se", relx=.95, rely=.95)

'''Initial Screen'''
choose_screen=tk.Tk()
choose_screen.title("StatCalc")
choose_screen.geometry("500x400")
welcome=tk.Label(choose_screen, text="Welcome to StatCalc, please select which statistic function you want to use:", font=("Times", 15), height=3, wraplength=450)
button_bp=tk.Button(choose_screen, text="Box Plot", width=20, command=lambda:bps())
button_hg=tk.Button(choose_screen, text="Histogram", width=20,command=lambda:hgs())
button_dp=tk.Button(choose_screen, text="Distribution Parameters", width=20, command=lambda:dps())
button_ci=tk.Button(choose_screen, text="Confidence Interval", width=20, command=lambda:cis())
button_ht=tk.Button(choose_screen, text="Hypotesis Test", width=20, command=lambda:notimplemented())
button_at=tk.Button(choose_screen, text="Adeherence Test", width=20, command=lambda:notimplemented())
button_va=tk.Button(choose_screen, text="Varience Analysis", width=20, command=lambda:notimplemented())
button_lr=tk.Button(choose_screen, text="Linear Regression", width=20, command=lambda:notimplemented())
butc=tk.Button(choose_screen, text="Exit", width=20, command=choose_screen.destroy)

welcome.pack()
welcome.place(anchor="n", relx=.5)
button_bp.pack()
button_bp.place(anchor="nw", relx=.1, rely=.25)
button_hg.pack()
button_hg.place(anchor="nw", relx=.525, rely=.25)
button_dp.pack()
button_dp.place(anchor="nw", relx=.1, rely=.4)
button_ci.pack()
button_ci.place(anchor="nw", relx=.525, rely=.4)
button_ht.pack()
button_ht.place(anchor="nw", relx=.1, rely=.55)
button_at.pack()
button_at.place(anchor="nw", relx=.525, rely=.55)
button_va.pack()
button_va.place(anchor="nw", relx=.1, rely=.7)
button_lr.pack()
button_lr.place(anchor="nw", relx=.525, rely=.7)
butc.pack()
butc.place(anchor="sw",relx=.05, rely=.95)

choose_screen.mainloop()