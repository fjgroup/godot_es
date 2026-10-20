# Plan y Checklist de Traducción: Herramientas 3D

Plan de trabajo detallado y lista de verificación interactiva para traducir la sección de **Herramientas 3D** (`tutorials/3d/index.html#tools`) de la documentación oficial de Godot al español.

---

## 📂 Resumen de Archivos a Traducir

Cada tutorial consta de dos archivos sincronizados, además de las páginas de índice y barras laterales:

1. **Herramientas CSG (`csg_tools`)**:
   - `tutorials/3d/csg_tools.html`
   - `_sources/tutorials/3d/csg_tools.rst.txt`
2. **Uso de GridMaps (`using_gridmaps`)**:
   - `tutorials/3d/using_gridmaps.html`
   - `_sources/tutorials/3d/using_gridmaps.rst.txt`
3. **Brazo de resorte y cámara en 3ª persona (`spring_arm`)**:
   - `tutorials/3d/spring_arm.html`
   - `_sources/tutorials/3d/spring_arm.rst.txt`
4. **Índice principal y barras laterales**:
   - `tutorials/3d/index.html` (sección `#tools` y enlaces `toctree`)
   - `_sources/tutorials/3d/index.rst.txt`
   - Menús de navegación lateral cruzados en las páginas relacionadas

---

## 📋 Checklist Detallado por Tema y Subsecciones

### 1. Prototipado de niveles con CSG (`csg_tools`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/csg_tools.html`
  - `_sources/tutorials/3d/csg_tools.rst.txt`
- [x] **Título principal:**
  - [x] *Prototyping levels with CSG* -> *Prototipado de niveles con CSG* (o *Prototipando niveles con CSG*)
- [x] **Subsecciones a traducir:**
  - [x] **Introducción y conceptos básicos:**
    - Definición de CSG (*Constructive Solid Geometry* / Geometría Sólida Constructiva) y operadores booleanos.
    - Casos de uso: prototipado rápido de niveles, combinación de primitivas y entornos interiores mediante primitivas invertidas.
    - Nota de limitaciones: CSG no sustituye el modelado 3D profesional (sin edición UV avanzada), recomendación de plugins externos (*FuncGodot*, *Cyclops Level Builder*).
    - Enlace al proyecto demo oficial de CSG y video incrustado.
  - [x] **Introduction to CSG nodes** (*Introducción a los nodos CSG*)
    - Listado y enlaces a clases: `CSGBox3D`, `CSGCylinder3D` (soporte de cono), `CSGSphere3D`, `CSGTorus3D`, `CSGPolygon3D`, `CSGMesh3D`, `CSGCombiner3D`.
    - [x] **CSG tools features** (*Funcionalidades de las herramientas CSG*)
      - Operaciones booleanas: **Unión** (*Union*), **Intersección** (*Intersection*) y **Sustracción** (*Subtraction*).
    - [x] **CSGPolygon** (*CSGPolygon3D*)
      - Modos de extrusión 2D: **Profundidad** (*Depth*), **Giro** (*Spin*), y **Ruta** (*Path* / *lofting*).
      - Requisito del nodo `Path3D` para el modo Path.
    - [x] **Custom meshes** (*Mallas personalizadas*)
      - Requisitos para mallas personalizadas (*manifold* / cerradas, cada arista conectada a exactamente dos caras, con volumen).
      - Elementos a evitar: volumen negativo, autointersecciones, caras internas.
      - Definición técnica de *manifold* según la librería de Godot.
      - [x] **Making an existing mesh manifold with Blender** (*Hacer que una malla existente sea manifold con Blender*)
        - Pasos con el complemento *3D Print Toolbox* (*Print3D Toolbox*): Clean Up -> Make Manifold.
    - [x] **CSGCombiner3D** (*CSGCombiner3D*)
      - Contenedor organizativo que combina operaciones exclusivamente entre sus nodos hijos.
    - [x] **Processing order** (*Orden de procesamiento*)
      - Procesamiento en orden de árbol de escena (*tree order*).
      - Recomendaciones de rendimiento: evitar árboles monolíticos con excesivos objetos, separar muebles/habitaciones en árboles independientes.
  - [x] **Prototyping a level** (*Prototipado de un nivel paso a paso*)
    - Configuración del visor 3D (proyección ortogonal, modo *Display Overdraw* o luz direccional de apoyo).
    - Construcción de la habitación (`room`: CSGBox3D con *Invert Faces*).
    - Construcción del escritorio (`desk`: CSGCombiner3D con superficie y 4 patas en modo Unión).
    - Construcción de la cama (`bed`: estructura, colchón y almohada `pillow` en modo Sustracción; demostración didáctica del orden de procesamiento al reemparentar nodos).
    - Construcción de la lámpara (`lamp`: base cónica, poste cilíndrico, pantalla mediante CSGPolygon3D en modo Spin con sección trapezoidal).
    - Construcción de la estantería (`bookshelf`: caja exterior, recorte sustractivo interior y estante separador).
  - [x] **Using prototype textures** (*Uso de texturas prototipo*)
    - Mapeo triplanar (*triplanar mapping*) en `StandardMaterial3D` para texturizar sin requerir mapa UV manual.
    - Recursos CC0 de texturas prototipo (Kenney).
    - Métodos de aplicación: `Material Override` en CSGCombiner3D vs. `Material` en nodos individuales (transferencia de material en operaciones sustractivas).
    - Configuración en el Inspector: Albedo, UV1 Triplanar, Scale y Offset. Copiado y pegado de materiales.
  - [x] **Converting to MeshInstance3D** (*Conversión a MeshInstance3D* - Característica Godot 4.4+)
    - Ventajas: horneado de lightmaps (UV2), horneado de occlusion culling, tiempos de carga optimizados y mejor rendimiento de transformaciones.
    - Procedimiento: botón de barra de herramientas `CSG > Bake Mesh Instance` y ocultación de la geometría CSG original.
    - Horneado de formas de colisión: `CSG > Bake Collision Shape` (trimesh) para `StaticBody3D` o `AnimatableBody3D`.
    - Conservación del nodo CSG original para futuras modificaciones.
  - [x] **Exporting as glTF** (*Exportación como glTF*)
    - Flujo de trabajo de bloqueo (*blockout*) y exportación mediante `Scene > Export As... > glTF 2.0 Scene`.

