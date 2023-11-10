# SecScanner
Usa sqlmap,nmap e nikto pra escanear um host

# Ferramentas de Varredura de Segurança

## Descrição
Este script Python permite realizar varreduras de segurança em um host ou IP alvo. Ele suporta a seleção de ferramentas específicas (nmap, nikto, sqlmap) ou todas, e oferece a opção de gerar um arquivo de saída para cada ferramenta selecionada.

## Requerimentos
- Python 3.x
- Nmap
- Nikto
- Sqlmap

## Uso
1. Execute o script `scanner.py`.
2. Insira o host ou IP alvo quando solicitado.
3. Selecione a ferramenta a ser usada (nmap, nikto, sqlmap, all) quando solicitado.
4. Insira o nome do arquivo de saída desejado quando solicitado.

## Exemplo
```
$ python scanner.py
Digite o host ou IP alvo: 192.168.1.1
Selecione a ferramenta a ser usada (nmap, nikto, sqlmap, all): all
Digite o nome do arquivo de saída (ou deixe em branco para não gerar arquivo): output_scan
Operação concluída.
```

## Saída
O script gerará arquivos de saída com a saída das ferramentas selecionadas, utilizando o nome do arquivo fornecido pelo usuário (se aplicável).

## Autor
Escrito por Wrench (jeanpseven)

Sinta-se à vontade para adicionar mais informações ou personalizá-lo de acordo com suas necessidades.
