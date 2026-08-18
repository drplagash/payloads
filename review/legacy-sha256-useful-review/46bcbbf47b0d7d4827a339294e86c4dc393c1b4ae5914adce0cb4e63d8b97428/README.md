# 🧬 Payload Analysis

`46bcbbf47b0d7d4827a339294e86c4dc393c1b4ae5914adce0cb4e63d8b97428`

## 📌 Resumen

Artefacto de 4.0 KiB. Presenta entropía elevada (7.28), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `46bcbbf47b0d7d4827a339294e86c4dc393c1b4ae5914adce0cb4e63d8b97428`
- **SHA1:** `cdb3bb63aa50febc46091700ec78c2167105d73a`
- **MD5:** `208102547e8772d598323a8dfdcc8d6b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.28 |
| Strings | 20 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.3; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 46bcbbf47b0d7d4827a339294e86c4dc393c1b4ae5914adce0cb4e63d8b97428 | static_analysis |
| ip | 59.46.62.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
