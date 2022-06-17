
package grafosjava;

import java.util.ArrayList;

public class Vertice implements Comparable<Vertice>{

String dados;
ArrayList<Aresta> arestaEntrada;
ArrayList<Aresta> arestaSaida;
ArrayList<Vertice> adjacentes = new ArrayList<Vertice>();
double distanciaMinima = Double.POSITIVE_INFINITY;
Vertice anterior = null;

    public Vertice(String dados) {
        this.dados = dados;
        arestaEntrada = new ArrayList<Aresta>();
        arestaSaida = new ArrayList<Aresta>();
    }


    public String getDados() {
        return dados;
    }

    public void setDados(String dados) {
        this.dados = dados;
    }

    public ArrayList<Aresta> getArestaEntrada() {
        return arestaEntrada;
    }

    public ArrayList<Aresta> getArestaSaida() {
        return arestaSaida;
    }
   public void adicionarArestaEntrada(Aresta a)
   {
       this.arestaEntrada.add(a);
   }
   public void adicionarArestaSaida(Aresta a)
   {
     this.arestaSaida.add(a);   
   }

   public ArrayList<Vertice> getAdjacentes(){
	   this.adjacentes.clear();
	   for(int i=0;i<getArestaSaida().size();i++) {
		   this.adjacentes.add(getArestaSaida().get(i).getFim());
	   }
	   return this.adjacentes;
   }
   
    @Override
    public int compareTo(Vertice o) {
        return Double.compare(distanciaMinima, o.distanciaMinima);
    }
    
}
