# 🧬 Payload Analysis

`7a20df000bcf4235e48c4c606a4de49cdcc013d08ee07bddcb6c0e08b3f48dc8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7a20df000bcf4235e48c4c606a4de49cdcc013d08ee07bddcb6c0e08b3f48dc8`
- **SHA1:** `aef8290bcef86eaf58594530a747f7572575c510`
- **MD5:** `ba9bbefaef80022bd3323844689c6cc2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.79 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apk,33261DATA
/data/local/tmp/ufo.apkOKAY
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 7a20df000bcf4235e48c4c606a4de49cdcc013d08ee07bddcb6c0e08b3f48dc8 | static_analysis |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| command | /data/local/tmp/ufo.apkOKAY | strings |
| ip | 111.55.196.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
