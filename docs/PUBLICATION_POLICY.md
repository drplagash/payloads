# Politica de publicacion

Nivel A: payload real.
Va a payloads/samples/<sha256>/ si tiene raw, analysis, evidence, yara, comando observado, source_url, filename real, arquitectura, familia probable o deteccion asociada.

Nivel B: indicador util.
Va a intel/ si es IP, URL, dominio, ASN o reputacion sin muestra materializada.

Nivel C: ruido.
Va a archive/legacy-sha256-noise/ o se elimina tras revision si:
- artifact.description = data
- risk_level = info
- evidence_score < 20
- no tiene raw
- no tiene analysis
- no tiene evidence
- no tiene yara
- no tiene filename real
- no tiene source_url real
- no tiene comando observado
- solo contiene hash mas IP redactada

Una IP no es un payload. Una URL no es un payload. Un ASN no es un payload. Son infraestructura.
