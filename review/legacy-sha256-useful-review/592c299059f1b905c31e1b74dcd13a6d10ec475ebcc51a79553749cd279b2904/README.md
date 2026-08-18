# 🧬 Payload Analysis

`592c299059f1b905c31e1b74dcd13a6d10ec475ebcc51a79553749cd279b2904`

## 📌 Resumen

Texto ASCII de 204 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/592c299059f1b905c31e1b74dcd13a6d10ec475ebcc51a79553749cd279b2904.md](../../../../../malware-like/oraculo/downloader/592c299059f1b905c31e1b74dcd13a6d10ec475ebcc51a79553749cd279b2904.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `592c299059f1b905c31e1b74dcd13a6d10ec475ebcc51a79553749cd279b2904`
- **MD5:** `9d2d45be50cd1e2a56ab9adb02b8a6ac`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 204 B |
| Entropía | 5.12 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
User-Agent: Wget/1.25.0 (linux-gnu)
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.42.XXX | static_analysis |
| command | User-Agent: Wget/1.25.0 (linux-gnu) | strings |
| command | User-Agent: curl/7.38.0 | strings |
| hash | 592c299059f1b905c31e1b74dcd13a6d10ec475ebcc51a79553749cd279b2904 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
