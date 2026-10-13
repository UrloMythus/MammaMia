# MammaMia TV Proxy

Questo fork aggiunge il percorso HLS tramite proxy che ha risolto il timer fermo a `00:00` e il seek su un Samsung QE65Q70TCTXZT con Stremio Theater 1.12.1. Il risultato su altri dispositivi va verificato.

## Avvio con Docker Compose

Prerequisiti: Docker con Compose, una propria API key TMDB e un proxy HLS compatibile con l'endpoint `/proxy/hls/manifest.m3u8` (testato con EasyProxy 2.5.0). Il proxy deve riscrivere playlist, segmenti, tracce audio e chiavi; deve essere raggiungibile dalla TV. Il Compose avvia MammaMia; EasyProxy è una dipendenza esterna e non è incluso in questa repository.

```bash
git clone https://github.com/dllfpp/MammaMia.git
cd MammaMia
cp .env.example .env
```

Modifica `.env` con la tua API key e l'indirizzo del proxy sulla tua rete, per esempio `http://IP_DEL_SERVER:7860`. Non usare `localhost` o un nome di servizio Docker: l'URL viene inviato direttamente alla TV.

```bash
docker compose up -d --build
```

Apri `http://IP_DEL_SERVER:8080/configure` per la configurazione originale dell'addon. Per usare il percorso TV Proxy, installa il manifest `http://IP_DEL_SERVER:8080/fFNDfFNDX01GUHw%3D/manifest.json` in Stremio (questa configurazione seleziona StreamingCommunity e SC_MFP senza credenziali MediaFlow). Seleziona **MammaMia TV Proxy** tra le sorgenti.

## Comportamento

### Test diretto con VLC su iPhone

Per isolare un problema nel passaggio del link da Stremio a VLC, apri in VLC un URL breve del server: `https://IL_TUO_DOMINIO/vlc/series/tt0413573:22:15.m3u8` (Grey's Anatomy S22E15), oppure `/vlc/movie/tt0816692.m3u8` per un film. Per la LAN puoi usare `http://IP_DEL_SERVER:8080` come base. L'endpoint recupera un flusso TV Proxy aggiornato e risponde con un redirect non memorizzabile. Richiede HLS_PROXY_URL e un proxy raggiungibile dall'iPhone. Non è una conferma di compatibilità con ogni versione di VLC.

- `HLS_PROXY_URL` in ambiente ha priorità su `General.HLS_PROXY_URL` in `config.json`.
- Con SC_MFP attivo, senza URL MediaFlow e con HLS_PROXY_URL impostato, viene mostrato soltanto il flusso TV Proxy di Vixcloud. Gli altri provider restano invariati.
- Senza HLS_PROXY_URL resta disponibile il comportamento diretto originale.
- Se sono fornite credenziali MediaFlow, resta attivo il percorso MediaFlow originale.

## Credenziali e configurazione

La repository usa la configurazione pubblica originale, senza configurazione o credenziali del server personale. `.env` è escluso da Git e dal contesto di build Docker. Le credenziali vengono passate solo all'avvio del container.

Per personalizzare i siti senza modificare il file pubblico, copia `config.json` in `config.local.json` (ignorato da Git) e modifica il mount del Compose in `./config.local.json:/app/config.json:ro`.

Il pacchetto è pensato per la rete locale. Il proxy deve avere le proprie impostazioni di accesso compatibili con gli URL generati; questa integrazione non aggiunge credenziali al proxy.

Licenza MIT e attribuzione al progetto originale: vedere [LICENSE](LICENSE) e [README.md](README.md).
