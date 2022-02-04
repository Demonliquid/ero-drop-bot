# ero-drop-bot

DONE:
1- Se inicia desde scrape-bscan: va a generar csv con los holders de token y las colecciones de NFT.
2- Sigue rarity_lookup: Le asigna una lista de item_ids a los usuarios con Collection 1 y 2
?-  
4- Accountant: Une y limpia las tablas

TODO:
3- Dividir la columna item_ids en rarity
5- Calcular los multipliers de multipliers.py sobre la tabla completa.
Ultimo_paso - adaptar web3 para interactuar con un contrato

PROBLEMAS:

- No coincide exactamente lo de la pantalla de Bscscan con lo que llega en la API.
- Bscscan no muestra mas de 1000 holders.
- Bscscan tiene proteccion a la hora de scrapear.
- La api devuelve la lista de transacciones de NFT, no la cantidad de NFT que tiene la cuenta.
  - Es facil calcular:
    - Un numero par de movimientos significa que lo vendio.
    - Un numero impar de movimientos significa que lo holdea.
  - PERO me encontre un caso de un usuario con 2 OUT seguidos hacia su propia cuenta sin IN. Podria haber quedado fuera del conteo.
