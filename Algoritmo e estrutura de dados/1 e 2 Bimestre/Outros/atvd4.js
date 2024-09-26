let fruta
fruta = ''
switch (fruta) {
    case 'maca':
        console.log(`O preço da maca é: $0.59 o kg`);
        break;
    case 'laranja':
        console.log(`O preço da laranja: $0.32 o kg`);
        break;
    case 'banana':
        console.log(`O preço da banana é; $0.48 o kg`);
        break;
    case 'cereja':
        console.log(`O preço da cereja é: $3 o kg`);
        break;
    case 'mamao':
    case 'manga':
        console.log(`as mangas e os mamões custam $3.79 o kg`)
    default:
        console.log(`Produto Indisponível`)
}