#define NMAX 100
#define ERRO 0.000001

#include <stdio.h>

//funções
double modulo(double num);

double potencia_expoente_inteiro(double base, int expoente);
double potencia(double base, double expoente);
double raiz_enesima(double base, int n);

int grau_pol_eq(double indices[NMAX]);
double* derivate_pol_eq(double indices[NMAX]);
double valor_pol_eq_no_pt(double indices[NMAX], double valor);
double raiz_da_equacao_pol(double indices[NMAX], double x0);
double* fatoracao_por_monomio(double indices[NMAX], double raiz);
double* raizes_da_equacao_pol(double indices[NMAX]);

double determinante(double matriz[NMAX][NMAX], int n);

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
	//multiplica a base por si mesma expoente vezes (necessariamente um inteiro)
	while(expoente>0){
		res=res*base;
		expoente--;
	}
	return res;
}
double raiz_enesima(double base, int n){
	int cont;
	double ind[NMAX];
	//cria vetor com -base na posicao inicial e 1 na posição n
	ind[0]=(-1)*base;
	cont=1;
	while(cont<NMAX){
		ind[cont]=0;
		cont++;
	}
	ind[n]=1;
	//a raiz do polinômio representado pelo vetor equivale a raiz n-sima de base
	return raiz_da_equacao_pol(ind, 0);
}
double potencia(double base, double expoente){
	//se o expoente for inteiro reduz-se o problema à função potencia_expoente_inteiro()
	if((int)expoente==expoente){
		return potencia_expoente_inteiro(base, (int)expoente);
	}
	int part_int, nominador, denominador;
	double part_frac, res;
	//separa o expoente na prte inteira e fracionária
	part_int=(int)expoente;
	part_frac=expoente-(double)part_int;
	//transforma a parte fracionária em denominador=NMAX-1 e nominador equivalente
	denominador=NMAX-1;
	nominador=(int)(part_frac*(double)denominador);
	//printf("%d %d %d\n", part_int, nominador, denominador);
	//calcula cada uma das partes e multiplica
	res=1;
	res*=potencia_expoente_inteiro(raiz_enesima(base, denominador), nominador);
	//printf("%f %f\n", raiz_enesima(base, denominador), res);
	res*=potencia_expoente_inteiro(base, part_int);
	//printf("%f\n", res);
	return res;
}

//equacoes
int grau_pol_eq(double indices[NMAX]){
	int cont;
	cont=NMAX-1;
	while(cont>1){
		if(indices[cont]!=0.0) return cont;
		cont--;
	}
	return 0;
}
double* derivate_pol_eq(double indices[NMAX]){
	static double deriv[NMAX];
	int cont;
	cont=0;
	//determina o coeficiente da derivada pela regra do tombo
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
	//soma cada uma das parcelas monômicas 
	while(cont<NMAX){
		res+=indices[cont]*potencia_expoente_inteiro(valor, cont);
		cont++;
	}
	return res;
}
double raiz_da_equacao_pol(double indices[NMAX], double x0){
	//método de Newton
	double *deriv=derivate_pol_eq(indices);
	while(valor_pol_eq_no_pt(deriv, x0)==0){
		x0++;
	}
	double x0ant=x0+1, funcval, tang;
	//determina o novo valor de x0 baseado no valor da função e da derivada em x0 enquanto x0 e x0ant forem demasiado distantes
	while(modulo(x0-x0ant)>ERRO){
		x0ant=x0;
		funcval=valor_pol_eq_no_pt(indices, x0);
		tang=valor_pol_eq_no_pt(deriv, x0);
		x0=x0-funcval/tang;	
		//printf("%f %f %f %f\n", x0ant, x0, funcval, tang);
	}
	return x0;
}
double* fatoracao_por_monomio(double indices[NMAX], double raiz){
	//método de Briot-Ruffini
	static double divisao[NMAX];
	double copia_indices[NMAX];
	int cont, n;
	cont=0;
	while(cont<NMAX){
		copia_indices[cont]=indices[cont];
		cont++;
	}
	cont=0;
	while(cont<NMAX){
		n=grau_pol_eq(copia_indices);
		//printf("o grau que chegou é %d\n", n);
		//printf("indices q chegou: %f %f %f %f\n", copia_indices[0], copia_indices[1], copia_indices[2], copia_indices[3]);
		divisao[cont]=0;
		cont++;
	}
	cont=n;
	//os índices do de maior grau são iguais na original e na dividida
	divisao[cont-1]=copia_indices[cont];
	cont--;
	//cada novo elemento é igual ao de ordem maior original somado ao de ordem maior dividido multiplicado pela raiz
	while(cont>0){
		divisao[cont-1]=copia_indices[cont]+divisao[cont]*raiz;
		cont--;
	}
	return divisao;
}
double* raizes_da_equacao_pol(double indices[NMAX]){
	static double raizes[NMAX];
	int cont, n;
	n=grau_pol_eq(indices);
	//printf("%d %f %f %f %f\n", grau_pol_eq(indices), indices[0], indices[1], indices[2], indices[3]);
	cont=0;
	while (cont<n){
		raizes[cont]=raiz_da_equacao_pol(indices, 0);
		//printf("%d %f %f %f %f\n", grau_pol_eq(indices), indices[0], indices[1], indices[2], indices[3]);
		indices=fatoracao_por_monomio(indices, raizes[cont]);
		cont++;
	}
	return raizes;
}

//matrizes
double determinante(double matriz[NMAX][NMAX], int n){
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
