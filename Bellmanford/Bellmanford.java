package grafosjava;

import java.util.ArrayList;
import java.util.Collections;

public class Bellmanford {	
	ArrayList<Vertice> menorCaminho = new ArrayList<Vertice>();
	
	public boolean Bellmanford (Grafos grafo, Vertice verticeInicial, Vertice verticeFinal) {
		Vertice verticeAtual = null;
		
		for(int i=0;i < grafo.getVertices().size();i++) {
			if(verticeInicial == grafo.getVertices().get(i)) {
				grafo.getVertices().get(i).distanciaMinima = 0;
			}
		}
		
		
		for(int i = 1;i<grafo.getVertices().size();i++) {
			for(int j = 0; j < grafo.getArestas().size();j++) {
				if(grafo.getArestas().get(j).getInicio().distanciaMinima + grafo.getArestas().get(j).getPeso() < grafo.getArestas().get(j).getFim().distanciaMinima) {
					grafo.getArestas().get(j).getFim().distanciaMinima = grafo.getArestas().get(j).getInicio().distanciaMinima + grafo.getArestas().get(j).getPeso();
					grafo.getArestas().get(j).getFim().anterior = grafo.getArestas().get(j).getInicio();
				}
			}
		}
		

		
		for(int j = 0; j < grafo.getArestas().size();j++) {
			if(grafo.getArestas().get(j).getInicio().distanciaMinima + grafo.getArestas().get(j).getPeso() < grafo.getArestas().get(j).getFim().distanciaMinima) {
				System.out.println("Ciclo de peso negativo detectado.");
				return false;
			}
		}
		
		
		
		verticeAtual = verticeFinal;
		while(true) {
			menorCaminho.add(verticeAtual);
			if (verticeAtual.anterior == null) break;
			verticeAtual = verticeAtual.anterior;
			
		}
		Collections.reverse(menorCaminho);
		
		System.out.println("O menor caminho entre os vertices " + verticeInicial.dados + " e " + verticeFinal.dados + " é:");
		
		for(int i=0;i< menorCaminho.size();i++) {
			if (i == menorCaminho.size() - 1) {
				System.out.print(menorCaminho.get(i).dados);
			} else {
				System.out.print(menorCaminho.get(i).dados + " -> ");
			}
		}
		
		System.out.println(" ");
		
		return true;
		
		
	}

}
