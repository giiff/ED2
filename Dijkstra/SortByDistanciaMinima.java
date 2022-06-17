package grafosjava;

import java.util.Comparator;

public class SortByDistanciaMinima implements Comparator<Vertice> {
    public int compare(Vertice a, Vertice b)
    {
 
        return Double.compare(a.distanciaMinima, b.distanciaMinima);
    }

}
