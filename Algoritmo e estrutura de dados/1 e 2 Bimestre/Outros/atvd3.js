let permissao
permissao = 'jorgin'
switch (permissao) {
    case 'vendedor':
        console.log(`acesso local`);
        break;
    case 'gerente':
        console.log(`acesso regional`);
        break;
    case 'diretor':
        console.log(`acesso total`);
        break;
    default: 
    console.log(`Pemissão Negada`)    
    }
