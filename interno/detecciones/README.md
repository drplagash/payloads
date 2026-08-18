# Detecciones

Material de detección derivado de las campañas, firmas y payloads confirmados de Oraculo SOC.

Este directorio no es decorativo. Si existe, tiene que servir para buscar patrones, explicar reglas y mostrar cómo el ruido de T-Pot se convierte en lógica defensiva.

## Acceso rápido

| Detección | Fuente | Para qué sirve |
|---|---|---|
| [Router downloader campaign](router-downloader-91-92-40.md) | `casos/tpot-router-downloader-campaign-91-92-40/` | Pivots HTTP, shell injection, downloader staging y reglas de búsqueda para 517 artefactos high-signal |
| [MIPS cad9e90 YARA](mips-cad9e90-yara.md) | `firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/` | Ubicación y uso de la regla YARA asociada al payload ELF32 MIPS confirmado |

## Qué debe vivir acá

- Pivots de búsqueda.
- Reglas o borradores YARA.
- Ideas Sigma o KQL.
- Pivots Suricata/HTTP.
- Mapeo desde campaña o firma hacia lógica defensiva.

## Qué no debe vivir acá

- Carpetas vacías.
- Hashes sin explicación.
- Basura automática sin contexto.
- Copias masivas que no ayuden a detectar nada.

## Regla humana

Cada archivo debe responder rápido:

1. qué detecta,
2. de dónde sale,
3. qué buscar,
4. cómo usarlo en SOC o threat hunting.
