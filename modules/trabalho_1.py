from scapy.all import *
from collections import defaultdict
from fastapi import FastAPI

app = FastAPI()

arquivo_pcapng = "./Data/trabalho1.pcapng"
pacotes = rdpcap(arquivo_pcapng)
hosts = {}

contador_origem = defaultdict(int)
contador_destino = defaultdict(int)

for pacote in pacotes:
    if pacote.haslayer("IP"):
        endereco_origem = pacote[IP].src
        endereco_destino = pacote[IP].dst
        contador_origem[endereco_origem] += 1
        contador_destino[endereco_destino] += 1

matriz_origem = list(contador_origem.items())
matriz_destino = list(contador_destino.items())

top_10_origem = sorted(contador_origem.items(), key=lambda x: x[1], reverse=True)[:10]
top_10_destino = sorted(contador_destino.items(), key=lambda x: x[1], reverse=True)[:10]