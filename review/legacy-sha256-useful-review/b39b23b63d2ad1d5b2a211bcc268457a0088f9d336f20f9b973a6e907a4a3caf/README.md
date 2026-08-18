# 🧬 Payload Analysis

`b39b23b63d2ad1d5b2a211bcc268457a0088f9d336f20f9b973a6e907a4a3caf`

## 📌 Resumen

Texto ASCII de 140 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b39b23b63d2ad1d5b2a211bcc268457a0088f9d336f20f9b973a6e907a4a3caf.md](../../../../../malware-like/oraculo/downloader/b39b23b63d2ad1d5b2a211bcc268457a0088f9d336f20f9b973a6e907a4a3caf.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b39b23b63d2ad1d5b2a211bcc268457a0088f9d336f20f9b973a6e907a4a3caf`
- **MD5:** `406f477141c661e343ba196997ad7810`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 140 B |
| Entropía | 5.17 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
GET /admin/modules//framework/amp_conf/var/www/html/admin/config.php HTTP/1.1
User-Agent: curl/8.5.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| command | GET /admin/modules//framework/amp_conf/var/www/html/admin/config.php HTTP/1.1 | strings |
| command | User-Agent: curl/8.5.0 | strings |
| hash | b39b23b63d2ad1d5b2a211bcc268457a0088f9d336f20f9b973a6e907a4a3caf | static_analysis |
| ip | 51.75.255.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
