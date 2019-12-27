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
			res=res+potencia(-1,cont)*matriz[0][cont]*determinante(matrizaux, n-1);
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
		sort(vet, esq, param);
		sort(vet, param+1, dir);
		return;
	}else{
		return;
	}
}
