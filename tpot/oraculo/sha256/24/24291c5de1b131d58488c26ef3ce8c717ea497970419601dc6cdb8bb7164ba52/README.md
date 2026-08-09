# 🧬 Payload Analysis

`24291c5de1b131d58488c26ef3ce8c717ea497970419601dc6cdb8bb7164ba52`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `24291c5de1b131d58488c26ef3ce8c717ea497970419601dc6cdb8bb7164ba52`
- **SHA1:** `b812816a9b1b7bed5026af8c3b280d3fb82448f3`
- **MD5:** `33994ee3be9003d577c09a6c4acc9b7b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 187 B |
| Entropía | 4.73 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
cd /tmp || cd /var/ || cd /var/run || cd /mnt || cd /root || cd /;/bin/busybox echo -ne '\x45\x4c\x46'
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 24291c5de1b131d58488c26ef3ce8c717ea497970419601dc6cdb8bb7164ba52 | static_analysis |
| command | cd /tmp \|\| cd /var/ \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /;/bin/busybox echo -ne '\x45\x4c\x46' | strings |
| ip | 120.85.117.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
