# 🧬 Payload Analysis

`25b3a3f5f06ff8260039bcdc1c5c1d76164f09a7b6c82b3f110c00be1992e99c`

## 📌 Resumen

Artefacto de 3.4 KiB. Entropía registrada: 6.64. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `25b3a3f5f06ff8260039bcdc1c5c1d76164f09a7b6c82b3f110c00be1992e99c`
- **SHA1:** `b6a8cb6576950a27eea38220de1e74d521217453`
- **MD5:** `56e9d8f5cc337d82796d6a043531bfa0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.4 KiB |
| Entropía | 6.64 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
shell:rm -rf /data/local/tmp/*
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | shell:rm -rf /data/local/tmp/* | strings |
| hash | 25b3a3f5f06ff8260039bcdc1c5c1d76164f09a7b6c82b3f110c00be1992e99c | static_analysis |
| ip | 173.198.143.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
