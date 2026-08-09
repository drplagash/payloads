# 🧬 Payload Analysis

`35d172732e5f4107b719f6dd16ba3e5311c0d3ed39ad7b7ce202a4272c8c2b51`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `35d172732e5f4107b719f6dd16ba3e5311c0d3ed39ad7b7ce202a4272c8c2b51`
- **MD5:** `8c2e356fa7b409c9d07c72db1119c3a8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.3 KiB |
| Entropía | 6.61 |
| Strings | 27 |

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
| hash | 35d172732e5f4107b719f6dd16ba3e5311c0d3ed39ad7b7ce202a4272c8c2b51 | static_analysis |
| command | shell:rm -rf /data/local/tmp/* | strings |
| ip | 49.91.39.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
