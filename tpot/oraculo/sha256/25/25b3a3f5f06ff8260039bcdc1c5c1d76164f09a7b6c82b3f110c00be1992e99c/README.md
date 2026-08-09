# 🧬 Payload Analysis

`25b3a3f5f06ff8260039bcdc1c5c1d76164f09a7b6c82b3f110c00be1992e99c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:38+00:00`
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
| hash | 25b3a3f5f06ff8260039bcdc1c5c1d76164f09a7b6c82b3f110c00be1992e99c | static_analysis |
| command | shell:rm -rf /data/local/tmp/* | strings |
| ip | 173.198.143.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
