
public class Item {
	String descricao;
	double peso;
	double valor;
	double media;
	
	public Item(String descricao, double peso, double valor) {
		this.descricao = descricao;
		this.peso = peso;
		this.valor = valor;
		this.media = valor/peso;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public double getPeso() {
		return peso;
	}

	public void setPeso(double peso) {
		this.peso = peso;
	}

	public double getValor() {
		return valor;
	}

	public void setValor(double valor) {
		this.valor = valor;
	}

	public double getMedia() {
		return media;
	}

	public void setMedia(double media) {
		this.media = media;
	}
	
	

}
