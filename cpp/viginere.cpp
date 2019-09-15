#include<iostream>
#include<string>
int indexof(char letter, std::string pal){
	//retorna oo índice de letter em pal
	int cont, size, res;
	size=pal.length();
	res=-1;
	cont=0;
	while(cont<size){
		if(pal[cont]==letter){
			res=cont;
			break;
		}
		cont++;
	}
	return res;
}
#define alphabet "abcdefghijklmnopqrstuvwxyz"
std::string enciphervig(std::string in, std::string key){
	//encripta por VIGINERE e retorna a string encriptada
	int cont, npal, nkey;
	std::string out;
	npal=in.length();
	nkey=key.length();
	cont=0;
        while(cont<npal){
		if(in[cont]!=' '){
			out+=alphabet[(indexof(in[cont],alphabet)+indexof(key[cont%nkey],alphabet))%26];
		}
                cont++;
        }
	return out;
}
std::string deciphervig(std::string in, std::string key){
	//decripta por VIGINERE e retorna a string decriptada
	int cont, npal, nkey;
	std::string out;
	npal=in.length();
	nkey=key.length();
	cont=0;
	while(cont<npal){
		out+=alphabet[(indexof(in[cont], alphabet)-indexof(key[cont%nkey], alphabet)+26)%26];
		cont++;
	}
	return out;
}
void tratastring(std::string& texto){
	//substitui maiúsculas por minúsculas e retira outros caracteres (incluindo espaços)
	std::string res;
	int size, cont;
	size=texto.length();
	cont=0;
	while(cont<size){
		if(texto[cont]>=65&&texto[cont]<=90){
			res+=texto[cont]+32;
		}else if(texto[cont]>=97&&texto[cont]<=122){
			res+=texto[cont];
		}
		cont++;
	}
	texto=res;
}
void opcoes_de_cifra(){
	//printa as opções de cifra disponíveis
	std::cout<<"1)'Cesar' ou 'cesar' ou 'c'"<<std::endl;
	std::cout<<"2)'Viginere' ou 'viginere' ou 'v'"<<std::endl;
	std::cout<<"3)'Playfair' ou 'playfair' ou 'p'"<<std::endl;
}
int main(){
	std::string key, in, out, escolha;
	std::cout<<"Bem-vindo ao programa de cifras do Tio Miguel"<<std::endl;
	while(true){
		std::cout<<"Cifra:";
		std::getline(std::cin, escolha);
		if(escolha=="h"||escolha=="help"){
			opcoes_de_cifra();
		}else if(escolha=="cesar"||escolha=="Cesar"||escolha=="c"){
			std::cout<<"Chave: ";
			std::cin>>key;
			if(key.size()!=1){
				std::cout<<"Chave inapropriada."<<std::endl;
			}else{
				
			}
		}
	}
	return 0;
}
