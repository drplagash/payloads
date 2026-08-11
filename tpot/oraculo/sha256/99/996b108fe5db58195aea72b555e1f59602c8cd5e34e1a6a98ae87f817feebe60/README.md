# 🧬 Payload Analysis

`996b108fe5db58195aea72b555e1f59602c8cd5e34e1a6a98ae87f817feebe60`

## 📌 Resumen

Texto ASCII de 102 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/996b108fe5db58195aea72b555e1f59602c8cd5e34e1a6a98ae87f817feebe60.md](../../../../../malware-like/oraculo/downloader/996b108fe5db58195aea72b555e1f59602c8cd5e34e1a6a98ae87f817feebe60.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `996b108fe5db58195aea72b555e1f59602c8cd5e34e1a6a98ae87f817feebe60`
- **MD5:** `22442b14ce966dc7486315a76f377088`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 102 B |
| Entropía | 5.13 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.42.XXX | static_analysis |
| command | User-Agent: curl/7.38.0 | strings |
| hash | 996b108fe5db58195aea72b555e1f59602c8cd5e34e1a6a98ae87f817feebe60 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
