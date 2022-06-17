import java.util.ArrayList;

public class TestaMochila {
	public static void main(String[] args) {
		Mochila mochila = new Mochila(15);
		
		Item ouro = new Item("Ouro", 3, 100);
		Item prata = new Item("Prata", 2, 20);
		Item diamante = new Item("Diamante", 8, 800);
		Item cobre = new Item("Cobre", 1, 5);
		
		ArrayList<Item> items = new ArrayList<>();
		
		items.add(ouro);
		items.add(prata);
		items.add(diamante);
		items.add(cobre);
		
		
		ArrayList<Item> mochilaOtimizada = mochila.caixeiroViajante(items);
		
		for(Item item : mochilaOtimizada) {
			System.out.println(item.descricao);
		}	
	}

}
