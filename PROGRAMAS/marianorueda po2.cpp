#include <stdio.h>
#include <malloc.h>
#include <string.h>

struct datos{
	char ayn[50];
	int dni;
	int edad;
};

struct nodo{
	char ayn[50];
	int dni;
	int edad;
	struct nodo *sig;
};

typedef struct nodo *puntero;

void carga(datos *xA, int xcant){
	int i;
	for(i=0;i<xcant;i++){
		printf("Ingrese Apellido y Nombre %d \n", i+1);
		fflush(stdin);
		gets(xA[i].ayn);
		printf("Ingrese dni %d \n", i+1);
		scanf("%d",&xA[i].dni);
		printf("Ingrese edad %d \n", i+1);
		scanf("%d",&xA[i].edad);
	}
}

void mostrar_mas_50(datos *xA, int xcant, int i){
	if(i==xcant){
		return;
	}
	else{
		if(xA[i].edad>50){
			printf("%s\n",xA[i].ayn);
			printf("%d\n",xA[i].dni);
			printf("%d\n",xA[i].edad);
		}
		mostrar_mas_50(xA,xcant,i+1);
	}
}

void buscar(datos &xA, int xcant){
	int xdni, i=0;
	printf("Ingrese el DNI del socio a buscar\n");
	fflush(stdin);
	scanf("%d",&xdni);
	while((i<xcant)&&(xdni!=xA[i].dni)){
			i++;
		}
	if(i==xcant){
		printf("El dni ingresado no se encontro\n");
	}
	else{
		printf("El apellido y nombre del socio es %s\n",xA[i].ayn);
	}
}

void pasar_lista(datos *xA, puntero &xp, int xcant){
	int i=0;
	puntero nuevo;
	for(i=0;i<xcant;i++){
		if(xA[i].edad>=21){
		nuevo=(puntero)malloc(sizeof(struct nodo));	
		strcpy(nuevo->ayn,xA[i].ayn);
		nuevo->dni=xA[i].dni;
		nuevo->edad=xA[i].edad;
		nuevo->sig=xp;
		xp=nuevo;
		}
	}
}

void mostrar_lista(puntero xp){
	printf("La lista actualizada de socios es:\n");
	while(xp!=NULL){
		printf("Nombre: %s\n",xp->ayn);
		printf("DNI: %d\n",xp->dni);
		printf("Edad: %d\n",xp->edad);
		xp=xp->sig;
	}
}

int main(){
	puntero cabeza;
	int cant,i=0;
	datos *A;
	cabeza=NULL;
	printf("Ingrese el numero de socios \n");
	scanf("%d",&cant);
	A=(datos*)malloc(sizeof(datos)*cant);
	carga(A,cant);
	printf("Los socios mayores a 50 años son: \n");
	mostrar_mas_50(A,cant,i);
	buscar(A,cant);
	pasar_lista(A,cabeza,cant);
	free(A);
	mostrar_lista(cabeza);
}