---

### 2. Uso de GridMaps (`using_gridmaps`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/using_gridmaps.html`
  - `_sources/tutorials/3d/using_gridmaps.rst.txt`
- [x] **Título principal:**
  - [x] *Using GridMaps* -> *Usar GridMaps*
- [x] **Subsecciones a traducir:**
  - [x] **Introduction** (*Introducción*)
    - Concepto de GridMap como equivalente 3D de TileMap 2D mediante colecciones de mallas (`MeshLibrary`).
    - Integración de mallas con colisiones y navegación.
  - [x] **Example project** (*Proyecto de ejemplo*)
    - Descarga de `gridmap_starter.zip`, importación y conversión a la versión actual de Godot.
  - [x] **Creating a MeshLibrary** (*Creación de una MeshLibrary*)
    - Estructura de la escena fuente (`mesh_library_source.tscn`): nodo raíz `Node3D` e hijos `MeshInstance3D`.
  - [x] **Collisions** (*Colisiones*)
    - Configuración manual con `StaticBody3D` y `CollisionShape3D`, o automática desde el menú `Mesh`.
    - Diferencia entre cuerpo convexo (*Convex*) y trimalla estática (*Trimesh Static Body*).
  - [x] **Materials** (*Materiales*)
    - Requisito de materiales asignados internamente en el recurso de malla (se ignoran los del nodo).
  - [x] **NavigationMeshes** (*Mallas de navegación*)
    - Adición de `NavigationRegion3D` como hijo de `MeshInstance3D` para hornear la navegación de cada elemento de GridMap.
    - Ajustes para celdas pequeñas (radio del agente y tamaño mínimo de región).
    - Advertencia sobre la sincronización del tamaño de celda (*cell size*) entre NavigationMesh y NavigationServer.
  - [x] **Lightmaps** (*Mapas de luz*)
    - Horneado de lightmaps sobre GridMap: reutilización o autogeneración de UV2 (texel size de 0.1 unidades).
    - Configuración previa de GI en el dock Import (*Static Lightmaps*).
  - [x] **MeshLibrary format** (*Formato de MeshLibrary*)
    - Resumen de reglas estructurales: raíz Node3D, mallas visuales exportadas, asignación de materiales, cuerpos estáticos y regiones de navegación.
  - [x] **Exporting the MeshLibrary** (*Exportación de la MeshLibrary*)
    - Procedimiento en el editor: `Scene > Export As... > MeshLibrary...` y archivo `.tres`.
  - [x] **Using GridMap** (*Uso del nodo GridMap*)
    - Asignación de recurso `MeshLibrary` al nodo `GridMap`.
    - [x] **Inspector properties** (*Propiedades del Inspector*)
      - Ajustes de `Physics Material`, dimensiones de celdas (`Cells > Size`, `Center Y`), capas/máscaras de colisión, y `Bake Navigation`.
      - Ajustes individuales por malla en el inspector de `MeshLibrary` (capas de navegación, sombras).
    - [x] **GridMap panel** (*Panel inferior de GridMap*)
      - Herramientas de la barra: Transform, Selection, Erase, Paint, Pick, Fill, Move, Duplicate, Delete.
      - Atajos de rotación de cursor en ejes X, Y, Z.
      - Selector de piso (*Change Grid Floor*), buscador de mallas, zoom y alternadores de disposición.
      - Menú de herramientas y ajuste de distancia de selección (*Pick Distance*).
  - [x] **Using GridMap in code** (*Uso de GridMap mediante código*)
    - Enlace a la documentación de API de la clase `GridMap`.

