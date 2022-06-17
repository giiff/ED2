import java.util.ArrayList;

public class Conta {
	int saldo;
	ArrayList<Nota> notas;;
	
	public Conta (int saldo) {
		this.saldo = saldo;
		this.notas = new ArrayList<Nota>();
		
		Nota duzentos = new Nota(200);
		Nota cem = new Nota(100);
		Nota cinquenta = new Nota(50);
		Nota vinte = new Nota(20);
		Nota dez = new Nota(10);
		Nota cinco = new Nota(5);
		Nota dois = new Nota(2);
		Nota um = new Nota(1);
		
		notas.add(duzentos);
		notas.add(cem);
		notas.add(cinquenta);
		notas.add(vinte);
		notas.add(dez);
		notas.add(cinco);
		notas.add(dois);
		notas.add(um);
	}
	
	public void sacaroMaximoDeNotas() {
		int valorRestante = this.saldo;
		int contador = 0;
		int numeroDeNotas = 0;
		
		while(true) {
			if(notas.get(contador).getValor() <= valorRestante) {
				valorRestante -= notas.get(contador).valor;
				numeroDeNotas++;
			} else {
				System.out.println(numeroDeNotas + " nota(s) de " + notas.get(contador).valor);
				numeroDeNotas = 0;
				contador++;
				if (valorRestante == 0) break;
			}
		}
	}

}
