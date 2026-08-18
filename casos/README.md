# Casos

Casos humanos de análisis de payloads, malware y campañas observadas con T-Pot.

Un caso no es una carpeta con un hash. Un caso es una historia técnica: qué se vio, por qué importa, qué evidencia existe, qué patrones aparecen y qué detección se puede construir.

## Casos principales

| Caso | Qué muestra |
|---|---|
| [`tpot-router-downloader-campaign-91-92-40`](tpot-router-downloader-campaign-91-92-40/) | Campaña router/IoT downloader agrupada desde 517 firmas high-signal. Incluye superficies HNAP, JNAP, Netgear setup.cgi, ping_test, syscmd.htm, ttcp_ip y weblogin.cgi. |

## Firmas relacionadas

Las firmas/payloads individuales viven en:

- [`../firmas/`](../firmas/)

El payload MIPS `cad9e90...` está documentado como firma confirmada, no como campaña.
