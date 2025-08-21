from .models import Cart, CartItem


def cart_counter(request):
    """Provide `counter` (total quantity) for the cart across all templates."""
    try:
        cart_id = request.session.session_key or request.session.create()
        cart = Cart.objects.filter(cart_id=cart_id).first()
        if not cart:
            return {"counter": 0}
        items = CartItem.objects.filter(cart=cart, active=True)
        total_quantity = sum(item.quantity for item in items)
        return {"counter": total_quantity}
    except Exception:
        return {"counter": 0}


