# 🧬 Payload Analysis

`0af1e1824def0944d69e44c3ca76bc52163ee20dda7e978ead06134f550fbdc5`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0af1e1824def0944d69e44c3ca76bc52163ee20dda7e978ead06134f550fbdc5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Bourne-Again shell script, ASCII text executable |
| MIME | text/x-shellscript |
| Tamaño | 2.3 KiB |
| Entropía | 5.25 |
| Strings | 81 |
| Strings sospechosas | 12 |
| URLs extraídas | 2 |
| Dominios extraídos | 1 |
| IPs extraídas | 1 |
| Comandos extraídos | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: file_type=script; mime=text/x-shellscript; magic=Bourne-Again shell script, ASCII text executable; embedded_urls=2; embedded_ips=1; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 217.60.195.XXX | static_analysis |
| url | hxxps://217.60.195.XXX/test/$1 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
