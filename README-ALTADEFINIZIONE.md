# AltaDefinizione in MammaMia

MammaMia displays the provider in each stream's name and description, including
AltaDefinizione, StreamingCommunity and the other selected providers. Quality is
shown when the HLS master declares it. An undeclared audio language is displayed
as unknown rather than assumed to be Italian.

## Configuration

Select **AltaDefinizione (Vidxgo)** on `/configure`. New configurations use `AD`;
existing `VD` configurations remain supported. Existing StreamingCommunity
configurations also include AltaDefinizione without reinstalling the addon.
Unchecking AltaDefinizione writes `AD_OFF` to explicitly disable this default.
The server's `Siti.Vidxgo.enabled` setting must be `"1"`.

The existing Vidxgo host setting is retained. `ALTADEFINIZIONE_URL` can override
the referring website; its default is `https://altadefinizionex.life`.
IMDb movie and episode IDs are supported. TMDB movie and TV IDs are translated
using the instance's existing TMDB key.

## Playback

AltaDefinizione streams use stable `/alta/...` URLs served by MammaMia itself.
The relay rewrites master playlists, media playlists, audio tracks, initialization
segments and key URIs. It preserves segment-specific query parameters and byte
ranges while renewing the signed `t`/`e` parameters. Signatures are renewed ahead
of expiry, and once immediately after an HTTP 401/403. This keeps the playback URL
stable when seeking or watching beyond the original signature's lifetime.

Clients must reach the MammaMia instance during playback; all AltaDefinizione HLS
data goes through that instance. No extra MediaFlow or EasyProxy configuration is
required for this provider. StreamingCommunity's existing proxy/VLC path remains
available. Provider sessions are cached in memory (up to 256); relay URLs can
resolve again after a restart.

Resources are restricted to the resolved title's HLS directory. Requests cannot
provide an arbitrary upstream host. External resources outside that directory
are rejected instead of being proxied. Provider availability and undeclared
metadata remain dependent on the upstream service.

The Docker image uses Python 3.12 and `httpx==0.28.1`, matching the HTTP transport
validated for the download service. To run regression tests in the built image:

```sh
docker run --rm --entrypoint sh mammamia:tv-proxy \
  -c 'PYTHONPATH=/app python tests/test_altadefinizione.py'
```

Tests cover provider labels, legacy configuration, explicit opt-out, playlist
rewriting, resource scope, expired signatures, byte ranges and the existing VLC
handoff URL. Live playback still depends on the specific Stremio client/device.
