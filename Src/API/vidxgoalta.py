"""Legacy VD entry point: retained for installed Stremio configurations."""
import re
from Src.API.altadefinizione import alta_streams
from Src.Utilities.loadenv import load_env
from Src.Utilities.config import setup_logging, LEVEL
logger=setup_logging(LEVEL)

async def vidxgoalta(streams,id,client,instance_url):
    try:
        if id.startswith('tmdb:'):
            parts=id[5:].split(':')
            kind='tv' if len(parts)==3 else 'movie'
            if not all(p.isdigit() for p in parts):return streams
            response=await client.get(f'https://api.themoviedb.org/3/{kind}/{parts[0]}/external_ids',params={'api_key':load_env().get('TMDB_KEY')},timeout=20)
            if response.status_code!=200:return streams
            imdb=response.json().get('imdb_id')
            if not imdb:return streams
            id=':'.join([imdb]+parts[1:])
        if not re.fullmatch(r'tt\d+(?::\d+:\d+)?',id):return streams
        return await alta_streams(streams,id,client,instance_url)
    except Exception:
        logger.warning('AltaDefinizione: flusso non disponibile al momento')
        return streams
