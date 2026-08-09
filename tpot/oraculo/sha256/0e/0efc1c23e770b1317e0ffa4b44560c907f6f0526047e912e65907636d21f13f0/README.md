# 🧬 Payload Analysis

`0efc1c23e770b1317e0ffa4b44560c907f6f0526047e912e65907636d21f13f0`

## 📌 Resumen

Artefacto de 188 B. Entropía registrada: 4.73. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0efc1c23e770b1317e0ffa4b44560c907f6f0526047e912e65907636d21f13f0`
- **MD5:** `12b1a8b96a6d403580d19f9df7b26f16`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 188 B |
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
| command | cd /tmp \|\| cd /var/ \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /;/bin/busybox echo -ne '\x45\x4c\x46' | strings |
| hash | 0efc1c23e770b1317e0ffa4b44560c907f6f0526047e912e65907636d21f13f0 | static_analysis |
| ip | 220.198.241.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
