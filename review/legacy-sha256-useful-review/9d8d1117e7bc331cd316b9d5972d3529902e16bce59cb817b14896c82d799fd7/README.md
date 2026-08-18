# 🧬 Payload Analysis

`9d8d1117e7bc331cd316b9d5972d3529902e16bce59cb817b14896c82d799fd7`

## 📌 Resumen

Artefacto de 1.1 KiB. Formato identificado como ASCII text, with very long lines (1044), with CRLF line terminators. Entropía registrada: 5.74. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9d8d1117e7bc331cd316b9d5972d3529902e16bce59cb817b14896c82d799fd7`
- **MD5:** `9e36cb00d909c69c2dfb10d340d0a781`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (1044), with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.74 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (1044), with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
config set dir /var/spool/cron/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 8.219.145.XXX | static_analysis |
| command | config set dir /var/spool/cron/ | strings |
| hash | 9d8d1117e7bc331cd316b9d5972d3529902e16bce59cb817b14896c82d799fd7 | static_analysis |
| ip | 124.236.108.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
