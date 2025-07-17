# MammaMia
A Stremio Addon for HTTPS Streams in Italian. Movies, Series, Anime and Live TV are supported.

---

# Configurazione
Tutta la configurazione avviene tramite **variabili d'ambiente**. Puoi:
- Usare un file `.env` (solo in locale o se montato/copiato nel container)
- Impostare le variabili direttamente nel sistema, in Docker Compose (`environment:`), o nell'interfaccia Portainer

## Esempio di file `.env`
Guarda `example.env` per un esempio completo di tutte le variabili supportate.

## Esempio di docker-compose.yml
```yaml
version: '3.8'
services:
  mammamia:
    build: .
    container_name: mammamia
    ports:
      - "8080:8080"
    # Opzionale: usa environment: se vuoi passare le variabili direttamente
    # environment:
    #   - SC_DOMAIN=https://streamingunity.bio
    #   - PORT=8080
```

## In Portainer
- Puoi impostare tutte le variabili d'ambiente nella sezione "Environment variables" dello stack/container.
- Non serve il file `.env` se imposti tutto da Portainer.

## Avvio locale
1. Installa le dipendenze:
   ```sh
   pip install -r requirements.txt
   ```
2. Crea un file `.env` (puoi copiare `example.env`) e personalizza le variabili.
3. Avvia il server:
   ```sh
   python3 run.py
   ```

## Avvio con Docker Compose
```sh
docker compose up --build
```

---

# Note tecniche
- Se usi solo variabili d'ambiente di sistema, **puoi rimuovere o commentare** la riga `load_dotenv()` dal codice.
- Se usi `.env`, assicurati che sia in UTF-8 e solo con caratteri ASCII per massima compatibilità.
- Le variabili non impostate useranno i valori di default definiti in `config.py`.

---

# Variabili d'ambiente principali
| Variabile         | Descrizione                                 |
|------------------|---------------------------------------------|
| SC_DOMAIN        | URL di StreamingCommunity                    |
| FT_DOMAIN        | URL di Filmpertutti                          |
| ...              | ... (vedi example.env per tutte)             |
| TMDB_KEY         | API Key di TheMovieDB                        |
| FORWARDPROXY     | (opzionale) Proxy per siti con Cloudflare    |
| PROXY            | (opzionale) Lista proxy per Cloudflare       |
| PORT             | Porta su cui avviare il server (default 8080)|

---

# Per problemi con Docker/Portainer
- Se usi solo variabili d'ambiente di sistema, non serve `.env`.
- Se vuoi usare `.env`, assicurati che sia montato o copiato nel container.
- In caso di errori di codifica, usa solo caratteri ASCII nel `.env`.

---

Per dettagli sulle variabili e la configurazione, consulta anche `example.env`.


