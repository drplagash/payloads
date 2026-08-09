# 🧬 Payload Analysis

`84f93536dadce4fa0f4f811b5f2cb80c1016a7dec0cd3d1c76e011cb7c58e022`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `84f93536dadce4fa0f4f811b5f2cb80c1016a7dec0cd3d1c76e011cb7c58e022`
- **SHA1:** `39ea5278230f8ad00f7b45f6e589114eb40f2da4`
- **MD5:** `1a9124978f0676fe5b743cfb4fd3e500`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 161 B |
| Entropía | 5.08 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🖥️ Comandos observados / extraídos

```text
GET /ubuntu/pool/main/c/curl/curl_8.5.0-2ubuntu10.10_amd64.deb HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 84f93536dadce4fa0f4f811b5f2cb80c1016a7dec0cd3d1c76e011cb7c58e022 | static_analysis |
| command | GET /ubuntu/pool/main/c/curl/curl_8.5.0-2ubuntu10.10_amd64.deb HTTP/1.1 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
