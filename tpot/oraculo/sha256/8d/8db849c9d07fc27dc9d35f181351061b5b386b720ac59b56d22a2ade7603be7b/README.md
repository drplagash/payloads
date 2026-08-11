# 🧬 Payload Analysis

`8db849c9d07fc27dc9d35f181351061b5b386b720ac59b56d22a2ade7603be7b`

## 📌 Resumen

Texto ASCII de 86 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8db849c9d07fc27dc9d35f181351061b5b386b720ac59b56d22a2ade7603be7b.md](../../../../../malware-like/oraculo/downloader/8db849c9d07fc27dc9d35f181351061b5b386b720ac59b56d22a2ade7603be7b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8db849c9d07fc27dc9d35f181351061b5b386b720ac59b56d22a2ade7603be7b`
- **MD5:** `f868cd2d36230aa55320e1fbbbb0e21a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text |
| Tamaño | 86 B |
| Entropía | 4.94 |
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
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 8db849c9d07fc27dc9d35f181351061b5b386b720ac59b56d22a2ade7603be7b | static_analysis |
| ip | 47.254.158.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
