double potencia_expoente_inteiro(double base, int expoente){
	double res;
	res=1;
	while(expoente>0){
		res=res*base;
		expoente--;
	}
	return res;
}
double raiz(double base, int radicando){
	if(radicando==1||base==1){
		return base;
	}
	double res, potencia;
	res=base;
	potencia=potencia_expoente_inteiro(res, radicando);
	while(potencia>base){
		res=res/2;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	while(potencia<base){
		res++;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	res--;
	potencia=potencia_expoente_inteiro(res, radicando);
	while(potencia<base){
		res=res+0.1;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	res=res-0.1;
	potencia=potencia_expoente_inteiro(res, radicando);
	while(potencia<base){
		res=res+0.01;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	res=res-0.01;
	potencia=potencia_expoente_inteiro(res, radicando);
	while(potencia<base){
		res=res+0.001;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	res=res-0.001;
	potencia=potencia_expoente_inteiro(res, radicando);
	while(potencia<base){
		res=res+0.0001;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	res=res-0.0001;
	potencia=potencia_expoente_inteiro(res, radicando);
	while(potencia<base){
		res=res+0.00001;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	res=res-0.00001;
	potencia=potencia_expoente_inteiro(res, radicando);
	while(potencia<base){
		res=res+0.000001;
		potencia=potencia_expoente_inteiro(res, radicando);
	}
	res=res-0.000001;
	return res;
}
double potencia(double base, double expoente){
	if(expoente==1){
		return base;
	}
	double res, res1;
	res=1;
	if(base<0){
		if((int)expoente!=expoente){
			return 0;
		}
		base=-base;
		if((int)expoente%2==1){
			res=-1;
		}
	}
	expoente=expoente*10;
	res1=potencia_expoente_inteiro(base, (int)expoente);
	res=res*raiz(res1, 10);
	return res;
}
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
			res=res+potencia(-1,cont)*matriz[0][cont]*determinante(matrizaux, n-1);
			cont++;
		}
		return res;
	}
}
void sort(double vet[], int esq, int dir){
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
		sort(vet, esq, param);
		sort(vet, param+1, dir);
		return;
	}else{
		return;
	}
}
#define NMAX 100
#include<stdlib.h>
double pi(){
	int cont;
	double res;
	cont=100;
	res=0;
	while(cont>0){
		res=res+potencia(-1, cont+1)/(2*cont-1);
		cont--;
	}
	res=res*4;
	//res=raiz(res, 2);
	return res;
}
