# Plan y Checklist de Traducción: Optimización 3D

Plan de trabajo detallado y lista de verificación interactiva para traducir la sección de **Optimización 3D** (`tutorials/3d/index.html#optimization`) de la documentación oficial de Godot al español.

---

## 📂 Resumen de Archivos a Traducir

Cada tema consta de dos archivos sincronizados:
1. **Archivo HTML compilado**: `tutorials/3d/<nombre>.html`
2. **Archivo fuente RST**: `_sources/tutorials/3d/<nombre>.rst.txt`
3. **Índice principal y barras laterales**:
   - `tutorials/3d/index.html`
   - `_sources/tutorials/3d/index.rst.txt`
   - Menús de navegación lateral (toctree) en las páginas relacionadas

---

## 📋 Checklist Detallado por Tema y Subsecciones

### 1. Uso de MultiMeshInstance3D (`using_multi_mesh_instance`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/using_multi_mesh_instance.html`
  - `_sources/tutorials/3d/using_multi_mesh_instance.rst.txt`
- [x] **Título principal:**
  - [x] *Using MultiMeshInstance3D* -> *Uso de MultiMeshInstance3D*
- [x] **Subsecciones a traducir:**
  - [x] **Introduction** (*Introducción*)
    - Explicación del caso de uso frente a `MeshInstance3D` duplicados.
  - [x] **Setting up the nodes** (*Configuración de los nodos*)
    - Configuración con nodo de superficie objetivo (`target`) y nodo origen (`source`).
    - Flujo del editor: botón `MultiMesh` -> `Populate surface` (*Poblar superficie*).
  - [x] **MultiMesh settings** (*Ajustes de MultiMesh*)
    - [x] **Target Surface** (*Superficie objetivo*)
    - [x] **Source Mesh** (*Malla de origen*)
    - [x] **Mesh Up Axis** (*Eje superior de la malla*)
    - [x] **Random Rotation** (*Rotación aleatoria*)
    - [x] **Random Tilt** (*Inclinación aleatoria*)
    - [x] **Random Scale** (*Escala aleatoria*)
    - [x] **Scale** (*Escala*)
    - [x] **Amount** (*Cantidad*)

---

### 2. Nivel de detalle de malla (LOD) (`mesh_lod`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/mesh_lod.html`
  - `_sources/tutorials/3d/mesh_lod.rst.txt`
- [x] **Título principal:**
  - [x] *Mesh level of detail (LOD)* -> *Nivel de detalle de malla (LOD)*
