# 🧬 Payload Analysis

`47156487b744e961d626fb4a70644f551ce7e04a21bba91c93afd66a9a58562e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asociaron 3 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `47156487b744e961d626fb4a70644f551ce7e04a21bba91c93afd66a9a58562e`
- **SHA1:** `a00ccead9587228af4a45c90987978cb9597f7fa`
- **MD5:** `cc13a130971ded424bf1a3642a938ca7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 671 B |
| Entropía | 5.11 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /ubuntu/pool/main/c/curl/curl_8.5.0-2ubuntu10.11_amd64.deb HTTP/1.1
GET /ubuntu/pool/main/c/curl/libcurl3t64-gnutls_8.5.0-2ubuntu10.11_amd64.deb HTTP/1.1
GET /ubuntu/pool/main/c/curl/libcurl4t64_8.5.0-2ubuntu10.11_amd64.deb HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 47156487b744e961d626fb4a70644f551ce7e04a21bba91c93afd66a9a58562e | static_analysis |
| command | GET /ubuntu/pool/main/c/curl/curl_8.5.0-2ubuntu10.11_amd64.deb HTTP/1.1 | strings |
| command | GET /ubuntu/pool/main/c/curl/libcurl3t64-gnutls_8.5.0-2ubuntu10.11_amd64.deb HTTP/1.1 | strings |
| command | GET /ubuntu/pool/main/c/curl/libcurl4t64_8.5.0-2ubuntu10.11_amd64.deb HTTP/1.1 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
