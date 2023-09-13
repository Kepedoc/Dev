/**
 * Generuje tabliczkę mnożenia o zadanych wymiarach i zwraca ją w postaci tabeli html.
 * @param {number} [rows=10] - liczba wierszy.
 * @param {number} [cols=10] - liczba kolumn.
 * @param {number} [minX=1] - minimalna wartość mnożnika dla kolumn.
 * @param {number} [minY=1] - minimalna wartość mnożnika dla wierszy.
 * @returns {string} - tabela html.
 */
function tabliczka(rows = 10, cols = 10, minX = 1, minY = 1) {
    let table = '<table>\n';
    
    // nagłówek tabeli
    table += '<thead>\n<tr><th></th>';
    for (let x = minX; x < minX + cols; x++) {
      table += `<th>${x}</th>`;
    }
    table += '</tr>\n</thead>\n';
    
    // ciało tabeli
    table += '<tbody>\n';
    for (let y = minY; y < minY + rows; y++) {
      table += '<tr>';
      table += `<th>${y}</th>`;
      for (let x = minX; x < minX + cols; x++) {
        table += `<td>${x * y}</td>`;
      }
      table += '</tr>\n';
    }
    table += '</tbody>\n';
    
    table += '</table>';
    return table;
  }

  // wywołanie z domyślnymi wartościami
console.log(tabliczka()); 

// wywołanie z 5 wierszami i 7 kolumnami
console.log(tabliczka(5, 7)); 

// wywołanie z 5 wierszami i 5 kolumnami począwszy od 3 i 4
console.log(tabliczka(5, 5, 3, 4)); 