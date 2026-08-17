# Estructura del repositorio

Objetivo: separar payloads reales, inteligencia de infraestructura, detecciones y material legacy.

Repos relacionados:
- oraculo-soc: codigo vivo, collectors, workers, systemd, DB, dashboards y operacion.
- oraculo-capturas: repo privado recomendado para capturas crudas y muestras codificadas.
- payload-analysis: analisis curado, legible y publicable.
- intel: IPs, URLs, dominios, ASN, reputacion y reportes derivados.
- diccionarios: diccionarios de credenciales y campanas. Debe ser privado.
- codebugbox-legacy: material legado, separado del flujo Oraculo.

Estructura objetivo:
- payloads/samples/<sha256>/
- intel/ips/
- intel/urls/
- intel/domains/
- detections/yara/
- detections/sigma/
- detections/suricata/
- archive/legacy-sha256-noise/
- archive/legacy-layout/

Regla principal:
Si una entrada no permite responder rapido que se vio, de donde salio, que riesgo tiene y que accion tomar, no pertenece al flujo visible.

tpot/oraculo/sha256 queda deprecado como destino de publicacion.
