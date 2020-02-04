#define NMAX 100
#define ERRO 0.000001

#include <stdio.h>

//funções
double modulo(double num);
double maximo(double nums[NMAX], int n);

int grau_eq_pol(double indices[NMAX]);
double* soma_eq_pol(double indicesp1[NMAX], double indicesp2[NMAX]);
double* multiplica_eq_pol_por_escalar(double indices[NMAX], double escalar);
double* multiplica_eq_pol(double indicesp1[NMAX], double indicesp2[NMAX]);
double* derivada_eq_pol(double indices[NMAX]);
double valor_eq_pol_no_pt(double indices[NMAX], double valor);
double raiz_da_eq_pol(double indices[NMAX], double x0);
double* fatoracao_por_monomio(double indices[NMAX], double raiz);
double* raizes_da_eq_pol(double indices[NMAX]);

//numeros
double modulo(double num){
	if(num<0) return (-1)*num;
	return num;
}
double maximo(double nums[NMAX], int n){
	int cont;
	double max;
	max=nums[0];
	cont=0;
	while(cont<n){
		if(max<nums[cont]) max=nums[cont];
		cont++;
	}
	return max;
}

//equacoes polinomiais
int grau_eq_pol(double indices[NMAX]){
	int cont;
	cont=NMAX-1;
	while(cont>0){
		if(indices[cont]!=0.0) return cont;
		cont--;
	}
	return 0;
}
double* soma_eq_pol(double indicesp1[NMAX], double indicesp2[NMAX]){
	static double res[NMAX];
	double graus[NMAX];
	int cont,n;
	graus[0]=grau_eq_pol(indicesp1);
	graus[1]=grau_eq_pol(indicesp2);
	n=maximo(graus, 2);
	cont=0;
	while(cont<NMAX){
		res[cont]=indicesp1[cont]+indicesp2[cont];
		cont++;
	}
	return res;
}
double* multiplica_eq_pol_por_escalar(double indices[NMAX], double escalar){
	static double res[NMAX];
	int cont, n;
	n=grau_eq_pol(indices);
	cont=0;
	while(cont<NMAX){
		if(cont<=n) res[cont]=escalar*indices[cont];
		else res[cont]=0;
		cont++;
	}
	return res;
}
double* multiplica_eq_pol(double indicesp1[NMAX], double indicesp2[NMAX]){
	static double res[2*NMAX-1];
	int cont, contt, n1, n2;
	n1=grau_eq_pol(indicesp1);
	n2=grau_eq_pol(indicesp2);
	cont=0;
	while(cont<2*NMAX-1){
		res[cont]=0;
		cont++;
	}
	cont=0;
	while(cont<=n1){
		contt=0;
		while(contt<=n2){
			res[cont+contt]+=indicesp1[cont]*indicesp2[contt];
			contt++;
		}
		cont++;
	}

	return res;
}
double* derivada_eq_pol(double indices[NMAX]){
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
double valor_eq_pol_no_pt(double indices[NMAX], double valor){
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
double raiz_da_eq_pol(double indices[NMAX], double x0){
	//método de Newton
	double *deriv=derivada_eq_pol(indices);
	while(valor_eq_pol_no_pt(deriv, x0)==0){
		x0++;
	}
	double x0ant=x0+1, funcval, tang;
	//determina o novo valor de x0 baseado no valor da função e da derivada em x0 enquanto x0 e x0ant forem demasiado distantes
	while(modulo(x0-x0ant)>ERRO){
		x0ant=x0;
		funcval=valor_eq_pol_no_pt(indices, x0);
		tang=valor_eq_pol_no_pt(deriv, x0);
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
		n=grau_eq_pol(copia_indices);
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
double* raizes_da_eq_pol(double indices[NMAX]){
	static double raizes[NMAX];
	int cont, n;
	n=grau_eq_pol(indices);
	//printf("%d %f %f %f %f\n", grau_pol_eq(indices), indices[0], indices[1], indices[2], indices[3]);
	cont=0;
	while (cont<n){
		raizes[cont]=raiz_da_eq_pol(indices, 0);
		//printf("%d %f %f %f %f\n", grau_pol_eq(indices), indices[0], indices[1], indices[2], indices[3]);
		indices=fatoracao_por_monomio(indices, raizes[cont]);
		cont++;
	}
	return raizes;
}