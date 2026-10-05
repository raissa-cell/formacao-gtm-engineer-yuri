# Mapa DDD → UF e Região

> Este mapeamento **não está nas tabelas BQ**. Use esta referência quando o usuário fornecer um número de telefone e perguntar a região, ou quando precisar correlacionar `DDD1`/`DDD2` em `estabelecimentos` com a localização geográfica.

## Tabela completa

| DDD | UF | Região | Cidades principais |
|---|---|---|---|
| 11 | SP | Sudeste | Grande São Paulo |
| 12 | SP | Sudeste | Vale do Paraíba (São José dos Campos) |
| 13 | SP | Sudeste | Baixada Santista (Santos) |
| 14 | SP | Sudeste | Bauru, Marília |
| 15 | SP | Sudeste | Sorocaba |
| 16 | SP | Sudeste | Ribeirão Preto, São Carlos |
| 17 | SP | Sudeste | São José do Rio Preto |
| 18 | SP | Sudeste | Presidente Prudente, Araçatuba |
| 19 | SP | Sudeste | Campinas, Piracicaba |
| 21 | RJ | Sudeste | Rio de Janeiro (capital) |
| 22 | RJ | Sudeste | Campos, Cabo Frio, Macaé |
| 24 | RJ | Sudeste | Petrópolis, Volta Redonda |
| 27 | ES | Sudeste | Vitória, Vila Velha |
| 28 | ES | Sudeste | Cachoeiro de Itapemirim |
| 31 | MG | Sudeste | Belo Horizonte |
| 32 | MG | Sudeste | Juiz de Fora |
| 33 | MG | Sudeste | Governador Valadares, Teófilo Otoni |
| 34 | MG | Sudeste | Uberlândia, Uberaba |
| 35 | MG | Sudeste | Poços de Caldas, Varginha |
| 37 | MG | Sudeste | Divinópolis |
| 38 | MG | Sudeste | Montes Claros |
| 41 | PR | Sul | Curitiba |
| 42 | PR | Sul | Ponta Grossa, Guarapuava |
| 43 | PR | Sul | Londrina |
| 44 | PR | Sul | Maringá |
| 45 | PR | Sul | Cascavel, Foz do Iguaçu |
| 46 | PR | Sul | Francisco Beltrão, Pato Branco |
| 47 | SC | Sul | Joinville, Blumenau, Itajaí |
| 48 | SC | Sul | Florianópolis, Criciúma |
| 49 | SC | Sul | Chapecó, Lages |
| 51 | RS | Sul | Porto Alegre |
| 53 | RS | Sul | Pelotas, Rio Grande |
| 54 | RS | Sul | Caxias do Sul, Bento Gonçalves |
| 55 | RS | Sul | Santa Maria, Uruguaiana |
| 61 | DF/GO | Centro-Oeste | Brasília e entorno |
| 62 | GO | Centro-Oeste | Goiânia |
| 63 | TO | Norte | Palmas |
| 64 | GO | Centro-Oeste | Rio Verde, Catalão (sul de GO) |
| 65 | MT | Centro-Oeste | Cuiabá |
| 66 | MT | Centro-Oeste | Rondonópolis, Sinop |
| 67 | MS | Centro-Oeste | Campo Grande, Dourados |
| 68 | AC | Norte | Rio Branco |
| 69 | RO | Norte | Porto Velho, Ji-Paraná |
| 71 | BA | Nordeste | Salvador |
| 73 | BA | Nordeste | Ilhéus, Itabuna |
| 74 | BA | Nordeste | Juazeiro, Senhor do Bonfim |
| 75 | BA | Nordeste | Feira de Santana |
| 77 | BA | Nordeste | Vitória da Conquista, Barreiras |
| 79 | SE | Nordeste | Aracaju |
| 81 | PE | Nordeste | Recife, Olinda |
| 82 | AL | Nordeste | Maceió |
| 83 | PB | Nordeste | João Pessoa, Campina Grande |
| 84 | RN | Nordeste | Natal, Mossoró |
| 85 | CE | Nordeste | Fortaleza |
| 86 | PI | Nordeste | Teresina |
| 87 | PE | Nordeste | Petrolina, Garanhuns (interior PE) |
| 88 | CE | Nordeste | Juazeiro do Norte, Sobral (interior CE) |
| 89 | PI | Nordeste | Picos, Floriano (interior PI) |
| 91 | PA | Norte | Belém |
| 92 | AM | Norte | Manaus |
| 93 | PA | Norte | Santarém, Itaituba (oeste PA) |
| 94 | PA | Norte | **Marabá, Parauapebas** (sudeste PA) |
| 95 | RR | Norte | Boa Vista |
| 96 | AP | Norte | Macapá |
| 97 | AM | Norte | Tefé, Tabatinga (interior AM) |
| 98 | MA | Nordeste | São Luís |
| 99 | MA | Nordeste | **Imperatriz, Açailândia, Caxias** (interior MA) |

## Como usar

```sql
-- Filtrar empresas por DDD
WHERE e.DDD1 IN ('62', '64')  -- Goiás
   OR e.DDD2 IN ('62', '64')

-- Comparar telefone completo
WHERE REGEXP_REPLACE(CONCAT(IFNULL(e.DDD1,''), IFNULL(e.TELEFONE1,'')), r'\D', '')
      = '6299123456'
```

## Notas

- **Mesmo DDD pode atender mais de uma UF**: 61 cobre DF + entorno goiano. Sempre confirme com `e.UF` no JOIN.
- **Celulares têm 9 dígitos** após o DDD desde 2016 (`9XXXXXXXX`); fixos têm 8 dígitos.
- **A RFB armazena predominantemente fixos**, então o número 9 inicial pode estar ausente.
- **Discrepância DDD vs UF**: às vezes a empresa tem matriz num estado e usa DDD de outro (filial, contador, número antigo). Não descarte só por isso — investigue.
