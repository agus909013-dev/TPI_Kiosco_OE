# PERSISTENCIA DE DATOS & CONTROL DE ESTADOS - KIOSCO "EL PASO"


# 1. BASE DE DATOS SIMULADA (Inventario y Clientes)
INVENTARIO = {
    "1": {"producto": "Alfajor Triple", "precio": 1200, "stock": 15},
    "2": {"producto": "Gaseosa 500ml", "precio": 1800, "stock": 0},  # Sin stock para probar reglas de negocio
    "3": {"producto": "Papas Fritas Bolsa", "precio": 2500, "stock": 8}
}

CLIENTES_VIP = {
    "200": {"nombre": "Juan Pérez", "descuento": 0.10}, # 10% de descuento
    "300": {"nombre": "María López", "descuento": 0.00}
}

# 2. MÁQUINA DE ESTADOS COMPLETA
# Estados posibles: INICIO -> ESPERANDO_CLIENTE -> MENU_PRODUCTOS -> CONFIRMACION
sesion = {
    "estado_actual": "INICIO",
    "cliente_id": None,
    "producto_elegido": None
}
def procesar_pedido_kiosco(mensaje_usuario):
    global sesion
    entrada = mensaje_usuario.strip()

    # --- COMPUERTA 1: INICIO Y BIENVENIDA ---
    if sesion["estado_actual"] == "INICIO":
        sesion["estado_actual"] = "ESPERANDO_CLIENTE"
        return (
            "🏪 *[Kiosco El Paso]*: ¡Hola! Soy el asistente virtual para pedidos.\n"
            "Por favor, ingresá tu **Número de Cliente** (3 dígitos) o poné '000' si sos cliente nuevo:"
        )

    # --- COMPUERTA 2: VALIDACIÓN DE CLIENTE (Camino Infeliz y Feliz) ---
    elif sesion["estado_actual"] == "ESPERANDO_CLIENTE":
        # Camino Infeliz 1: Formato incorrecto
        if not entrada.isdigit() or len(entrada) != 3:
            return "❌ *[ERROR]*: El código debe ser de exactamente 3 números. Intentá de nuevo:"

        # Guardamos el tipo de cliente
        sesion["cliente_id"] = entrada
        sesion["estado_actual"] = "MENU_PRODUCTOS"

        # Mostramos el menú dinámico desde la "Base de Datos"
        texto_menu = "✅ *[CLIENTE RECONOCIDO]*\nAquí tenés nuestro stock disponible. Elegí el número de opción:\n"
        for k, v in INVENTARIO.items():
            texto_menu += f"[{k}] - {v['producto']} (${v['precio']}) - Stock: {v['stock']} u.\n"
        
        return texto_menu

    # --- COMPUERTA 3: SELECCIÓN DE PRODUCTO Y REGLAS DE NEGOCIO ---
    elif sesion["estado_actual"] == "MENU_PRODUCTOS":
        # Camino Infeliz 2: Opción que no existe en el menú
        if entrada not in INVENTARIO:
            return "⚠️ *[OPCIÓN INVÁLIDA]*: Ese producto no está en el menú. Seleccioná una opción válida:"

        producto = INVENTARIO[entrada]

        # REGLA DE NEGOCIO CRÍTICA: ¿Hay Stock? (Camino Infeliz de Negocio)
        if producto["stock"] <= 0:
            return f"🚫 *[SIN STOCK]*: Lo sentimos, no queda {producto['producto']}. Por favor, elegí otra opción:"

        # Guardamos el producto elegido y pasamos a la confirmación
        sesion["producto_elegido"] = entrada
        sesion["estado_actual"] = "CONFIRMACION"
        
        # Calcular precio base
        precio_final = producto["precio"]
        detalles_descuento = ""
        
        # Aplicar descuento si es cliente VIP existente
        if sesion["cliente_id"] in CLIENTES_VIP:
            desc = CLIENTES_VIP[sesion["cliente_id"]]["descuento"]
            if desc > 0:
                precio_final = producto["precio"] * (1 - desc)
                detalles_descuento = f" (¡Se aplicó {desc*100}% de desc. por Cliente VIP!)"

        return (
            f"🛒 *[RESUMEN DE TU PEDIDO]*:\n"
            f"• Producto: {producto['producto']}\n"
            f"• Total a pagar: ${precio_final:.2f}{detalles_descuento}\n\n"
            f"¿Confirmás el pedido para retirar por el local? (Respondé: **SI** o **NO**)"
        )

    # --- COMPUERTA 4: CIERRE DEL PROCESO ---
    elif sesion["estado_actual"] == "CONFIRMACION":
        opcion = entrada.upper()
        
        if opcion == "SI":
            # Simulamos la resta de stock en la BD
            prod_id = sesion["producto_elegido"]
            INVENTARIO[prod_id]["stock"] -= 1
            
            sesion["estado_actual"] = "INICIO" # Reseteo de la máquina de estados
            return "🎉 *[PEDIDO CONFIRMADO]*: Tu pedido ya está reservado y empaquetado. Podés pasar a retirarlo y abonarlo por caja. ¡Gracias!"
            
        elif opcion == "NO":
            sesion["estado_actual"] = "INICIO"
            return "❌ *[PEDIDO CANCELADO]*: Se canceló la operación. Si querés empezar de nuevo, escribí cualquier mensaje."
        
        else:
            return "⚠️ *[RESPUESTA INVÁLIDA]*: Por favor, respondé únicamente con **SI** o **NO**:"
        # INTERFAZ DE SIMULACIÓN EN VIVO
if __name__ == "__main__":
    print("-" * 60)
    print("🏪 SIMULADOR DE PEDIDOS AUTOMATIZADOS - KIOSCO 'EL PASO'")
    print("Escribí 'salir' para terminar.")
    print("-" * 60)
    
    print(procesar_pedido_kiosco("Iniciar"))
    
    while True:
        entrada_usuario = input("\n👤 Cliente: ")
        if entrada_usuario.lower() == "salir":
            break
        print(procesar_pedido_kiosco(entrada_usuario))
