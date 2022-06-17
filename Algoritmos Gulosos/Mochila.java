import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Mochila {
	int peso;
	
	public Mochila(int peso) {
		this.peso = peso;
	}
	
	
	public ArrayList<Item> caixeiroViajante(ArrayList<Item> items){
		items.sort(Comparator.comparing(Item::getMedia));
		Collections.reverse(items);
		ArrayList<Item> mochilaOtimizada = new ArrayList<Item>();
		int pesoDisponivel = this.peso;
		
		
		
		int contador = 0;
		
		while(contador < items.size()) {
			if(items.get(contador).getPeso() <= pesoDisponivel) {
				mochilaOtimizada.add(items.get(contador));
				pesoDisponivel -= items.get(contador).getPeso();
			}else{
				contador++;
			}
		}
		
		return mochilaOtimizada;
	}

}
