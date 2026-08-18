# 🧬 Payload Analysis

`9c66f88b79ad60d6d5b63839bbb709b0cdfd591898c35ac187c3c272c47b52ae`

## 📌 Resumen

Artefacto de 6.1 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `copyright-software-19980720` en `hxxp://www[.]w3[.]org/Consortium/Legal/copyright-software-19980720`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/9c66f88b79ad60d6d5b63839bbb709b0cdfd591898c35ac187c3c272c47b52ae.md](../../../../../malware-like/oraculo/downloader/9c66f88b79ad60d6d5b63839bbb709b0cdfd591898c35ac187c3c272c47b52ae.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9c66f88b79ad60d6d5b63839bbb709b0cdfd591898c35ac187c3c272c47b52ae`
- **MD5:** `fab4aa3bc10fe3020538e90252e9b8f3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Tamaño | 6.1 KiB |
| Entropía | 5.18 |
| Strings | 100 |

## 🧠 Comportamiento observado

1. **Comunicación remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=unknown; iocs=8

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/Consortium/Legal/copyright-software-19980720 | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| url | hxxp://www[.]w3[.]org/Consortium/Legal/IPR-FAQ-20000620.html#DTD | strings |
| url | hxxp://www[.]w3[.]org/2001/06/soap-envelope | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://www[.]w3[.]org/Consortium/Legal/ | strings |
| hash | 9c66f88b79ad60d6d5b63839bbb709b0cdfd591898c35ac187c3c272c47b52ae | static_analysis |

## 🔭 Enriquecimiento histórico local

| Fuente | Detecciones | Etiquetas |
| --- | --- | --- |
| otx | 0 | austinsonger, austinsonger, trojan, jhasenbusch, sandbox, cmdlets, snort, getcommand |
| circl_hashlookup | 0 | snap-hashlookup-import/lib/python3.12/site-packages/onvif/wsdl/envelope |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
