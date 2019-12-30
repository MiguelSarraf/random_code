#define NMAX 100
#define ERRO 0.000001

#include <stdio.h>

//functions
double modulo(double num);
double potencia_expoente_inteiro(double base, int expoente);
double raiz_enesima(double base, int n);
double* derivate_pol_eq(double indices[NMAX]);
double valor_pol_eq_no_pt(double indices[NMAX], double valor);
double* raiz_da_equacao_pol(double indices[NMAX]);
double determinante(double matriz[10][10], int n);
void quick_sort(double vet[NMAX], int esq, int dir);

//numeros
double modulo(double num){
	if(num<0) return (-1)*num;
	return num;
}

//potencias
double potencia_expoente_inteiro(double base, int expoente){
	double res;
	res=1;
	while(expoente>0){
		res=res*base;
		expoente--;
	}
	return res;
}
double raiz_enesima(double base, int n){
	int cont;
	double ind[NMAX];
	ind[0]=(-1)*base;
	cont=1;
	while(cont<NMAX){
		ind[cont]=0;
		cont++;
	}
	ind[n]=1;
	return *raiz_da_equacao_pol(ind);
}

//equacoes
double* derivate_pol_eq(double indices[NMAX]){
	static double deriv[NMAX];
	int cont;
	cont=0;
	while(cont<NMAX-1){
		deriv[cont]=indices[cont+1]*(cont+1);
		cont++;
	}
	deriv[NMAX]=0;
	return deriv;
}

double valor_pol_eq_no_pt(double indices[NMAX], double valor){
	int cont;
	static double res;
	cont=0;
	res=0;
	while(cont<NMAX){
		res+=indices[cont]*potencia_expoente_inteiro(valor, cont);
		cont++;
	}
	return res;
}

double* raiz_da_equacao_pol(double indices[NMAX]){
	double *deriv=derivate_pol_eq(indices);
	static double x0=0.5;
	double x0ant=1, funcval, tang;
	while(modulo(x0-x0ant)>ERRO){
		x0ant=x0;
		funcval=valor_pol_eq_no_pt(indices, x0);
		tang=valor_pol_eq_no_pt(deriv, x0);
		x0=x0-funcval/tang;	
		//printf("%f %f %f %f\n", x0ant, x0, funcval, tang);
	}
	return &x0;
}

//matrizes
double determinante(double matriz[10][10], int n){
	double matrizaux[10][10], res;
	int cont, contt, conttt;
	res=0;
	if(n==1){
		return matriz[0][0];
	}else if(n==2){
		return (matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]);
	}else{
		cont=0;
		while(cont<n){
			contt=1;
			while(contt<n){
				conttt=0;
				while(conttt<n){
					if(conttt==cont){
						conttt++;
					}
					if(conttt>cont){
						matrizaux[contt-1][conttt-1]=matriz[contt][conttt];
					}else{
						matrizaux[contt-1][conttt]=matriz[contt][conttt];
					}
					conttt++;
				}
				contt++;
			}
			//res=res+potencia(-1,cont)*matriz[0][cont]*determinante(matrizaux, n-1);
			cont++;
		}
		return res;
	}
}

//sort
void quick_sort(double vet[], int esq, int dir){
	if(dir>esq){
		int param, cont, aux;
		param=esq;
		cont=esq;
		while(cont<dir){
			if(cont==param){
				cont++;
			}
			if(vet[cont]<vet[param]&&cont>param){
				if(cont==param+1){
					aux=vet[cont];
					vet[cont]=vet[param];
					vet[param]=aux;
				}else{
					aux=vet[param+1];
					vet[param+1]=vet[param];
					vet[param]=aux;
					aux=vet[cont];
					vet[cont]=vet[param];
					vet[param]=aux;
				}
				param++;
			}else if(vet[cont]>vet[param]&&cont<param){
				if(cont==param-1){
					aux=vet[cont];
					vet[cont]=vet[param];
					vet[param]=aux;
				}else{
					aux=vet[param-1];
					vet[param-1]=vet[param];
					vet[param]=aux;
					aux=vet[cont];
					vet[cont]=vet[param];
					vet[param]=aux;
				}
				param--;
			}
			cont++;
		}
		cont=0;
		quick_sort(vet, esq, param);
		quick_sort(vet, param+1, dir);
		return;
	}else{
		return;
	}
}
