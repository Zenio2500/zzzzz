#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, vetor[2000000], inicio, fim, meio, i, soma, resposta;
    scanf("%d %d", &n, &m);
    inicio=0;
    fim=n-1;
    for(i=0;i<n;i++){
        scanf("%d", &vetor[i]);
    }
    sort(vetor, vetor + n);
    while(inicio<=fim){
        meio = (inicio+fim)/2;
        soma=0;
        for(i=meio+1; i<n; i++){
            soma += vetor[i]-vetor[meio];
        }
        if(soma==m){
            printf("%d", vetor[meio]);
            break;
        }
        else{
            if(soma<m){
                fim = meio-1;
            }
            else{
                resposta = vetor[meio];
                inicio = meio+1;              
            }            
        }
    }
    if(inicio>fim){
        printf("%d", resposta);
    }
	return 0;
}