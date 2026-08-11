# 🧬 Payload Analysis

`c54b20781fd9897b359facc3555e73112c0baefc93272b5a1e57b3cf52c1dec6`

## 📌 Resumen

Texto ASCII de 695 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c54b20781fd9897b359facc3555e73112c0baefc93272b5a1e57b3cf52c1dec6.md](../../../../../malware-like/oraculo/downloader/c54b20781fd9897b359facc3555e73112c0baefc93272b5a1e57b3cf52c1dec6.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c54b20781fd9897b359facc3555e73112c0baefc93272b5a1e57b3cf52c1dec6`
- **MD5:** `51eef6363b2e9486e1a055184abdf357`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 695 B |
| Entropía | 5.12 |
| Strings | 30 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
GET /wget.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 31.56.209.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /wget.sh HTTP/1.1 | strings |
| hash | c54b20781fd9897b359facc3555e73112c0baefc93272b5a1e57b3cf52c1dec6 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
