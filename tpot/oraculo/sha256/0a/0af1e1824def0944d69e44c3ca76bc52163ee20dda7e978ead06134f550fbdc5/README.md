# 🧬 Payload Analysis

`0af1e1824def0944d69e44c3ca76bc52163ee20dda7e978ead06134f550fbdc5`

## 📌 Resumen

Script Bash de 2.3 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `$1` en `hxxps://217.60.195.XXX/test/$1`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01.000000Z`
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
| url | hxxps://217.60.195.XXX/test/$1 | static_analysis |
| ip | 217.60.195.XXX | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
