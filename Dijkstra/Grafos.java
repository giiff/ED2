package grafosjava;

import java.util.ArrayList;


public class Grafos {
   
    ArrayList<Vertice> vertices;
    ArrayList<Aresta> arestas;

    public Grafos() {
        this.vertices = new ArrayList<Vertice>();
        this.arestas = new ArrayList<Aresta>();
    }

    public ArrayList<Vertice> getVertices() {
        return vertices;
    }

    public ArrayList<Aresta> getArestas() {
        return arestas;
    }
    public void adicionarVertice(String dado)
    {
        Vertice v = new Vertice(dado);
        vertices.add(v);
    }
    
    public void adicionarAresta(int peso, String dadoinicio,String dadofim)
    {
        Vertice inicio =  this.getVertice(dadoinicio);
        Vertice fim  =this.getVertice(dadofim);
        Aresta aresta = new Aresta(peso, inicio, fim);
        inicio.adicionarArestaSaida(aresta);
        fim.adicionarArestaEntrada(aresta);
        this.arestas.add(aresta);
    }
    public Vertice getVertice(String dado)
    {
        Vertice encontrado = null;
        
        for(int i=0;i<vertices.size();i++)
        {
            if(vertices.get(i).getDados().equals(dado))
            {
                encontrado = vertices.get(i);
                break;
            }
        }
        
        return encontrado;
    }
    
    
    public Vertice getVerticeByValue (String value) {
    	Vertice v;
    	for (int i=0; i < getVertices().size(); i++) {
    		if(getVertices().get(i).dados.equals(value)) {
    			return getVertices().get(i);
    		}
    	}
    	return null;
    }
   
    public void buscaEmLargura()
   {
       ArrayList<Vertice> marcados = new ArrayList<Vertice>();
       ArrayList<Vertice> fila = new ArrayList<Vertice>();
       Vertice atual = this.vertices.get(0);
       marcados.add(atual);
       System.out.println(atual.getDados());
       fila.add(atual);
       while(!fila.isEmpty())
       {
           Vertice visitado = fila.get(0);
           for(int i=0; i<visitado.getArestaSaida().size();i++)
           {
               Vertice proximo = visitado.getArestaSaida().get(i).getFim();
               if(!marcados.contains(proximo))
               {
                   marcados.add(proximo);
                   System.out.println(proximo.getDados());
                   fila.add(proximo);
               }
           }
           fila.remove(0);
       }
       
       
   }
   public int[][] gerarMatrizAdjacencia()
   {
       int[][] matriz =  new int[vertices.size()][vertices.size()];
       for(int i=0;i<vertices.size();i++)
       {
           for(int j=0;j<vertices.size();j++)
           {
               matriz[i][j] = 0;
           }
       }
       for(int i=0;i<vertices.size();i++)
       {
           for(int j=0;j<vertices.size();j++)
           {
               for(int k=0;k<arestas.size();k++)
               {
                   if(arestas.get(k).getInicio().getDados().equals(vertices.get(i).getDados()) && arestas.get(k).getFim().getDados().equals(vertices.get(j).getDados()) || arestas.get(k).getInicio().getDados().equals(vertices.get(j).getDados()) && arestas.get(k).getFim().getDados().equals(vertices.get(i).getDados()))
                   {
                       matriz[i][j] = arestas.get(k).getPeso();
                   }
               }
           }
       }
       
       
       
       
       for(int i=0;i<vertices.size();i++)
       {
           for(int j=0;j<vertices.size();j++)
           {
               System.out.print(matriz[i][j]+"\t");
           }
           System.out.println("");
       }
       
       return matriz;
   }
    
}
