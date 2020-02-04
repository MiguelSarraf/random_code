#include "polinomios.h"
#include <stdio.h>

double potencia_expoente_inteiro(double base, int expoente);
double potencia(double base, double expoente);
double raiz_enesima(double base, int n);

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
	return raiz_da_eq_pol(ind, 0);
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
