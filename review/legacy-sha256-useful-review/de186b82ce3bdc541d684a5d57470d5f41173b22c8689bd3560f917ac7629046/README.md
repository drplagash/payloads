# 🧬 Payload Analysis

`de186b82ce3bdc541d684a5d57470d5f41173b22c8689bd3560f917ac7629046`

## 📌 Resumen

Texto ASCII de 82 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/de186b82ce3bdc541d684a5d57470d5f41173b22c8689bd3560f917ac7629046.md](../../../../../malware-like/oraculo/downloader/de186b82ce3bdc541d684a5d57470d5f41173b22c8689bd3560f917ac7629046.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:12:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `de186b82ce3bdc541d684a5d57470d5f41173b22c8689bd3560f917ac7629046`
- **SHA1:** `3f935c0e703d6bdb17f3d49bad0cf49246105080`
- **MD5:** `45383ab1e94cb2467e4f4efac8de8d2b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.85 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | de186b82ce3bdc541d684a5d57470d5f41173b22c8689bd3560f917ac7629046 | static_analysis |
| ip | 47.250.93.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
