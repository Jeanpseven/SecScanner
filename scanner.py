import subprocess

target = input("Digite o host ou IP alvo: ")
select_tool = input("Selecione a ferramenta a ser usada (nmap, nikto, sqlmap, all): ")
output_file = input("Digite o nome do arquivo de saída (ou deixe em branco para não gerar arquivo): ")

if select_tool.lower() == "nmap" or select_tool.lower() == "all":
    nmap_command = f'nmap -v {target}'
    nmap_output = subprocess.getoutput(nmap_command)
    if output_file:
        with open(output_file + "_nmap.txt", "w") as file:
            file.write(nmap_output)

if select_tool.lower() == "nikto" or select_tool.lower() == "all":
    nikto_command = f'nikto -h {target}'
    nikto_output = subprocess.getoutput(nikto_command)
    if output_file:
        with open(output_file + "_nikto.txt", "w") as file:
            file.write(nikto_output)

if select_tool.lower() == "sqlmap" or select_tool.lower() == "all":
    sqlmap_command = f'sqlmap -u {target}'
    sqlmap_output = subprocess.getoutput(sqlmap_command)
    if output_file:
        with open(output_file + "_sqlmap.txt", "w") as file:
            file.write(sqlmap_output)

print("Operação concluída.")
