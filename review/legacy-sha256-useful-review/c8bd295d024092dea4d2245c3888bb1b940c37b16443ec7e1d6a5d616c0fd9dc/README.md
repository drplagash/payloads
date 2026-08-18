# 🧬 Payload Analysis

`c8bd295d024092dea4d2245c3888bb1b940c37b16443ec7e1d6a5d616c0fd9dc`

## 📌 Resumen

Texto ASCII de 190 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c8bd295d024092dea4d2245c3888bb1b940c37b16443ec7e1d6a5d616c0fd9dc.md](../../../../../malware-like/oraculo/downloader/c8bd295d024092dea4d2245c3888bb1b940c37b16443ec7e1d6a5d616c0fd9dc.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c8bd295d024092dea4d2245c3888bb1b940c37b16443ec7e1d6a5d616c0fd9dc`
- **MD5:** `3a80a04b4eb6098bba0cd0e4bcd8eb5f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 190 B |
| Entropía | 5.29 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.19.7 NSS/3.27.1 zlib/1.2.3 libidn/1.18 libssh2/1.4.2
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.19.7 NSS/3.27.1 zlib/1.2.3 libidn/1.18 libssh2/1.4.2 | strings |
| hash | c8bd295d024092dea4d2245c3888bb1b940c37b16443ec7e1d6a5d616c0fd9dc | static_analysis |
| ip | 210.129.184.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
