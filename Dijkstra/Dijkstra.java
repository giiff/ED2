package grafosjava;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Dijkstra {
	ArrayList<Vertice> verticesAbertos = new ArrayList<Vertice>();
	ArrayList<Vertice> menorCaminho = new ArrayList<Vertice>();
	
	
	
	
	public void  shortestPath (Grafos grafo, Vertice verticeInicial, Vertice verticeFinal) {
		Vertice verticeAtual = null;
		for(int i=0;i < grafo.getVertices().size();i++) {
			if(verticeInicial == grafo.getVertices().get(i)) {
				grafo.getVertices().get(i).distanciaMinima = 0;
				verticesAbertos.add(grafo.getVertices().get(i));
			}
		}
		
		
		
		while(!verticesAbertos.isEmpty()) {
			verticeAtual = verticesAbertos.get(0);
			for(int i =0;i < verticeAtual.getArestaSaida().size(); i++) {
				if(verticeAtual.distanciaMinima + verticeAtual.getArestaSaida().get(i).peso < verticeAtual.getArestaSaida().get(i).fim.distanciaMinima) {
					verticeAtual.getArestaSaida().get(i).fim.distanciaMinima = verticeAtual.distanciaMinima + verticeAtual.getArestaSaida().get(i).peso;
					verticeAtual.getArestaSaida().get(i).fim.anterior = verticeAtual;
					verticesAbertos.add(verticeAtual.getArestaSaida().get(i).fim);
				}
			}
			verticesAbertos.remove(0);
			Collections.sort(verticesAbertos, new SortByDistanciaMinima());
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
		
		System.out.println("O menor caminho entre os vertices " + verticeInicial.dados + " e " + verticeFinal.dados + " é:");
		
		for(int i=0;i< menorCaminho.size();i++) {
			if (i == menorCaminho.size() - 1) {
				System.out.print(menorCaminho.get(i).dados);
			} else {
				System.out.print(menorCaminho.get(i).dados + " -> ");
			}
		}
		
	}
}
