# 🧬 Payload Analysis

`7d1169fcd87242c712407401bff3e7a7b90547e5a6532e535f7e60b839411372`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como Compiled PSI (v2) data (\234\350q>2\271\374\005'*frR\350|\007). Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:36:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7d1169fcd87242c712407401bff3e7a7b90547e5a6532e535f7e60b839411372`
- **SHA1:** `f5b95e48b5804d246efed2c8658a3f9acf4ddeaa`
- **MD5:** `7ff1b70f9c4018b8cad07d0568b1a5cd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Compiled PSI (v2) data (\234\350q>2\271\374\005'*frR\350\|\007) |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Compiled PSI (v2) data (\234\350q>2\271\374\005'*frR\350|\007); high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 7d1169fcd87242c712407401bff3e7a7b90547e5a6532e535f7e60b839411372 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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