- [x] **Subsecciones a traducir:**
  - [x] **Introduction** (*Introducción*)
    - Historia del LOD manual vs. generación automática en importación.
    - Integración con la librería `meshoptimizer`.
    - Nodos compatibles (`MeshInstance3D`, `MultiMeshInstance3D`, partículas GPU/CPU).
  - [x] **Visual comparison** (*Comparación visual*)
    - Vistas sombreadas y en modo malla alámbrica (*wireframe*).
  - [x] **Generating mesh LOD** (*Generación de LOD de malla*)
    - Comportamiento por defecto en escenas 3D (glTF, .blend, FBX).
    - Configuración especial para archivos OBJ (*Import As -> Scene*).
    - Desactivación de LOD para mallas problemáticas en el dock Import.
  - [x] **Comparing mesh LOD visuals and performance** (*Comparación visual y de rendimiento de LOD de malla*)
    - Modos de depuración en el visor 3D (*Disable Mesh LOD*, *Display Wireframe*).
    - Medición con *View Frame Time* y *View Information* (primitivas y FPS).
  - [x] **Configuring mesh LOD performance and quality** (*Configuración del rendimiento y calidad de LOD de malla*)
    - Ajuste de proyecto: `Rendering > Mesh LOD > LOD Change > Threshold Pixels`.
    - Ajuste en tiempo de ejecución: `mesh_lod_threshold` en el Viewport (GDScript y C#).
    - Propiedad `LOD Bias` en nodos `GeometryInstance3D`.
    - Ajuste de `Mesh LOD Threshold` en `ReflectionProbe`.
  - [x] **Using mesh LOD with MultiMesh and particles** (*Uso de LOD de malla con MultiMesh y partículas*)
    - Selección de LOD basada en AABB de nodo hacia la cámara.
    - Generación de AABB en `GPUParticles3D`.
    - Separación de instancias lejanas en múltiples nodos `MultiMeshInstance3D`.

---

### 3. Rangos de visibilidad (HLOD) (`visibility_ranges`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/visibility_ranges.html`
  - `_sources/tutorials/3d/visibility_ranges.rst.txt`
- [x] **Título principal:**
  - [x] *Visibility ranges (HLOD)* -> *Rangos de visibilidad (HLOD)*
- [x] **Subsecciones a traducir:**
  - [x] **How it works** (*Cómo funciona*)
    - Compatibilidad con derivados de `GeometryInstance3D` y cambio de tipo de nodo según distancia.
    - Concepto de HLOD (*Hierarchical Level of Detail*) para reducir *draw calls*.
    - Desvanecimiento total para reducir saturación visual (`Label3D`, etc.).
  - [x] **Setting up visibility range** (*Configuración del rango de visibilidad*)
    - Guía paso a paso: esfera cercana y caja lejana con margen de histéresis.
  - [x] **Visibility range properties** (*Propiedades del rango de visibilidad*)
    - Parámetros: `Begin`, `Begin Margin`, `End`, `End Margin`, `Fade Mode`.
    - [x] **Fade mode** (*Modo de desvanecimiento*)
      - Modos: `Disabled` (histéresis inmediata), `Self` (desvanecimiento propio con alfa), `Dependencies` (desvanecimiento de dependencias).
    - [x] **Visibility parent** (*Padre de visibilidad*)
      - Jerarquía de visibilidad HLOD (ejemplo de lote de casas).
      - Manejo de ciclos y comportamiento con la propiedad `visible`.
  - [x] **Configuration tips** (*Consejos de configuración*)
    - [x] **Use simpler materials at a distance to improve performance** (*Usar materiales más simples a la distancia para mejorar el rendimiento*)
      - Desactivación de características costosas (Normal Map, Rim, Subsurface Scattering, Refraction, etc.).
    - [x] **Use dithering for LOD transitions** (*Usar tramado (dithering) para transiciones de LOD*)
      - Ventajas sobre alpha blending (mayor rendimiento, sin problemas de orden de transparencia).
      - Configuración con `BaseMaterial3D > Distance Fade -> Object Dither`.

---

### 4. Eliminación de oclusión (`occlusion_culling`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/occlusion_culling.html`
  - `_sources/tutorials/3d/occlusion_culling.rst.txt`
- [x] **Título principal:**
  - [x] *Occlusion culling* -> *Eliminación de oclusión*
- [x] **Subsecciones a traducir:**
  - [x] **Why use occlusion culling** (*Por qué usar eliminación de oclusión*)
    - Escenarios interiores vs. exteriores.
    - Comparación Forward+ (depth prepass) vs. Mobile (alto beneficio por sobregiro/overdraw).
  - [x] **How occlusion culling works in Godot** (*Cómo funciona la eliminación de oclusión en Godot*)
    - Rasterizado por CPU en búfer de baja resolución mediante la biblioteca `Embree`.
    - Concepto de oclusor (*occluder*) y objeto ocluido (*occludee*).
    - Prueba del AABB del objeto ocluido.
  - [x] **Setting up occlusion culling** (*Configuración de la eliminación de oclusión*)
    - Ajuste de proyecto: `Rendering > Occlusion Culling > Use Occlusion Culling`.
    - [x] **Automatically baking occluders (recommended)** (*Horneado automático de oclusores (recomendado)*)
      - Nodo `OccluderInstance3D` y botón **Bake Occluders**.
      - Filtrado de objetos dinámicos mediante `Bake > Cull Mask` y capas de `VisualInstance3D`.
    - [x] **Manually placing occluders** (*Colocación manual de oclusores*)
      - Tipos: `QuadOccluder3D`, `BoxOccluder3D`, `SphereOccluder3D`, `PolygonOccluder3D`, `ArrayOccluder3D`.
  - [x] **Previewing occlusion culling** (*Vista previa de la eliminación de oclusión*)
    - Modo de depuración: `Display Advanced... > Occlusion Culling Buffer`.
    - Estadísticas con `View Information` y `View Frame Time`.
    - Control por código: `use_occlusion_culling` en Viewport (GDScript y C#).
  - [x] **Performance considerations** (*Consideraciones de rendimiento*)
    - [x] **Design your levels to take advantage of occlusion culling** (*Diseña tus niveles para aprovechar la eliminación de oclusión*)
    - [x] **Avoid moving OccluderInstance3D nodes during gameplay** (*Evita mover nodos OccluderInstance3D durante el juego*)
    - [x] **Use the simplest possible occluder shapes** (*Usa las formas de oclusor más simples posibles*)
      - Propiedades `Bake > Simplification`, `BVH Build Quality`, `Occlusion Rays Per Thread`.
  - [x] **Troubleshooting** (*Resolución de problemas*)
    - [x] **My occludee isn't being culled when it should be** (*Mi objeto no se ocluye cuando debería*)
      - Verificación de Cull Mask, materiales opacos vs. transparentes, AABB y margen de corte.
    - [x] **My occludee is being culled when it shouldn't be** (*Mi objeto se ocluye cuando no debería*)
      - Objetos movidos tras hornear, oclusores dinámicos no deseados, simplificación excesiva.

---

### 5. Escalado de resolución (`resolution_scaling`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/resolution_scaling.html`
  - `_sources/tutorials/3d/resolution_scaling.rst.txt`
- [x] **Título principal:**
  - [x] *Resolution scaling* -> *Escalado de resolución*
- [x] **Subsecciones a traducir:**
  - [x] **Why use resolution scaling?** (*¿Por qué usar escalado de resolución?*)
    - Impacto en cuellos de botella de GPU y dispositivos móviles.
  - [x] **Resolution scaling options** (*Opciones de escalado de resolución*)
    - [x] **Scaling mode** (*Modo de escalado*)
      - Comparación entre `Bilinear`, `FSR 1.0` (AMD FidelityFX) y `FSR 2.2`.
      - Interacción con técnicas de antialiasing (TAA, MSAA, FXAA).
    - [x] **Rendering scale** (*Escala de renderizado*)
      - Ajuste `Rendering > Scaling 3D > Scale` y `scaling_3d_scale` en `Viewport`.
      - Supermuestreo (SSAA) con valores mayores a 1.0.
      - Tablas completas de resoluciones (1080p, 1440p, 4K) y cálculo de megapíxeles por cuadro.
    - [x] **FSR Sharpness** (*Nitidez FSR*)
      - Inversión de valores (0.0 más nítido, 2.0 menos nítido). Trucos para resolución nativa.
    - [x] **Mipmap bias** (*Sesgo de mipmap*)
      - Preservación de detalle de texturas con valores negativos.
      - Ajuste `Texture Mipmap Bias` y compensación para TAA y FXAA.
  - [x] **Troubleshooting** (*Resolución de problemas*)
    - [x] **Performance does not increase much when decreasing resolution scale** (*El rendimiento no aumenta mucho al disminuir la escala de resolución*)
      - Detección de cuellos de botella en CPU (*draw calls*) o efectos de postproceso intensivos.

---

### 6. Sombreado de tasa variable (`variable_rate_shading`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/variable_rate_shading.html`
  - `_sources/tutorials/3d/variable_rate_shading.rst.txt`
- [x] **Título principal:**
  - [x] *Variable rate shading* -> *Sombreado de tasa variable (VRS)*
- [x] **Subsecciones a traducir:**
  - [x] **What is variable rate shading?** (*¿Qué es el sombreado de tasa variable?*)
    - Reducción del costo de sombreado por fragmento preservando la geometría.
    - Aplicación en Realidad Virtual (VR) para *foveated rendering* (renderizado foveado).
  - [x] **Hardware support** (*Soporte de hardware*)
    - Compatibilidad en GPUs de escritorio (NVIDIA Turing+, AMD RDNA2+, Intel Arc).
    - Compatibilidad móvil (Snapdragon 888+, Dimensity 9000+, Mali-G615+).
  - [x] **Using variable rate shading in Godot** (*Uso del sombreado de tasa variable en Godot*)
    - Ajustes en `Rendering > VRS`: `Mode` (Disabled, Texture, XR) y `Texture`.
    - Renderizadores compatibles (Forward+, Mobile; no soportado en Compatibility).
    - [x] **Creating a VRS density map** (*Creación de un mapa de densidad VRS*)
      - Tabla de densidades (1x1 a 8x8) y asignación de colores RGB exactos.
      - Recomendaciones de tamaño de textura (256x256, 480x270) basadas en el tamaño de tesela (*tile size* de 8x8).
      - Uso conjunto con sesgo negativo de mipmap.
    - [x] **Performance comparison** (*Comparación de rendimiento*)
      - Tabla de comparativa en resoluciones 1080p, 1440p, 4K y 8K.

---

### 7. Índice Principal y Menús Globales
- [x] **Archivos objetivo:**
  - `tutorials/3d/index.html` (sección `#optimization` y bloque `toctree-l1`)
  - `_sources/tutorials/3d/index.rst.txt`
- [x] **Enlaces de la sección Optimización:**
  - [x] `Using MultiMeshInstance3D` -> `Uso de MultiMeshInstance3D`
  - [x] `Mesh level of detail (LOD)` -> `Nivel de detalle de malla (LOD)`
  - [x] `Visibility ranges (HLOD)` -> `Rangos de visibilidad (HLOD)`
  - [x] `Eliminación de oclusión` -> Mantener / Verificar consistencia
  - [x] `Resolution scaling` -> `Escalado de resolución`
  - [x] `Variable rate shading` -> `Sombreado de tasa variable (VRS)`
- [x] **Sincronización de barras laterales:**
  - [x] Actualizar títulos en el árbol de navegación lateral de las páginas 3D para que coincidan con los nuevos nombres en español.

---

## 📖 Glosario de Términos Clave

| Inglés | Español recomendado | Notas / Contexto |
| :--- | :--- | :--- |
| **Draw call** | Llamada de dibujo (*draw call*) | Mantener término técnico reconocible |
| **Level of detail (LOD)** | Nivel de detalle (LOD) | Siglas habituales |
| **Hierarchical LOD (HLOD)** | Nivel de detalle jerárquico (HLOD) | |
| **Occlusion culling** | Eliminación de oclusión | |
| **Occluder / Occludee** | Oclusor / Objeto ocluido | |
| **Bake / Baking** | Hornear / Horneado | Proceso de cálculo estático |
| **Frustum culling** | Recorte por tronco de visión (*frustum culling*) | |
| **Wireframe** | Malla alámbrica (*wireframe*) | |
| **Overdraw** | Sobregiro (*overdraw*) | Píxeles re-sombreados en la misma pasada |
| **Variable rate shading (VRS)** | Sombreado de tasa variable (VRS) | |
| **Foveated rendering** | Renderizado foveado | Relevante en VR/XR |
| **Mipmap bias** | Sesgo de mipmap | |
| **Dithering** | Tramado (*dithering*) | Técnica alternativa a la transparencia alfa |
| **Hysteresis** | Histéresis | Margen para evitar alternancias bruscas |