---

### 3. Cámara en tercera persona con brazo de resorte (`spring_arm`)
- [x] **Archivos objetivo:**
  - `tutorials/3d/spring_arm.html`
  - `_sources/tutorials/3d/spring_arm.rst.txt`
- [x] **Título principal:**
  - [x] *Third-person camera with spring arm* -> *Cámara en tercera persona con brazo de resorte (SpringArm3D)*
- [x] **Subsecciones a traducir:**
  - [x] **Introduction** (*Introducción*)
    - El problema del recorte (*clipping*) de cámaras en 3D a través de paredes y geometría.
    - Función del nodo `SpringArm3D`.
  - [x] **What is a spring arm?** (*¿Qué es un brazo de resorte?*)
    - Parámetros clave: Longitud (*length*) y Forma de colisión (*shape*).
    - Concepto de barrido (*sweep*) y reposicionamiento automático de los nodos hijos en el punto de impacto.
  - [x] **Spring arm with a camera** (*Brazo de resorte con cámara*)
    - Generación automática de una pirámide de colisión que representa el plano cercano (*near plane*) de la cámara.
    - Condición: la cámara debe ser hija directa del brazo de resorte (o fallback a *raycast* menos preciso).
    - Proyección de movimiento (*motion cast*) en cada fotograma de físicas.
  - [x] **Setting up the spring arm and camera** (*Configuración del brazo de resorte y la cámara*)
    - Proyecto base: *Platformer 3D demo* (GitHub / Asset Library).
    - Jerarquía de nodos recomendada:
      ```text
      Node3D (Pivote de cámara)
      └── SpringArm3D
          └── Camera3D
      ```
    - Configuración en `player.tscn` con nombres únicos de escena (`%Camera3D`, `%CameraPivot`).
    - Elevación del pivote en eje Y y ajuste de longitud (`length = 3`).
    - Selección de forma: forma vacía `<empty>` para usar el plano de cámara, o esfera para deslizamiento suave.
    - [x] **Scripting en GDScript (`player.gd`)**:
      - Variables `@onready` para cámara y pivote.
      - Implementación de vista de ratón (*mouselook*) en `_unhandled_input` con `event.screen_relative` y sensibilidad.
      - Restricción de cabeceo con `clampf` y límite de inclinación (*tilt limit*).
      - Demostración de funcionamiento y video incrustado.

---

### 4. Sincronización de Índices y Menús Globales
- [x] **Archivos objetivo:**
  - `tutorials/3d/index.html` (sección `#tools` y enlaces relacionados)
  - `_sources/tutorials/3d/index.rst.txt`
- [x] **Verificación de consistencia de títulos en menú:**
  - [x] `Prototyping levels with CSG` -> `Prototipando niveles con CSG` (unificado en todo el proyecto)
  - [x] `Using GridMaps` -> `Usar GridMaps` (unificado con el resto de tutoriales)
  - [x] `Third-person camera with spring arm` -> `Cámara en tercera persona con brazo de resorte`
