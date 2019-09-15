#include <iostream>
#include <string>
#include <vector>

#define N_MAX_OBJS 100

class Objeto{
private:
	std::string name;
	int width, height;
public:
	Objeto(std::string n, int w, int h, bool printa){
		name=n;
		width=w;
		height=h;
		if(printa){
			std::cout<<"Objeto criado com sucesso"<<std::endl;
		}
	}
	std::string get_name(){
		return name;
	}
	int get_width(){
		return width;
	}
	int get_height(){
		return height;
	}
};
class Parede{
private:
	int width, height, n_objs=0, pos[N_MAX_OBJS][2];
	float scale_x, scale_y;
	std::string name;
	std::vector<Objeto> objs;
public:
	Parede(std::string nome, int w, int h){
		int cont;
		name=nome;
		width=w;
		height=h;
		scale_x=48/float(width);
		scale_y=51/float(height);
		cont=0;
		std::cout<<"Parede criada com sucesso."<<std::endl;
	}
	//retorna o nome da parede
	std::string get_name(){
		return name;
	}
	//retorna a largura da parede
	int get_width(){
		return width;
	}
	//retorna a altura da parede
	int get_height(){
		return height;
	}
	//retorna o numero de objetos pendurados na parede
	int get_n_objs(){
		return n_objs;
	}
	//retorna o nome do objeto na posicao ind do vector de objetos
	std::string get_name(int ind){
		return objs[ind].get_name();
	}
	//confere se haverá alguma inteseccao se um objeto obj for colocado em (x, y)
	bool intersection(Objeto obj, int x, int y){
		int cont;
		cont=0;
		while(cont<n_objs){
			if( ((x>=pos[cont][0]  &&  x<=pos[cont][0]+objs[cont].get_width()-1)  || (x+obj.get_width()>=pos[cont][0]   &&  x+obj.get_width()<=pos[cont][0]+objs[cont].get_width()-1)) && 
				((y>=pos[cont][1]  &&  y<=pos[cont][1]+objs[cont].get_height()-1) || (y+obj.get_height()>=pos[cont][1]  &&  y+obj.get_height()<=pos[cont][1]+objs[cont].get_height()-1))){
				return true;
			}
			cont++;
		}
		return false;
	}
	//pendura um objeto obj na posicao (x, y)
	void add_object(Objeto obj, int x, int y){
		if(intersection(obj, x, y)){
			std::cout<<"Objeto não pode ser colocado nesta posição"<<std::endl;
			return;
		}
		objs.push_back(obj);
		pos[n_objs][0]=x;
		pos[n_objs][1]=y;
		std::cout<<"Objeto pendurado com sucesso."<<std::endl;
		n_objs++;
	}
	//retorna o nome do objeto pendurado em (x, y) se houver
	std::string object_in(int x, int y){
		int cont;
		cont=0;
		while(cont<n_objs){
			if((x>=pos[cont][0] && x<=pos[cont][0]+objs[cont].get_width()) && (y>=pos[cont][1] && y<=pos[cont][1]+objs[cont].get_height())){
				return objs[cont].get_name();
			}else{
				return "Não existe objeto nesta posição";
			}
		}
	}
	//remove o obejto dado seu nome
	void rmv_object(std::string nome){
		int cont;
		cont=0;
		while(cont<n_objs){
			if(objs[cont].get_name()==nome){
				break;
			}
			cont++;
		}
		if(cont==n_objs){
			std::cout<<"Não existe objeto especificado"<<std::endl;
			return;
		}
		n_objs--;
		std::cout<<"Objeto removido com sucesso"<<std::endl;
	}
	//move o objeto de nome nome para a posicao (x, y)
	void mv_object(std::string nome, int x, int y){
		int cont;
		cont=0;
		while(cont<n_objs){
			if(objs[cont].get_name()==nome){
				break;
			}
			cont++;
		}
		if(cont==n_objs){
			std::cout<<"Não existe objeto especificado"<<std::endl;
			return;
		}
		n_objs--;
		add_object(objs[cont], x, y);
	}
	//identifica qual forma de impressao deve ser usada
	void print(){
		if(scale_x>=1 && scale_y>=1){
			print_normal();
		}else{
			print_escalado();
		}
	}
	//imprime na tela sem aplicar escala
	void print_normal(){
		int cont, contt;
		Objeto teste("", 1, 1, false);
		std::cout<<" 0"<<"+";
		cont=0;
		while(cont<width){
			std::cout<<"--";
			cont++;
		}
		std::cout<<"+"<<std::endl;
		cont=0;
		while(cont<height){
			std::cout<<"  |";
			contt=0;
			while(contt<width){
				Objeto teste("", 0, 0, false);
				if(intersection(teste, contt, cont)){
					std::cout<<"* ";
				}else{
					std::cout<<"  ";
				}
				contt++;
			}
			std::cout<<"|"<<std::endl;
			cont++;
		}
		if(height<10){
			std::cout<<" ";
		}
		std::cout<<height<<"+";
		cont=0;
		while(cont<width){
			std::cout<<"--";
			cont++;
		}
		std::cout<<"+"<<std::endl;
		std::cout<<" 0";
		cont=0;
		while(cont<width){
			std::cout<<"  ";
			cont++;
		}
		std::cout<<" "<<width<<std::endl;
	}
	//imprime na tela aplicando escala em x e y
	void print_escalado(){
		int cont, contt;
		float scale;
		scale=std::min(scale_x, scale_y);
		std::cout<<" 0"<<"+";
		cont=0;
		while(cont<width*scale){
			std::cout<<"--";
			cont++;
		}
		std::cout<<"+"<<std::endl;
		cont=0;
		while(cont<height*scale){
			std::cout<<"  |";
			contt=0;
			while(contt<width*scale){
				Objeto teste("", 0, 0, false);
				if(intersection(teste, float(contt)*scale, float(cont)*scale)){
					std::cout<<"* ";
				}else{
					std::cout<<"  ";
				}
				contt++;
			}
			std::cout<<"|"<<std::endl;
			cont++;
		}
		if(height<10){
			std::cout<<" ";
		}
		std::cout<<height<<"+";
		cont=0;
		while(cont<width*scale){
			std::cout<<"--";
			cont++;
		}
		std::cout<<"+"<<std::endl;
		std::cout<<"  0";
		cont=0;
		while(cont<width*scale){
			std::cout<<"  ";
			cont++;
		}
		std::cout<<width<<std::endl;
	}
};
//separa a cadeia todo em partes usando " " como separador
void separa(std::string todo, std::vector<std::string> *partes){
	int cont;
	std::string crop;
	cont=0;
	crop="";
	std::cout<<"a ";
	while(cont<todo.length()){
		if(todo[cont]==*" "){
			if(crop!=""){
				partes->push_back(crop);
				crop="";
			}
		}else{
			crop+=todo[cont];
		}
		std::cout<<cont<<" ";
		cont++;
	}
}
//mostra mensagem de erro caso seja recebido número errado de parâmetros em uma função
void erro_parametro(std::vector<std::string> parametros, int num_param){
	if(parametros.size()<num_param+1){
		std::cout<<"Instrução "<<parametros[0]<<" com falta de parâmetros, o número correto de parâmetros a ser inserido é "<<num_param;
	}else{
		std::cout<<"Instrução "<<parametros[0]<<" com excesso de parâmetros, o número correto de parâmetros a ser inserido é "<<num_param;
	}
}
int main(){
	int w, h, cont, contt;
	bool pass;
	std::string comando, nome_o, nome_p;
	std::vector<Parede> paredes;
	std::vector<Objeto> objetos;
	std::vector<std::string> parametros;
	while(true){
		std::cout<<"oq quer fazer?"<<std::endl;
		std::cin>>comando;
		std::cout<<"manda ";
		separa(comando, &parametros);
		if (parametros[0]=="he"){
			if (parametros.size()==1){
				std::cout<<"'he': lista de comandos"<<std::endl<<
						   "'np' [nome] [largura] [altura]: cria nova parede"<<std::endl<<
						   "'no' [nome] [largura] [altura]: cria novo objeto"<<std::endl<<
						   "'po' [nome_do_objeto] [nome_da_parede] [pos_x] [pos_y]: coloca um objeto numa parede"<<std::endl<<
						   "'pr' [nome_da_parede]: mostra uma parede a tela"<<std::endl<<
						   "'oi' [pos_x] [pos_y] [nome_da_parede]: retorna o nome do objeto em determinada posição"<<std::endl<<
						   "'rm' [nome_do_objeto] [nome_da_parede]: remove um objeto de uma parede"<<std::endl<<
						   "'mv' [nome_do_objeto] [nome_da_parede] [pos_x] [pos_y]: move um objeto numa parede"<<std::endl;
			}else{
				erro_parametro(parametros, 0);
			}
		}else if(parametros[0]=="np"){
			if (parametros.size()==4){
				std::cin>>nome_p>>w>>h;
				paredes.push_back(Parede(nome_p, w, h));
			}else{
				erro_parametro(parametros,3);
			}
		}else if(parametros[0]=="no"){
			std::cin>>nome_o>>w>>h;
			objetos.push_back(Objeto(nome_o, w, h, true));
		}else if(parametros[0]=="po"){
			std::cin>>nome_o>>nome_p>>w>>h;
			cont=0;
			pass=true;
			while(cont<objetos.size()){
				if(objetos[cont].get_name()==nome_o){
					break;
				}
				cont++;
			}
			if(cont==objetos.size()){
				std::cout<<"Não existe objeto especificado"<<std::endl;
				pass=false;
			}
			contt=0;
			while(cont<paredes.size()){
				if(paredes[contt].get_name()==nome_p){
					break;
				}
				cont++;
			}
			if(contt==paredes.size()){
				std::cout<<"Não existe parede especificada"<<std::endl;
				pass=false;
			}
			if(pass){
				paredes[contt].add_object(objetos[cont], w, h);
			}
		}else if(parametros[0]=="pr"){
			std::cin>>nome_p;
			cont=0;
			pass=true;
			while(cont<paredes.size()){
				if(paredes[cont].get_name()==nome_p){
					break;
				}
				cont++;
			}
			if(cont==paredes.size()){
				std::cout<<"Não existe a parede especificada"<<std::endl;
				pass=false;
			}
			if(pass){
				paredes[cont].print();
			}
		}else if(parametros[0]=="oi"){
			std::cin>>w>>h>>nome_p;
			cont=0;
			while(cont<paredes.size()){
				if(paredes[cont].get_name()==nome_p){
					std::cout<<paredes[cont].object_in(w, h)<<std::endl;
					break;
				}
				cont++;
			}
			if(cont==paredes.size()){
				std::cout<<"Não existe parede especificada"<<std::endl;
			}
		}else if(parametros[0]=="rm"){
			std::cin>>nome_o>>nome_p;
			cont=0;
			while(cont<paredes.size()){
				if(paredes[cont].get_name()==nome_p){
					break;
				}
				cont++;
			}
			if(cont==paredes.size()){
				std::cout<<"Não existe parede especificada"<<std::endl;
			}
			paredes[cont].rmv_object(nome_o);
		}else if(parametros[0]=="mv"){
			std::cin>>nome_o>>nome_p>>w>>h;
			cont=0;
			while(cont<paredes.size()){
				if(paredes[cont].get_name()==nome_p){
					break;
				}
				cont++;
			}
			if(cont==paredes.size()){
				std::cout<<"Não existe parede especificada"<<std::endl;
			}
			paredes[cont].mv_object(nome_o, w, h);
		}else{
			std::cout<<"Comando não reconhecido"<<std::endl;
			std::cin.clear();
			std::cin.ignore(100, '\n');
		}
	}
	return 0;
}