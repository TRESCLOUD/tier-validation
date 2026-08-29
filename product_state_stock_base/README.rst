===================
Product State Stock
===================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fproduct--attribute-lightgray.png?logo=github
    :target: https://github.com/OCA/product-attribute/tree/18.0/product_state_stock_base
    :alt: OCA/product-attribute

|badge1| |badge2| |badge3|

Este módulo agrega el uso de los estados de producto (módulo ``product_state``)
en el flujo de Inventario: expone el menú de configuración de Estados de
Producto también bajo Inventario, y otorga a los responsables de inventario
el permiso para administrarlos.

**Tabla de contenidos**

.. contents::
   :local:

Características
================

* Expone el menú de configuración de Estados de Producto (``product_state``)
  también bajo *Inventario > Configuración > Productos*.
* Otorga al grupo de Responsable de Inventario (``stock.group_stock_manager``)
  el permiso de Responsable de Estados de Producto
  (``product_state.group_product_state_manager``).

Uso
===

Para acceder a los estados de producto desde Inventario:

1. Ve a *Inventario > Configuración > Productos > Estados de Producto*.
2. Puedes definir su nombre y una descripción, igual que desde el menú
   original de ``product_state``.

Créditos
========

Autores
-------

* Camptocamp

Colaboradores
-------------

- `Trobz <https://trobz.com>`__:

  - Tuan Nguyen <tuanna@trobz.com>

Otros créditos
--------------

El desarrollo de este módulo fue financiado por Camptocamp.

Mantenedor
----------

Este módulo es mantenido por la OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

La OCA, u Odoo Community Association, es una organización sin fines de lucro
cuya misión es apoyar el desarrollo colaborativo de funcionalidades de Odoo y
promover su uso extendido.

Changelog
=========

* 1.0: Migración a Odoo 20.
