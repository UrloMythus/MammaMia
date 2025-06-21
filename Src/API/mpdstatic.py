import urllib.parse
from Src.Utilities.dictionaries import STATIC_CHANNELS_DATA
# import logging # Rimosso per eliminare i log di debug
# (Assicurarsi che il logger sia configurato in run.py o qui se eseguito stand-alone)

async def get_static_channel_streams(client): # client non è usato
    """
    Recupera i canali statici definiti localmente in STATIC_CHANNELS_DATA
    senza MFP.
    """
    streams = []
    for channel_data in STATIC_CHANNELS_DATA:
        original_channel_id = channel_data.get('id')
        original_channel_title = channel_data.get('title')
        original_channel_url = channel_data.get('url')
        original_channel_logo = channel_data.get('logo')
        group_name = channel_data.get('group', "Statici")
        if not all([original_channel_id, original_channel_title, original_channel_url]):
            # logging.warning(f"MPDSTATIC: Skipping channel due to missing data: {channel_data}")
            continue

        stream_id = f"{original_channel_id}"
        stream_entry = {
            'id': stream_id,
            'title': f"{original_channel_title} (MPD)", # Titolo come in run.py
            'url': original_channel_url,
            'group': group_name, # Gruppo come in run.py
        }
        
        if original_channel_logo:
            stream_entry['logo'] = original_channel_logo
        
        streams.append(stream_entry)
    
    return streams

async def get_mpdstatic_streams_for_channel_id(channel_id_full: str, client): # client non è usato
    """
    Recupera uno stream specifico da MPD Static basato sull'ID completo.
    """
    if not channel_id_full.startswith("mpdstatic-"):
        # logging.warning(f"MPDSTATIC: channel_id_full '{channel_id_full}' does not start with 'mpdstatic-'. Returning empty list.")
        return []
    
    # Estrae la parte dell'ID del canale originale da channel_id_full
    # Esempio: se channel_id_full è "mpdstatic-sky-sport-24", original_id_part sarà "sky-sport-24"
    original_id_part = channel_id_full.replace("mpdstatic-", "")
    target_static_id_to_match = original_id_part

    all_static_streams = await get_static_channel_streams(client) # client non è usato qui
    
    for stream in all_static_streams:
        if stream['id'] == target_static_id_to_match:
            return [stream] # Restituisce una lista contenente il singolo stream trovato
    
    # logging.warning(f"MPDSTATIC: No match found for target_id '{target_static_id_to_match}'.")
    return []