- [x] **Sincronización de barras laterales:**
  - [x] Asegurar que los menús `toctree` de todas las páginas de la sección 3D muestren los títulos traducidos coherentes (44 archivos sincronizados en `tutorials/3d/` y subdirectorios).

---

## 📖 Glosario de Términos Clave (Herramientas 3D)

| Inglés | Español recomendado | Notas / Contexto |
| :--- | :--- | :--- |
| **Constructive Solid Geometry (CSG)** | Geometría Sólida Constructiva (CSG) | Sigla técnica estándar |
| **Boolean operations** | Operaciones booleanas | Unión, Intersección, Sustracción |
| **Manifold (mesh)** | Manifold (malla cerrada válida) | Propiedad topológica obligatoria en CSG |
| **Extrude / Extrusion** | Extruir / Extrusión | Modo de CSGPolygon3D |
| **Spin** | Giro / Girar | Extrusión circular alrededor del origen |
| **Lofting / Path extrusion** | Transición / Extrusión a lo largo de ruta (*lofting*) | Modo Path en CSGPolygon3D |
| **Invert Faces** | Invertir caras (*Invert Faces*) | Para crear interiores huecos |
| **Blockout / Blocking out** | Bloqueo de nivel (*blockout*) | Fase de prototipado geométrico |
| **Triplanar mapping** | Mapeo triplanar (*triplanar mapping*) | Texturizado sin coordenadas UV explícitas |
| **Material override** | Sobrescritura de material (*material override*) | Propiedad en CSGCombiner3D y GeometryInstance3D |
| **Bake Mesh Instance** | Hornear instancia de malla (*Bake Mesh Instance*) | Novedad de Godot 4.4 |
| **Bake Collision Shape** | Hornear forma de colisión (*Bake Collision Shape*) | Novedad de Godot 4.4 |
| **GridMap** | GridMap | Nombre del nodo y concepto de mapa en cuadrícula 3D |
| **MeshLibrary** | Biblioteca de mallas (*MeshLibrary*) | Recurso que contiene la colección de bloques 3D |
| **Convex / Trimesh body** | Cuerpo convexo / Cuerpo trimalla | Tipos de colisión estática |
| **Spring arm** | Brazo de resorte (*spring arm*) | Mecanismo de cámara antipenetración |
| **Motion cast / Sweep** | Proyección de movimiento (*motion cast*) / Barrido (*sweep*) | Detección de colisión volumétrica continua |
| **Near plane** | Plano cercano (*near plane*) | Plano de recorte frontal de la cámara |
| **Camera pivot** | Pivote de cámara (*camera pivot*) | Nodo origen de rotación para la cámara |
| **Mouselook** | Control de vista con ratón (*mouselook*) | Movimiento de cámara basado en ratón |
| **Screen-relative** | Relativo a la pantalla (*screen-relative*) | Propiedad de sensibilidad independiente de resolución |

---

## 🛠️ Directrices Técnicas de Traducción

1. **Preservar anclas y enlaces internos:**
   - Mantener intactos los identificadores de sección en HTML (`id="introduction-to-csg-nodes"`, `id="collisions"`, etc.) y las etiquetas de anclaje Sphinx en RST (`.. _doc_csg_tools:`, `.. _doc_using_gridmaps:`).
2. **Respetar nombres de API y nodos de Godot:**
   - Mantener literales exactos para nodos, métodos y propiedades: `CSGBox3D`, `CSGCombiner3D`, `GridMap`, `MeshLibrary`, `SpringArm3D`, `Camera3D`, `screen_relative`, `clampf`, etc.
3. **Consistencia de interfaz del editor:**
   - Usar negrita para elementos de la interfaz de Godot: **Scene > Export As... > MeshLibrary...**, **Geometry > Material Override**, **CSG > Bake Mesh Instance**, etc.
4. **Metadatos HTML completos:**
   - Actualizar siempre `<title>`, `og:title`, `description` y `og:description` en cada archivo `.html` compilado.
5. **Comentarios en bloques de código:**
   - Traducir los comentarios dentro de los ejemplos de código GDScript para máxima claridad del lector hispanohablante.
