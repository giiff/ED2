package grafosjava;

import java.util.ArrayList;

/**
 *
 * @author Afranio
 */
public class GrafosJava {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
                
        Grafos grafo = new Grafos();
        grafo.adicionarVertice("A");
        grafo.adicionarVertice("B");
        grafo.adicionarVertice("C");
        grafo.adicionarVertice("D");
        grafo.adicionarVertice("E");
        grafo.adicionarVertice("F");
        
        grafo.adicionarAresta(10, "A", "B");
        grafo.adicionarAresta(15, "A", "C");
        grafo.adicionarAresta(12, "B", "D");
        grafo.adicionarAresta(15, "B", "F");
        grafo.adicionarAresta(10, "C", "E");
        grafo.adicionarAresta(2, "D", "E");
        grafo.adicionarAresta(1, "D", "F");
        grafo.adicionarAresta(5, "F", "E");
        
        Grafos negativeCycleGrafo = new Grafos();
        
        negativeCycleGrafo.adicionarVertice("A");
        negativeCycleGrafo.adicionarVertice("B");
        negativeCycleGrafo.adicionarVertice("C");
        negativeCycleGrafo.adicionarVertice("D");
        
        negativeCycleGrafo.adicionarAresta(1, "A", "B");
        negativeCycleGrafo.adicionarAresta(-1, "B", "C");
        negativeCycleGrafo.adicionarAresta(-1, "C", "D");
        negativeCycleGrafo.adicionarAresta(-1, "D", "A");
        
        Bellmanford  b = new Bellmanford();
        
        System.out.println(b.Bellmanford(grafo, grafo.getVerticeByValue("A"), grafo.getVerticeByValue("E")));
        
        System.out.println(b.Bellmanford(negativeCycleGrafo, negativeCycleGrafo.getVerticeByValue("A"), negativeCycleGrafo.getVerticeByValue("D")));
        

        
    }   
    
}
