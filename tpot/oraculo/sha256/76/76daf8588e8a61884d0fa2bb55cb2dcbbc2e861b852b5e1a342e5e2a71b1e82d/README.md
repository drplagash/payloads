# 🧬 Payload Analysis

`76daf8588e8a61884d0fa2bb55cb2dcbbc2e861b852b5e1a342e5e2a71b1e82d`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/76daf8588e8a61884d0fa2bb55cb2dcbbc2e861b852b5e1a342e5e2a71b1e82d.md](../../../../../malware-like/oraculo/downloader/76daf8588e8a61884d0fa2bb55cb2dcbbc2e861b852b5e1a342e5e2a71b1e82d.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `76daf8588e8a61884d0fa2bb55cb2dcbbc2e861b852b5e1a342e5e2a71b1e82d`
- **MD5:** `9b67cebb3cbc6a0b7a2e6f4d3e90a8ab`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.78 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 76daf8588e8a61884d0fa2bb55cb2dcbbc2e861b852b5e1a342e5e2a71b1e82d | static_analysis |
| ip | 8.216.7.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
