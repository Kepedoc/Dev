#include <iostream>

using namespace std;

int main() {

	int size = 0;
	cout <<	"podaj rozmiar tablicy!\n";
	cin >> size;
	int *tablica = new int[size];

	for(int i = 0 ; i < size ; i++ ){
		tablica[i] = i;
		cout << tablica[i];
	}
	delete tablica;
}

//1. Stwórz plik nagłówkowy dla swojej implementacji wektora. Umieść w nim wszystko co niezbędne.
//Zastanów się jakie funkcje mogą być przydatne. Może przyda się funkcja, która będzie wypisywała
//czytelnie na ekran całą zawartość wektora?
//2. Po przygotowaniu pliku nagłówkowego stwórz plik źródłowy i umieść w nim na razie puste definicje dla funkcji znajdujących się w pliku nagłówkowym.
//3. Zaimplementuj oba konstruktory oraz destruktor dla swojego wektora.
//4. W funkcji main. Stwórz egzemplarz klasy MyVector używając któregoś z konstruktorów.
